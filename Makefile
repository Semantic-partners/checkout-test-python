BIN=.venv/bin

remove-env:
	rm -fr env/

clean-build:
	rm -fr target/
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.so' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean: remove-env clean-build clean-pyc clean-test

virtualenv: clean
	python3 -m venv .venv

update_pip:
	$(BIN)/pip install --upgrade pip

pip_install:
	$(BIN)/pip install -r requirements.txt

test:
	$(BIN)/pytest tests

build_new: clean virtualenv update_pip pip_install test

run_pre_commit:
	$(BIN)/pre-commit run --all-file
