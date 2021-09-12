.ONESHELL:

.PHONY: clean install tests run all

UNAME_S := $(shell uname -s)

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	python3 -m venv venv; \
	. venv/bin/activate; \

	ifeq ($(UNAME_S), Linux)
		pip3 install cffi
	endif
	
	pip3 install -r requirements.txt; \
	. cd client; \
	npm install; \
	npm run build;

tests:
	. venv/bin/activate; \
	python3 manage.py test

run:
	. venv/bin/activate; \
	python3 manage.py run

all: clean install tests run

db-init:
	. rm -rf migrations; \
	python3 manage.py db init; \
	python3 manage.py db migrate --message 'initial database migration'; \
	python3 manage.py db upgrade;
