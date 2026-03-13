import psycopg2
import psycopg2.extras

def connect():
  conn = psycopg2.connect(
  host = 'localhost',
  dbname = 'master',
  user="postgres",
  password= 'abc',
  cursor_factory = psycopg2.extras.NamedTupleCursor
  )
  conn.autocommit = True
  return conn


connect()