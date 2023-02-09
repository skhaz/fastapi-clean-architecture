.PHONY: help run tests vet

.SILENT:

SHELL := bash -eou pipefail

export PYTHONPATH=.

ifeq ($(shell command -v docker-compose;),)
	COMPOSE := docker compose
else
	COMPOSE := docker-compose
endif

help:
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

run: ## Run the project using docker-compose
	$(COMPOSE) up --build

test: vet ## Run tests
	poetry run pytest --cov=app tests/

vet: ## Run linters, type-checking, auto-formaters, and other tools
	poetry run black app/ tests/
	poetry run flake8 app/ tests/
	poetry run isort app/ tests/
	poetry run mypy app/ tests/