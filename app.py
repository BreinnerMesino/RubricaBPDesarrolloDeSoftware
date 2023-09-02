from flask import Flask, render_template
import pyodbc

# Código para correr el servidor con el index de HTML.
app = Flask(__name__)
# Conectarse a la base de datos de Access
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\brein\Documents\Codes\Base de datos examen\src\TallerBD.accdb;")
#Se crea el cursor y se hace una consulta para pedir los datos
cursor = conn.cursor()
cursor.execute("SELECT * FROM Estudiantes") 
# Obtener y asignar a la variable data los datos de la consulta
data_Students = cursor.fetchall()
cursor.execute("SELECT * FROM Cursos") 
# Obtener y asignar a la variable data los datos de la consulta
data_Course = cursor.fetchall()
#Terminar conexión con la base de datos y el cursor.
cursor.close()
conn.close()
#Definir los titulos de cada columna de la lista
headings_Students = ("ID", "Nombre", "Apellido", "Edad")
headings_Course = ("ID", "Nombre_Curso", "ID_Estudiante")
@app.route('/')
def index():
    return render_template('index.html', headings=headings_Students, data=data_Students, data2=data_Course, headings2=headings_Course)

if __name__ == '__main__':
    app.run()