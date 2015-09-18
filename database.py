# Database access functions for the web forum.
 
import time
import psycopg2

def GetAllPosts():
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()

  c.execute("SELECT time, content FROM posts ORDER BY time DESC")

  posts = ({'content': str(row[1]), 
    'time': str(row[0])}
      for row in c.fetchall())
  DB.close()

  return posts

def AddPost(content):
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()

  # doing string substitution with a pyton tuple to avoid SQL injections
  c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
  DB.commit()
  DB.close()
