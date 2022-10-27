.PHONY: docker-test-all docker-test-latest docker-test-py37 docker-test-py38 docker-test-py39 docker-test-py310 docker-test-py311 docs install test test-coverage test-init test-lint

PYTHON_VERSION = "3.10"

docs:
	@python -m pip install Sphinx
	@sphinx-build -b html docs/source/ docs/build/html/

install:
	@python -m pip install -U -e .

test: test-lint
	@coverage run -m unittest discover tests/

test-coverage: test
	@coverage html

test-init:
	@python -m pip install -U -r requirements.txt

test-lint: test-init
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude docs
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude docs

docker-test-all: docker-test-py37 docker-test-py38 docker-test-py39 docker-test-latest

docker-test-latest: docker-test-py310

docker-test-py37: PYTHON_VERSION = "3.7"
docker-test-py37:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

docker-test-py38: PYTHON_VERSION = "3.8"
docker-test-py38:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

docker-test-py39: PYTHON_VERSION = "3.9"
docker-test-py39:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

docker-test-py310: PYTHON_VERSION = "3.10"
docker-test-py310:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'

docker-test-py311: PYTHON_VERSION = "3.11"
docker-test-py311:
	@echo "Testing Python:$(PYTHON_VERSION)"
	@docker run -it --rm -v "$(PWD)":/usr/src/app -w /usr/src/app python:$(PYTHON_VERSION)\
		sh -c 'python -m pip install -U -r ./requirements.txt && python -m unittest discover ./tests/'