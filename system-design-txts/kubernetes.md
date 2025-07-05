How is Kubernetes Used - CI/CD Integration
Your GitHub Actions workflow builds your Docker image, pushes it to a registry, then deploys the updated app to AKS. This continuous integration and deployment pipeline lets you release new chatbot versions seamlessly.

How it works end-to-end for your chatbot
Develop chatbot app locally → write code + Dockerfile + Kubernetes manifests.

Push code to GitHub → triggers GitHub Actions workflow.

Workflow builds Docker image → pushes image to GitHub Container Registry.

Workflow authenticates to Azure AKS → configures kubectl context.

Workflow applies Kubernetes manifests → AKS pulls new Docker image, updates running pods.

AKS runs the chatbot container(s) → manages scaling, health checks, networking.

Users access chatbot → through the service exposed by AKS, load balanced to pods.

Summary in simple terms
AKS runs your chatbot inside containers on Azure cloud servers.

It automates running, scaling, and managing those containers reliably.

It connects your GitHub automated builds to live deployment of the chatbot.

This makes your chatbot production-ready, scalable, and easy to update.

