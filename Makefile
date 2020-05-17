SHELL := /bin/bash

# Create the requirements.txt file.
freeze:
	pip freeze > requirements.txt

flask:
	FLASK_APP_CONFIG=settings.cfg
	FLASK_ENV=development
	FLASK_APP=project
	./venv/bin/flask run