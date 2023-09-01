import sys
import pyodbc
#Conección a la base de datos usando python y access. 
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\brein\Documents\Codes\Base de datos examen\src\TallerBD.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Estudiantes")
#Presentando la información de la base de datos
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT * FROM Cursos")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close