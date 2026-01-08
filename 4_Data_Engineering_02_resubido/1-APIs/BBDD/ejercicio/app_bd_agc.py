# IMPORT
import pandas as pd
import sqlite3
from flask import Flask, jsonify, request

connection = sqlite3.connect("books.db") 
crsr = connection.cursor()
tabla = 'books'

crsr.execute("""
    CREATE TABLE books_temp (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title TEXT,
        author TEXT,
        published INTEGER,
        first_sentence TEXT
    )
""")

crsr.execute(f"""
    INSERT INTO books_temp (title, author, published, first_sentence) 
    SELECT DISTINCT title, author, published, first_sentence 
    FROM {tabla}
""")

crsr.execute(f"DROP TABLE {tabla}")
crsr.execute(f"ALTER TABLE books_temp RENAME TO {tabla}")

connection.commit()
connection.close()

app = Flask(__name__)
app.config["DEBUG"] = True

# Ruta inicial
@app.route('/', methods=['GET'])
def home():
    return "<h1>API Biblioteca AGC</h1><p>Ejercicio de creación de APIs a partir de BB.DD SQL</p>"


# 0.Ruta para obtener todos los libros
@app.route("/libros", methods = ["GET"])
def libros():
    connection = sqlite3.connect("books.db") 
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM {tabla}")
    libros = crsr.fetchall()
    crsr.close()
    connection.close()
    return jsonify(libros)

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route("/total_libros_autor", methods = ["GET"])
def libros_autores_count():
    connection = sqlite3.connect("books.db") 
    crsr = connection.cursor()
    crsr.execute(f"SELECT author, COUNT(id) as total FROM {tabla} GROUP BY author ORDER BY total DESC")
    total_libros_autor = crsr.fetchall()
    crsr.close()
    connection.close()
    return jsonify(total_libros_autor)

# 2.Ruta para obtener los libros de un autor
@app.route("/libros_autor/<string:nombre_autor>", methods = ["GET"])
def libros_autor(nombre_autor):
    connection = sqlite3.connect("books.db") 
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM {tabla} WHERE author=?", (nombre_autor,))
    libros_autor = crsr.fetchall()
    crsr.close()
    connection.close()
    return jsonify(libros_autor)

# 3.Ruta para añadir un libro
# http://127.0.0.1:5000/libro_nuevo/Libro de Alvaro/Alvaro Guerra Cabello/2025/Este es el libro que he insertado
@app.route("/libro_nuevo/<string:title>/<string:author>/<int:published>/<string:first_sentence>", methods=["POST"])
def nuevo_libro_ruta(title, author, published, first_sentence):
    connection = sqlite3.connect("books.db")
    crsr = connection.cursor()

    query = """
        INSERT INTO books (title, author, published, first_sentence) 
        VALUES (?, ?, ?, ?)
    """
    
    crsr.execute(query, (title, author, published, first_sentence))
    connection.commit()
    connection.close()

    return jsonify({"mensaje": f"Libro '{title}' añadido con éxito"}), 201

app.run()
