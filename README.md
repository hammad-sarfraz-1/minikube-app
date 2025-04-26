# Full-Stack Microservices Authentication App

A full-stack microservices application with authentication service, PostgreSQL database, and frontend. Deployed using Docker, Kubernetes (Minikube), and JWT for user authentication.
Tech Stack
  
    Frontend: React / Vue / Angular
  
    Backend: Flask / Django / Node.js
  
    Database: PostgreSQL
  
    Authentication: JWT
  
    Orchestration: Kubernetes (Minikube)

 1. Clone the repository:

        git clone https://github.com/hammad-sarfraz-1/minikube-app.git
        cd your-repository

2. Build Docker images:

        docker build -t frontend:latest ./frontend
        docker build -t backend-auth:latest ./backend-auth

3. Deploy on Minikube:
        
        minikube start
        kubectl apply -f k8s/*

4. Access the app:

        minikube service frontend-service

5. Apply Database Secrets:

        kubectl apply -f db/secrets.yml

6. Troubleshooting Commands:

   View logs:

          kubectl logs <pod-name>
   Check service status:

          kubectl get pods
          kubectl get services
    
