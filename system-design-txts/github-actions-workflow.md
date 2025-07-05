Use manual testing for smaller parts

Test Docker build locally:

docker build -t my-chatbot-app .
docker run -p 8501:8501 my-chatbot-app


Test kubectl deployment:
After authenticating to your AKS cluster with az aks get-credentials, try:


kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml