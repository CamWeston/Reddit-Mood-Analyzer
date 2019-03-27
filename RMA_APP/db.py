
# TODO: We need to change the database connection badly. Right now we are just creating an instance DB
#       that is being overwritten. Someone needs to find a way to just connect to a db that is in the
#       directory while keeping the strict open close policy that is in place right now - Cam

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# Get database instance from python local db var g
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# close the db instance
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
# open the db instance
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# click command for flask init-db
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
