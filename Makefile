PYTHON_VERSION := $(shell python --version | grep -Eo '[2-3].[0-9]+')

.PHONY: docs
docs:
	@python -m pip install Sphinx
	@sphinx-build -b html docs/source/ docs/build/html/

.PHONY: install
install:
	@python -m pip install -U .

.PHONY: install-dev
install-dev:
	@python -m pip install -U -e .

.PHONY: test
test: test-lint
	@echo "Testing Python:$(PYTHON_VERSION)"
	@coverage run -m unittest discover tests/

.PHONY: test-coverage
test-coverage: test
	@coverage html

.PHONY: test-init
test-init:
	@python -m pip install -U -r requirements.txt

.PHONY: test-lint
test-lint: test-init
	@echo "Running Flake8"
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude docs
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude docs

.PHONY: docker-test-all
docker-test-all: docker-test-py37 docker-test-py38 docker-test-py39 docker-test-py310 docker-test-py311

.PHONY: docker-test-latest
docker-test-latest: docker-test-py311

.PHONY: docker-test-py37
docker-test-py37: PYTHON_VERSION := 3.7
docker-test-py37:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

.PHONY: docker-test-py38
docker-test-py38: PYTHON_VERSION := 3.8
docker-test-py38:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

.PHONY: docker-test-py39
docker-test-py39: PYTHON_VERSION := 3.9
docker-test-py39:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

.PHONY: docker-test-py310
docker-test-py310: PYTHON_VERSION := 3.10
docker-test-py310:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

.PHONY: docker-test-py311
docker-test-py311: PYTHON_VERSION := 3.11
docker-test-py311:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'