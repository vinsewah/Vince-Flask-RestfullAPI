from app.db import get_db
from sqlite3 import Error

db = get_db()

def get_top_movies_by_runtime(take=1):
    try:
        cur = db.cursor()
        cur.execute('SELECT * from movies order by runtime desc limit ?', (take,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)


def get_top_movies_by_actors(take=1):
    try:
        cur = db.cursor()
        cur.execute(
            '''
            select m.id, m.title, count(*) from actors a join movies m on a.movie_id = m.id group by movie_id order by count(*) desc limit ?
            ''',
            (take,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)


def get_all_movies(take=10):
    try:
        cur = db.cursor()
        cur.execute('''select * from movies limit ?''', (take,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
