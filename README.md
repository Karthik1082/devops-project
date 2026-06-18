# Devops Project

A complete CI/CD pipeline that automatically builds, containerizes and deploys a web application to Kubernetes.

## Tech Stack

- Docker
- Kubernetes
- GitHub Actions

## How it Works

1. Developer pushes code to Github
2. GitHub Actions automatically triggers
3. Pipeline builds Docker image from the code
4. Image is pushed to Docker Hub
5. Kubernetes Deployment and Service are created using this image
6. Application runs with 2 replica pods

## Local Testing Note

Tested locally using Minikube. Since Minikube is a local cluster, it doesn't provide a real external IP for LoadBalancer service (unlike cloud platforms like GKE). Used 'minikube service --url' to access the application for local testing. In production on GKE, LoadBlancer automatically provisions a real external IP.

## How to Run Locally

'''bash
#Build Docker image
docker build -t karthik-app:v1 .

#Run container
docker run -d -p 8080:80 karthik-app:v1

#Or deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
'''

