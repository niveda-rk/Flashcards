import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, '
                          r'*.accdb)};DBQ=C:\Users\Niveda\Desktop\flaskTrial1\flashcards_db.accdb;')
cursor = conn.cursor()
query = 'INSERT INTO flashcards (question, answer) VALUES(\'' + 'hey' + '\',\'' + 'hey' + '\')'
row = cursor.execute(query)
print(row.question)
conn.commit()
