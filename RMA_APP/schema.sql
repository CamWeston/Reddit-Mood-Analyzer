CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS search (
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
);
