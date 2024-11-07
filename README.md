
# Personal Finance Tracker with Automated Cloud Deployment

An expense-tracking app built in Python, deployed on AWS EKS with a CI/CD pipeline for streamlined and seamless updates.

## Features

- **Expense Tracking by Category**: Log and categorize expenses with an intuitive interface.
- **Visual Analytics**: Automatically generates a pie chart, displaying expenses by category with percentage breakdown.
- **AWS Cloud Deployment**: Deployed on AWS EKS for scalability and reliability.
- **CI/CD Pipeline with Self-Hosted Runner**: A self-hosted GitHub Actions runner automates the app's deployment process, ensuring rapid and seamless updates.

## Project Structure

- **`main.py`**: Core Flask application logic, managing routes for expense entry, report generation, and data storage.
- **`report.py`**: Generates visual reports using Plotly, rendering a pie chart that breaks down expenses by category.
- **`Dockerfile`**: Configures the application for deployment in a containerized environment.
- **Kubernetes (`k8s/`) Files**: Kubernetes configurations for deployment and service setup (`app-deployment.yaml`, `app-service.yaml`).
- **GitHub Workflow (`.github/workflows/deploy.yaml`)**: CI/CD pipeline for automated Docker image building and Kubernetes deployment, leveraging a self-hosted GitHub Actions runner.

## Technologies Used

- **Python / Flask**: For backend application logic and handling HTTP requests.
- **AWS DynamoDB**: To store and manage expense records.
- **Plotly**: For generating pie chart reports on expenses.
- **Docker**: For containerizing the application.
- **AWS EKS**: For managing and deploying the app in a scalable Kubernetes environment.
- **GitHub Actions (Self-Hosted Runner)**: Automates deployment with continuous integration and delivery, hosted on a self-managed server.

## Deployment Pipeline

The CI/CD pipeline leverages GitHub Actions with a self-hosted runner, enabling:

1. **Automated Builds**: Builds the Docker image on each push.
2. **Seamless Deployment**: Pushes the image to Docker Hub and deploys it to EKS.
3. **Self-Hosted Runner Benefits**: Running the CI/CD pipeline on a self-hosted server provides enhanced control, security, and faster job execution.
