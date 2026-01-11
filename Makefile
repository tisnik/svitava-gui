PATH_TO_PLANTUML := ~/bin


run: ## Run the service locally
	python -B src/svitava-gui.py


test-unit: ## Run the unit tests
	@echo "Running unit tests..."
	@echo "Reports will be written to ${ARTIFACT_DIR}"
	COVERAGE_FILE="${ARTIFACT_DIR}/.coverage.unit" uv run python -m pytest tests/unit --cov=src --cov-report term-missing --cov-report "json:${ARTIFACT_DIR}/coverage_unit.json" --junit-xml="${ARTIFACT_DIR}/junit_unit.xml" --cov-fail-under=60


check-types: ## Checks type hints in sources
	mypy --explicit-package-bases --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs --ignore-missing-imports --disable-error-code attr-defined src/


security-check: ## Check the project for security issues
	bandit -c pyproject.toml -r src tests


format: ## Format the code into unified format
	uv run black .
	uv run ruff check . --fix


black:	## Check source code using Black code formatter
	uv run black --check .


pylint:	## Check source code using Pylint static code analyser
	uv run pylint src tests


pyright:	## Check source code using Pyright static type checker
	uv run pyright src


docstyle:	## Check the docstring style using Docstyle checker
	uv run pydocstyle -v src


ruff:	## Check source code using Ruff linter
	uv run ruff check . --per-file-ignores=tests/*:S101 --per-file-ignores=scripts/*:S101


verify:	## Run all linters
	$(MAKE) black
	$(MAKE) pylint
	$(MAKE) pyright
	$(MAKE) ruff
	$(MAKE) docstyle
	$(MAKE) check-types


help: ## Show this help screen
	@echo 'Usage: make <OPTIONS> ... <TARGETS>'
	@echo ''
	@echo 'Available targets are:'
	@echo ''
	@grep -E '^[ a-zA-Z0-9_./-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-33s\033[0m %s\n", $$1, $$2}'
	@echo ''
