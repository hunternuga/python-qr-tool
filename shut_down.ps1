# ---------------------------------------------
# shut_down.ps1
# Safely shuts down and cleans up QR app deployment
# ---------------------------------------------

# Variables
$imageName = "qr-app"

# Ensure script is running elevated
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Error "Please run this script as Administrator."
    exit 1
}

Write-Host "`n[1/4] Removing Kubernetes deployment and service..."
kubectl delete deployment $imageName --ignore-not-found
kubectl delete service "$imageName-service" --ignore-not-found

Write-Host "`n[2/4] Removing Docker image..."
docker rmi "${imageName}:latest" --force

Write-Host "`n[3/4] Stopping Minikube..."
minikube stop

Write-Host "`n[4/4] Cleaning up Minikube resources..."
minikube delete

Write-Host "`nCleanup complete! All resources have been removed.`n"
Write-Host "To redeploy the application, run deploy.ps1`n"