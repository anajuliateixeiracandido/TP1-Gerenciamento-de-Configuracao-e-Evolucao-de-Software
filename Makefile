.PHONY: install build clean run validate help

help:
	@echo "Available build commands:"
	@echo "  install      - Install build dependencies"
	@echo "  validate     - Validate Python syntax"
	@echo "  build        - Build package"
	@echo "  clean        - Clean build artifacts"
	@echo "  run          - Run the application"

install:
	pip install --upgrade pip
	pip install -r requirements.txt

validate:
	@echo "Validating Python syntax..."
	python3 -m py_compile *.py
	@echo "Syntax validation completed"

build:
	@echo "Building package..."
	python3 -m build
	@echo "Package build completed"
	@echo "Generated artifacts:"
	@ls -la dist/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Build artifacts cleaned"

run:
	@echo "Running application..."
	python3 main.py