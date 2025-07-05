# ClinicalTrialStudiesChatbot
Chatbot to answer user's queries on clinical trial study documents. 

python -m venv qa_venv
cd C:\Users\Administrator\Documents\ClinicalTrialStudiesChatbot
.\qa_venv\Scripts\activate


pip install -r requirements.txt
ollama run llama3
streamlit run app.py


Docker
wsl --install --no-distribution
[1] Restart Your Computer

wsl --install -d Ubuntu
[1] Open Docker Desktop
[2] Go to Settings > Resources > WSL Integration
[3] Toggle Ubuntu ON (or whatever distro you installed)
[4] Click "Apply & Restart"



docker init
docker compose up --build


Azure CLI
az login
az account list --output table
az account set --subscription "SUBSCRIPTION_NAME"

winget install -e --id Kubernetes.kubectl
Path environment variable modified; restart your shell to use the new value.
Command line alias added: "kubectl"


az group create --name chatbot-resource-group --location eastus        
{
  "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/chatbot-resource-group",
  "location": "eastus",
  "managedBy": null,
  "name": "chatbot-resource-group",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}


az provider register --namespace Microsoft.OperationalInsights
az provider show --namespace Microsoft.OperationalInsights --query "registrationState"

az provider register --namespace microsoft.insights
az provider show --namespace microsoft.insights --query "registrationState"

 az aks create --resource-group chatbot-resource-group --name chatbot-azure-kubernetes --node-count 1 --enable-addons monitoring --generate-ssh-keys --node-vm-size Standard_D2s_v3


 Push Docker Image to GitHub Container Registry (GHCR)

 az ad sp create-for-rbac --name github-actions-deployer --role contributor --scopes /subscriptions/SUBSCRIPTION_ID/resourceGroups/chatbot-resource-group --sdk-auth

 Creating 'contributor' role assignment under scope '/subscriptions/SUBSCRIPTION_ID/resourceGroups/chatbot-resource-group'

JSON output added to AZURE_CREDENTIALS in GitHub Secrets
 https://github.com/Soumya0190/ClinicalTrialStudiesChatbot/settings/secrets/actions


| Secret              | Used For                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------ |
| `GHCR_PAT`          | Logging in to GitHub Container Registry (`docker login ghcr.io`) so Docker can push images |
| `AZURE_CREDENTIALS` | Authenticating to Azure to set context for Kubernetes (`az login` & `kubectl`)             |



✅ What is GitHub Actions?
GitHub Actions is CI/CD automation built into GitHub. You can use it to:

| Task           | Example                                        |
| -------------- | ---------------------------------------------- |
| 🏗 Build code  | Build Docker images for your app               |
| 📦 Package app | Push image to GitHub Container Registry (GHCR) |
| 🚀 Deploy app  | Deploy it to AKS (Kubernetes)                  |
| 🧪 Run tests   | Lint or test Python/Streamlit code             |
| 🔁 Automate    | Run on push, pull requests, or on a schedule   |

🔄 Trigger: This workflow will automatically run every time manual trigger from GitHub UI


az aks get-credentials --name Chatbot-Azure-Kubernetes --resource-group Chatbot-resource-group

kubectl apply -f kubernetes/deployment.yaml
        deployment.apps/chatbot-deployment created
kubectl apply -f kubernetes/service.yaml   
        service/chatbot-service created


kubectl get deployments
NAME                 READY   UP-TO-DATE   AVAILABLE   AGE
chatbot-deployment   0/1     1            0           7m18s

kubectl get pods
NAME                                  READY   STATUS             RESTARTS   AGE
chatbot-deployment-65c77fc5f7-57m59   0/1     InvalidImageName   0          7m26s

kubectl get services
NAME              TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
chatbot-service   LoadBalancer   10.0.63.162   135.237.66.86   80:32415/TCP   2m46s
kubernetes        ClusterIP      10.0.0.1      <none>          443/TCP        61m