.PHONY: setup
setup:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate && pip install -r requirements.txt"

.PHONY: up
up:
	docker-compose build
	docker-compose up

.PHONY: deploy-database
deploy-database:
	# Pre-request that directory must be presented
	sudo mkdir -p /opt/mysql-pvc/
	# Apply database config
	kubectl apply -f ./k8s-conf/mysql.deployment.yaml

.PHONY: deploy-app
deploy-app:
	# Build docker image
	docker build -t localhost:32000/weather/app:1.0.0 -f Dockerfile .
	# Push docker image to local microk8s registry
	docker push localhost:32000/weather/app:1.0.0
	# Apply config 
	kubectl apply -f ./k8s-conf/app.deployment.yaml

