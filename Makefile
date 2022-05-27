.PHONY: docs install test test-coverage test-init

docs:
	@python -m pip install Sphinx
	@sphinx-build -b html docs/source/ docs/build/html/ && open docs/build/html/index.html

install:
	@python -m pip install -U -e .

test: test-init
	@coverage run -m unittest discover tests/

test-coverage: test
	@coverage html && open htmlcov/index.html

test-init:
	@python -m pip install -U -r requirements.txt