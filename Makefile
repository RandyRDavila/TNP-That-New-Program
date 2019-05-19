install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements_dev.txt

install-all:
	pip install -r requirements.txt -r requirements_dev.txt

lint:
	flake8 tnp/

check-formatting:
	black --check tnp/

format:
	black tnp/
