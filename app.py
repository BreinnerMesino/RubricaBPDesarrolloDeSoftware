from flask import Flask, render_template
#Código para correr el servidor con el index de html.
app  = Flask(__name__)

headings = ("Nombre", "Apellido", "Edad")
data = (
    ("d1", "d2", "d3"),
    ("d1", "d2", "d3"),
    ("d1", "d2", "d3"),
)
@app.route('/')
def index():
    return render_template('index.html', headings=headings, data=data)
if __name__=='__main__':
    app.run()
    pass