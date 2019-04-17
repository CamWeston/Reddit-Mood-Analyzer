
# TODO: We need to change the database connection badly. Right now we are just creating an instance DB
#       that is being overwritten. Someone needs to find a way to just connect to a db that is in the
#       directory while keeping the strict open close policy that is in place right now - Cam

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# functions work for database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# initial a local database
DATABASE = 'Reddit-Mood-Analyzer.db'
user_table = """ CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    ); """

search_table = """ CREATE TABLE IF NOT EXISTS search (
    id INTEGER,
    username TEXT,
    date DATE,
    subreddit TEXT,
    anger TEXT,
    fear TEXT,
    joy TEXT,
    sadness TEXT,
    analytical TEXT,
    condifent TEXT,
    tentative TEXT,
    FOREIGN KEY (id) REFERENCES user (id)
    ); """

conn = create_connection(DATABASE)
if conn is not None:
    # create projects table
    create_table(conn, user_table)
    # create tasks table
    create_table(conn, search_table)
else:
    print("Error! cannot create the database connection.")

def get_db():
    db = getattr(g, '_database', None)
  #  if 'db' not in g:
  #      g.db = sqlite3.connect(
  #          current_app.config['DATABASE'],
  #          detect_types=sqlite3.PARSE_DECLTYPES
  #      )
    db = g._database = sqlite3.connect(
	     DATABASE,
             detect_types=sqlite3.PARSE_DECLTYPES
	)
    db.row_factory = sqlite3.Row

    return db

# close the db instance
def close_db(e=None):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()
# open the db instance
def init_db():
    db = get_db()

    # click command for flask init-db

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
