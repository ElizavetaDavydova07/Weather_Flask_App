.PHONY: setup
setup:
	python3 -m venv .venv
	bash -c "source .venv/bin/activate && pip install -r requirements.txt"

.PHONY: up
up:
	docker-compose build
	docker-compose up
