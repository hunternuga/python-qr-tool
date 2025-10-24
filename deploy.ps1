# ---------------------------------------------
# deploy-qr-app.ps1
# Automates Docker + Minikube deployment for qr-app
# ---------------------------------------------

# Variables
$imageName = "qr-app"
$deploymentFile = "deployment.yaml"

# Ensure script is running elevated
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Error "Please run this script as Administrator."
    exit 1
}

Write-Host "`n[1/5] Building Docker image '${imageName}:latest' ..."
docker build -t "${imageName}:latest" .

Write-Host "`n[2/5] Starting Minikube (Docker runtime)..."
minikube start --container-runtime=docker
Write-Host "`n[3/5] Loading image into Minikube..."
minikube image load "${imageName}:latest"

Write-Host "`n[4/5] Deleting old deployment/service if they exist..."
kubectl delete deployment $imageName --ignore-not-found
kubectl delete service "$imageName-service" --ignore-not-found

Write-Host "`n[5/5] Applying new deployment/service..."
kubectl apply -f $deploymentFile

Write-Host "`nWaiting for pod to be ready..."
kubectl wait --for=condition=Ready pod -l app=$imageName --timeout=120s

Write-Host "`nDeployment complete! Current pod status:"
kubectl get pods

Write-Host "`nService info:"
kubectl get svc

$minikubeIP = minikube ip
Write-Host "`nAccess your app at: https://${minikubeIP}:30000`n"
