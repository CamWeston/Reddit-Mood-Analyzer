import sqlite3

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

def main():

    database = "Reddit-Mood-Analyzer.db"

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
                        anger boolean,
                        fear boolean,
                        joy boolean,
                        sadness boolean,
                        analytical boolean,
                        condifent boolean,
                        tentative boolean,
                        FOREIGN KEY (id) REFERENCES user (id)
                      ); """
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, user_table)
        # create tasks table
        create_table(conn, search_table)
    else:
        print("Error! cannot create the database connection.")

#==================================
if __name__ == '__main__':
    main()
