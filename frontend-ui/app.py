import streamlit as st
import requests

API_URL = "http://backend:5000"

st.title("Auth System")

menu = st.sidebar.selectbox("Menu", ["Login", "Signup", "Forgot Password"])

if menu == "Signup":
    st.subheader("Create Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        res = requests.post(f"{API_URL}/signup", json={"email": email, "password": password})
        st.success(res.json().get("message", "Signup complete"))

elif menu == "Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        res = requests.post(f"{API_URL}/login", json={"email": email, "password": password})
        if res.status_code == 200:
            st.success("Login successful")
            st.json(res.json())
        else:
            st.error(res.json().get("message", "Login failed"))

elif menu == "Forgot Password":
    st.subheader("Reset Password")
    email = st.text_input("Email")
    if st.button("Send Reset Link"):
        res = requests.post(f"{API_URL}/forgot-password", json={"email": email})
        st.info(res.json().get("message", "If registered, reset link sent"))
