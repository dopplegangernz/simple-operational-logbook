#### Simple Operational Logbook

This is based off the most excellent Flask-RestX-Boilerplate

### Terminal commands

Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.

    > python3 manage.py db init

    > python3 manage.py db migrate --message 'initial database migration'

    > python3 manage.py db upgrade

or run:

    make db-init

Bear in mind that this will drop any existing database, so use with extreme caution.

### Viewing the app

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/

### Using Postman

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.

### Full description and guide for the underlying flash-restx

https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563

### Contributing
