.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete


installServer:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; 

installClient:
	. cd client; \
	npm install; \
	npm run build;

initdb:
	rm -rf migrations; \
	find . -type f -name '*.db' -delete; \
    flask db init; \
	flask db migrate --message 'initial database migration'; \
	flask db upgrade;

installServerDev:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt;

installServerDev: installServer initdb

tests:
	. venv/bin/activate; \
	python3 manage.py test

run:
	. venv/bin/activate; \
	flask run

all: clean install tests run

db-init:
	. rm -rf migrations; \
	python3 manage.py db init; \
	python3 manage.py db migrate --message 'initial database migration'; \
	python3 manage.py db upgrade;
