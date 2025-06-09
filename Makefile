PYTHON_VERSION := $(shell python --version | grep -Eo '[2-3].[0-9]+')
UV_PATH := $(shell which uv 2>/dev/null)

.PHONY: init
init:
	@if [ -z "$(UV_PATH)" ]; then curl -LsSf https://astral.sh/uv/install.sh | sh; fi

.PHONY: docs
docs: init
	@uv export --group docs --format requirements.txt --no-hashes -o docs/requirements.txt
	@uv run --group docs sphinx-build -b html docs/source/ docs/build/html/

.PHONY: test
test: init
	@uv run --group dev coverage run -m unittest discover tests/

.PHONY: test-coverage
test-coverage: test
	@coverage html

.PHONY: test-lint
test-lint: init
	@uv run --group dev ruff check picklejar.py

.PHONY: docker-test-all
docker-test-all: docker-test-py39 docker-test-py310 docker-test-py311 docker-test-py312 docker-test-py313

.PHONY: docker-test-latest
docker-test-latest: docker-test-py313

.PHONY: docker-test-py39
docker-test-py39: PYTHON_VERSION := 3.9
docker-test-py39: --docker-test

.PHONY: docker-test-py310
docker-test-py310: PYTHON_VERSION := 3.10
docker-test-py310: --docker-test

.PHONY: docker-test-py311
docker-test-py311: PYTHON_VERSION := 3.11
docker-test-py311: --docker-test

.PHONY: docker-test-py312
docker-test-py312: PYTHON_VERSION := 3.12
docker-test-py312: --docker-test

.PHONY: docker-test-py313
docker-test-py313: PYTHON_VERSION := 3.13
docker-test-py313: --docker-test

# Private target for docker-tests
.PHONY: --docker-test
--docker-test:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install uv && uv run --group dev python -m unittest discover ./tests/'
