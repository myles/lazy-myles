.PHONY: all
all: clean setup test lint mypy bandit build

.PHONY: setup
setup: pyproject.toml
	poetry install

.PHONY: test
test:
	poetry run pytest --cov=lazymyles/ --cov-report=xml

.PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run ruff check .

.PHONY: mypy
mypy:
	poetry run mypy lazymyles/

.PHONY: bandit
bandit:
	poetry run bandit --recursive --quiet lazymyles/

.PHONY: clean
clean:
	rm -fr ./.mypy_cache
	rm -fr ./.pytest_cache
	rm -fr ./.ruff_cache
	rm -fr ./dist
	rm .coverage
	rm coverage.xml
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: build
build:
	poetry build

.PHONY: bulid_docs
build_docs:
	poetry run sphinx-build ./docs ./docs/_build
