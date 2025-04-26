from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt, datetime
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Database URI using environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/appdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "User already exists"}), 400
    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    new_user = User(email=data["email"], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user and bcrypt.check_password_hash(user.password, data["password"]):
        token = jwt.encode(
            {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config["SECRET_KEY"], algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user:
        # Simulate sending a reset token
        return jsonify({"reset_token": "dummy-reset-token"})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
