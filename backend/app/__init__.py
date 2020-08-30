import os

import typing
import flask


def create_app(test_config=None) -> flask.Flask:
    """
    This creates and configures the python flask app, test_config is passed in
    to override the configuration parameters during testing.
    """

    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'kanak_api.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index() -> typing.Dict:
        return {
            "status": True
        }

    @app.route('/hello')
    def hello() -> typing.Dict:
        return {
            "status": True,
            "data": "Hello, World",
        }

    return app
