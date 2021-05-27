import pyodbc

"""
In a real production setting, this will not allow multiple
simultaneous users. For such a setting, you will not use
Json, but rather will use a real database layer like
https://flask-sqlalchemy.palletsprojects.com
"""
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, '
                      r'*.accdb)};DBQ=C:\Users\Niveda\Desktop\flaskTrial1\flashcards_db.accdb;')
cursor = conn.cursor()


def load_db():
    cursor.execute('select * from flashcards order by flashcardID')
    return cursor.fetchall()


def insert_into_db(question, answer):
    query = 'INSERT INTO flashcards (question, answer) VALUES(\'' + question + '\',\'' + answer + '\')'
    cursor.execute(query)
    conn.commit()


def delete_row_db(index):
    db = load_db()
    cursor.execute('DELETE FROM flashcards WHERE flashcardID=' + str(db[index].flashcardID))
    conn.commit()
