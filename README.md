#### Simple Operational Logbook

This is based off the most excellent Flask-RestX-Boilerplate

**Note:** this is in active development approaching 1.0 - i'm trying not to leave it in a broken state day to day, but I'm working on this no my own, and AFAIK noone else is looking at it, so I'm not being super paranoid about good commit practices; fear not, this will change once it gets to a minimum viable version. And in the interim, if it's snapped, chuck in an issue and I'll aim to fix it ASAP 

### Terminal commands

Note: make sure you have `pip`, `virtualenv`, and `npm` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.

    > flask db init

    > flask db migrate --message 'initial database migration'

    > flask db upgrade

or run:

    make db-init

Bear in mind that this will drop any existing database, so use with extreme caution.

### Viewing the app

    Open the following url on your browser to view client
    http://127.0.0.1:5000/index.html

    Or the following to browse the API's swagger documentation
    http://127.0.0.1:5000/api

### Using Postman

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

### Full description and guide for the underlying flash-restx

https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563

### Contributing

docker run -p 5000:5000 -w /app -v "$(pwd):/app" python:3 sh -c "make installdev && make run"