from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["GET"])
def home():
    return "Mi primera API"

@app.route("/libros", methods = ["GET"])
def libros():
    return books
# Primer metodo parametros.
@app.route("/libros_id", methods = ["GET"])
def libros_id():
    id = int(request.args["id"])
    for book in books:
        if book["id"] == id:
            return book
# Segundo metodo parametros.
@app.route("/libros_titulo/<int:id>", methods = ["GET"])
def libros_titulo(id, titulo):

    for book in books:
        if (book["id"] == id) and (book["title" == titulo]):
            return book

@app.route("/libro_nuevo", methods = ["POST"])
def nuevo_libro():
    book = {}
    book["id"] = int(request.args["id"])
    book["author"] = request.args["autor"]
    book["title"] = request.args["titulo"]
    book["published"] = request.args["anio"]
    book["first_sentence"] = request.args["frase"]

    books.append(book)
    return books

# Terce metodo parametros.

@app.route("/libro_nuevo_2", methods = ["POST"])
def nuevo_libro_2():
    """
    {
        "id": 3,
        "author": Orwell,
        "title": 1984,
        "first_sentence": El gran hermano,
        "published": 1950
    }
    """
    data = request.get_json()
    books.append(data)

    return books

@app.route("/eliminar_libro", methods = ["DELETE"])
def eliminar():
    id = int(request.args["id"])
    for book in books:
        if book["id"] == id:
            books.remove(book)

    return books
app.run()