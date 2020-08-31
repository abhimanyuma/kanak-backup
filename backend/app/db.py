import sqlite3

import click
import flask
import flask.cli as flask_cli


def get_db() -> sqlite3.Connection:
    """
    This returns the flask application's database connection object. If there is
    no db connection object defined, then a new one is created from the config.
    """
    if 'db' not in flask.g:
        flask.g.db = sqlite3.connect(
            flask.current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        flask.g.db.row_factory = sqlite3.Row

    return flask.g.db


def close_db(_e=None) -> None:
    """
    If a db connection object exists for the flask application, it is closed
    """
    db = flask.g.pop('db', None)

    if db is not None:
        db.close()


def init_db() -> None:
    """
    This initialises the database, it executes the schema.sql script on the
    database, which in turn drops all the tables and creates new empty ones
    """
    db = get_db()

    with flask.current_app.open_resource('schema.sql') as schema_file:
        db.executescript(schema_file.read().decode('utf8'))


@click.command('init-db')
@flask_cli.with_appcontext
def init_db_command() -> None:
    """
    Call the init db method which deletes and recreates all the tables.
    """
    init_db()
    click.echo('Initialized the database')


def init_app(app: flask.Flask) -> None:
    """
    This links the db commands with the flask application
    """
    # Ensure we execute close_db during app teardown
    app.teardown_appcontext(close_db)
    # Add init_db_command as a flask cli command
    app.cli.add_command(init_db_command)
