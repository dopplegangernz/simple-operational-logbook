from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.exc import OperationalError
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
from flask_migrate import Migrate


from .config import config_by_name


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__, static_folder=os.path.join(
        os.path.dirname(__file__), '../../client/dist/'), static_url_path='')
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    flask_bcrypt.init_app(app)

    try:
        ensureDBHasGroups(app, db)
        ensureDBHasUsers(app, db)
    except OperationalError:
        pass

    return app


def ensureDBHasUsers(app, db):
    """Checks whether the DB has users. If there are none, create a default admin user.

    Args:
        app (Flask app instance): the app instance
        db (SQLAlchemy ORM instance): the DB object for the app
    """
    from .model.user import User
    from .model.group import Group
    import datetime
    import uuid

    app.logger.info("Checking users present")

    with app.app_context():
        userCount = db.session.query(User).add_columns(User.username).count()

    if userCount < 1:
        # add default admin user

        with app.app_context():
            groupId = db.session.query(Group).add_columns(Group.id).first().id

        default_admin_user = User(
            public_id=str(uuid.uuid4()),
            email="admin",
            username="admin",
            password="admin",
            admin=True,
            group_id=groupId,
            registered_on=datetime.datetime.utcnow()
        )
        app.logger.info("Adding default user")
        with app.app_context():
            db.session.add(default_admin_user)
            db.session.commit()


def ensureDBHasGroups(app, db):
    """Checks whether the DB has groups. If there are none, create a default group.

    Args:
        app (Flask app instance): the app instance
        db (SQLAlchemy ORM instance): the DB object for the app
    """
    from .model.group import Group
    import uuid

    app.logger.info("Checking groups present")

    with app.app_context():
        groupCount = db.session.query(Group).add_columns(Group.name).count()

    if groupCount < 1:
        # add default admin user
        new_group = Group(
            public_id=str(uuid.uuid4()),
            name='default group',
            description='A default group'
        )
        app.logger.info("Adding default group")
        with app.app_context():
            db.session.add(new_group)
            db.session.commit()
