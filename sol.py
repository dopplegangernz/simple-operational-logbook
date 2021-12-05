import os
import unittest

from flask_migrate import Migrate
from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

from flask.cli import FlaskGroup

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate()
migrate.init_app(app, db)

cli = FlaskGroup(app)


# @cli.command('run')
# def run():
#     app.logger.info("Running sol.py")
#     os._exit(1)
#     app.run(host='0.0.0.0')
#     app.logger.info("Running sol.py")


@cli.command('test')
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
