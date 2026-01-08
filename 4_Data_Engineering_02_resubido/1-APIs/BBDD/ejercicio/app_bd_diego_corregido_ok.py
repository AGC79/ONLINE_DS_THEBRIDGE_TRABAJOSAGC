# IMPORT
import sqlite3
from flask import Flask, jsonify, request

def bbdd(query):
    con = sqlite3.connect("books.db")
    cursor = con.cursor()
    query
    resultado = cursor.execute(query).fetchall()
    con.close()
    return resultado

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["GET"])
def main():
    return "Api libros con BBDD"
# 0.Ruta para obtener todos los libros
@app.route("/libros", methods = ["GET"])
def libros():
    res = bbdd("SELECT * FROM books")
    return jsonify(res)
# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route("/libros_autor", methods = ["GET"])
def libro_autor():
    res = bbdd("SELECT author, count(*) FROM books GROUP BY author ORDER BY 2 DESC")
    return jsonify(res)

# 2.Ruta para obtener los libros de un autor
@app.route("/buscar_libro", methods = ["GET"])
def buscar_libro():
    autor = request.args["autor"]
    query = f"SELECT * FROM books WHERE author = '{autor}'"
    res = bbdd(query)
    return jsonify(res)
# 3.Ruta para añadir un libro
@app.route("/insertar_libro", methods = ["POST"])
def insertar_libro():
    """
    {
    [
    2000,
    1954,
    "Tolkien",
    "El señor de los anillos",
    "El anillo unico"
    ]
    }
    """

    data = request.get_json()
    query =  f"INSERT INTO books(id, published, author, title, first_sentence) VALUES({data[0]},'{data[1]}','{data[2]}','{data[3]}','{data[4]}')"
    con = sqlite3.connect("books.db")
    cursor = con.cursor()
    resultado = cursor.execute(query).fetchall()
    con.commit()
    con.close()
    return "Libro guardado correctamente"


app.run()