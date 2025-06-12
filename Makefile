# Default version of Python (for Docker testing)
PYTHON_VERSION := "3.13"
UV_PATH := $(shell which uv 2>/dev/null)

.PHONY: help
help:
	@echo "Usage: make <target> [PYTHON_VERSION=3.11]"
	@echo "\nTargets:"
	@echo "  install            Install this package (pip install)"
	@echo "  docs               Build Sphinx documentation"
	@echo "  test               Run unit tests"
	@echo "  coverage           Build an HTML coverage report"
	@echo "  lint               Run 'ruff' linting on project"
	@echo "  docker-test        Run unit tests in Docker container"
	@echo "\nSpecial Targets:"
	@echo "  docker-test-all    Runs unit tests in Docker containers across all versions of Python"


# Install UV if it is not installed
.PHONY: uv-init
uv-init:
	@if [ -z "$(UV_PATH)" ]; then curl -LsSf https://astral.sh/uv/install.sh | sh; fi

.PHONY: install
install:
	@python -m pip install .

.PHONY: docs
docs: uv-init
	@uv export --group docs --format requirements.txt --no-hashes -o docs/requirements.txt >/dev/null
	@uv run --group docs sphinx-build -b html docs/source/ docs/build/html/

.PHONY: test
test: uv-init
	@uv run --group test coverage run -m unittest discover tests/

.PHONY: coverage
coverage: test
	@coverage html

.PHONY: lint
lint: uv-init
	@uv run --group test ruff check picklejar.py

.PHONY: docker-test-all
docker-test-all:
	@$(MAKE) docker-test PYTHON_VERSION=3.9
	@$(MAKE) docker-test PYTHON_VERSION=3.10
	@$(MAKE) docker-test PYTHON_VERSION=3.11
	@$(MAKE) docker-test PYTHON_VERSION=3.12
	@$(MAKE) docker-test PYTHON_VERSION=3.13

# Private target for docker-tests
.PHONY: docker-test
docker-test:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install uv && uv run --group test python -m unittest discover ./tests/'
