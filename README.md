# Weather_Flask_App
This project will be used to demonstrate how it works in Kubernetes.

### Microservice scheme
![alt text](https://github.com/ElizavetaDavydova07/Weather_Flask_App/blob/main/scheme.png)

### Built With:
- Docker - Deployment model
- Flask - The web framework
- Python - programming language
- pip - Package and dependency manager
- MySQL - Database
- Kubernetes - Container-orchestration system

### Build docker image:
```
docker build -t localhost:32000/weather/app:1.0.0 -f Dockerfile
```
### Push docker image to local microk8s registry:
```
docker push localhost:32000/weather/app:1.0.0
```
### Apply config:
```
kubectl apply -f ./k8s-conf/app.deployment.yaml
```
