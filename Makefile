SRC=./aspose_barcode_cloud

ifneq ($(wildcard .venv),)
PYTHON = .venv/bin/python
else
PYTHON = python
endif

.PHONY: all
all: format lint test-tox

.PHONY: check_git
check_git:
	git fetch origin
	git diff origin/main --exit-code

.PHONY: dist
dist:
	$(PYTHON) setup.py sdist bdist_wheel --universal

.PHONY: format
format:
	$(PYTHON) -m black --line-length=120 -v $(SRC) tests/ scripts/ snippets/ *.py

.PHONY: format_doc
format_doc:
	# Trim white space
	sed -i -e 's_[[:space:]]*$$__' README.md
	# Trim trailing empty line
	sed -i -e '$${/^$$/d;}' README.md
	# Replace true->True false->False: sed -e "s/\b\(false\|true\)/\u\1/g"
	find . -type f -iname '*.md' -exec sed -i -e 's_\b\(false\|true\)_\u\1_g' '{}' \;

.PHONY: init
init:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt -r lint-requirements.txt -r test-requirements.txt

.PHONY: venv
venv:
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt -r lint-requirements.txt -r test-requirements.txt

.PHONY: init-docker
init-docker:
	$(PYTHON) -m pip install -r publish-requirements.txt -r requirements.txt

.PHONY: lint
lint:
	# stop the build if there are Python syntax errors or undefined names
	$(PYTHON) -m flake8 aspose_barcode_cloud --count --select=E9,F63,F7,F82 --show-source --statistics --extend-exclude '.*'
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	$(PYTHON) -m flake8 aspose_barcode_cloud --count --exit-zero --max-line-length=127 --statistics --extend-ignore=E501 --extend-exclude '.*'

.PHONY: publish
publish: check_git test-tox dist
	$(PYTHON) -m twine upload dist/*

.PHONY: publish-docker
publish-docker: init-docker unittest dist
	$(PYTHON) -m twine upload dist/* --verbose

.PHONY: test
test: cover
	./scripts/run_snippets.sh

# pytest-cov enforces the 80% line gate (.coveragerc); the shared scripts/coverage.py
# prints the percentage, applies COVERAGE_THRESHOLD (default 80) and writes
# coverage/coverage-{badge,summary}.json. The HTML report is in coverage/html.
.PHONY: cover
cover:
	$(PYTHON) -m pytest --cov=aspose_barcode_cloud --cov-report=term --cov-report=xml:coverage/coverage.xml --cov-report=html:coverage/html tests/
	$(PYTHON) scripts/coverage.py cobertura coverage/coverage.xml

.PHONY: unittest
unittest:
	$(PYTHON) -Werror -m unittest discover -v

.PHONY: test-example
test-example:
	$(PYTHON) -Werror example.py

.PHONY: test-tox
test-tox:
	$(PYTHON) -m tox $(SRC)

.PHONY: insert-examples
insert-examples:
	./scripts/insert-example.bash

.PHONY: add-warnings
add-warnings:
	./scripts/add-deprecation-warnings.bash

.PHONY: after-gen
after-gen: format insert-examples add-warnings format_doc

.PHONY: update
update:
	echo "Not implemented"
