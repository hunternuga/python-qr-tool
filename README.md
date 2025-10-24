# Python QR Code Generation Application
> This mini Python app is built using k8s, minikube, docker & `render.com`'s free hosting service for public viewing and use.
> To use, simply navigate to `https://python-qr-tool.onrender.com` to utilize.

# pre-requisites
- docker
- minikube
- python (at least 3.11, have not tested it with more recent versions)
- it is best to use a virtual python environment (venv) when working locally to avoid library issues.

docker & python:
- a simple dockerfile is used to build the image for the Python app using flask.

k8s & minikube:
- a minikube container is uses a Docker built image, loads it, and makes it availbe for use after being port forwarded to port 5000, @ `localhost`.
- a `deployment.yaml` file is used to deploy the service via `kubectl`. the pod and service are then created.

`render.com` hosting (optional, for public viewing):
- the application image is built and passed into a `render.com` web service and deploys it using the dockerfile and Python flask.
- the application can be used at the following url: `https://python-qr-tool.onrender.com`

other information:
- the application, when built and deployed locally with minikube, needs to be port forwarded to localhost:5000. this can be done very easily by running the command `kubectl port-forward service/qr-app-service 5000:5000`. this allows the app to be accessible locally for development/testing or even personal use!
