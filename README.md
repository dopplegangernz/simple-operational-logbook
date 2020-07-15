#### FLASK RESTX BOILER-PLATE WITH JWT

“FLASK RESTX BOILER-PLATE is being sponsored by the following tool; please help to support us by taking a look and signing up to a free trial”
<!--
<a href="https://tracking.gitads.io/?repo=YOUR_REPO">
 <img src="https://images.gitads.io/YOUR_REPO" alt="GitAds"/> </a>
-->

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

    Note: make sure to run the initial migration commands to update the database.
    ```
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade
    ```

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.

### Full description and guide ###
https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563


### Contributing
If you want to contribute to this flask restplus boilerplate, clone the repository and just start making pull requests.

```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git
```
