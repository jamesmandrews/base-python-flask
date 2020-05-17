SHELL := /bin/bash

# Create the requirements.txt file.
requirements:
	pip freeze > requirements.txt

flask:
	FLASK_APP=project
	FLASK_ENV=development
	./venv/bin/flask run