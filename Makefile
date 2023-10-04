MANAGE = python manage.py
.
VENV = venv

DOCKER_COMPOSE = docker-compose

run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser

collectstatic:
	$(MANAGE) collectstatic --no-input

install: $(VENV) requirements.txt
	$(VENV)/bin/pip install -r requirements.txt

$(VENV):
	python3 -m venv $(VENV)

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rmdir {} \; 2>/dev/null || true

docker-up:
	$(DOCKER_COMPOSE) up --build

docker-down:
	$(DOCKER_COMPOSE) down

.PHONY: run migrate createsuperuser test collectstatic install clean docker-up docker-down
