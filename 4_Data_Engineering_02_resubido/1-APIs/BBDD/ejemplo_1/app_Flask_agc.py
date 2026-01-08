from flask import Flask, jsonify, request
from datos_dummy import books

# Objeto para ir añadiendo los endpoints
app = Flask(__name__)
# Linea que se pone cuando se esta probando
# Permite probar sin tener que cargar toda la API
# En desarollo es adecuado, en producción no es tan recomendable
# Si no se mete esta línea, hay que apagar la API con CTRL+c 
app.config["DEBUG"] = True


# Endpoint inicial 
# Ruta de accesso de la request
# Con esta plantilla puedo crear los endpoints que quiera
# Dentro de esta funcion se puede crear otras alojadas en otro archivo para no tener aqui llamadas a BB.DD, por ejemplo
@app.route('/', methods=['GET'])
def home():
    return "<h1>Mi primera API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return books

# Ejemplo de request de una suma
# Manera de pasar argumentos en la url de request: http://127.0.0.1:5000/suma?num1=3&num2=5
@app.route('/suma', methods=['GET'])
def sumar():
    num1 = request.args["num1"]
    num2 = request.args["num2"]

    resultado = str(num1 + num2)
    return resultado
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
# El parametro se le pasa en la url
# http://127.0.0.1:5000/v0/book_id?id=0
@app.route('/v0/book_id', methods=['GET'])
def book_id():
    id = int(request.args['id'])
    for book in books:
        if book ["id"] == id:
            return book
    #results = [book for book in books if book["id"]==id]
    #return results

# Lo mismo que lo anterior pero la consulta se hace asi:
# http://127.0.0.1:5000/v0/book_id/0
@app.route('/v0/book_id/<int:id>', methods=['GET'])
def book_id2(id):
    for book in books:
        if book ["id"] == id:
            return book
    #results = [book for book in books if book["id"]==id]
    #return results


# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
@app.route('/v0/book/<string:title>', methods=["GET"])
def book_title(title):
    results = [book for book in books if book["title"].lower()==title.lower()]
    return results


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
@app.route('/v1/book', methods=["GET"])
def book_title_body():
    title = request.get_json().get('title', None)
    if not title:
        return "Not a valid title in the request", 400
    else:
        results = [book for book in books if book["title"].lower()==title.lower()]
        if results == []:
            return "Book not found", 400
        else:
            return results

# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/v1/add_book', methods=["POST"])
def post_books():
    data = request.get_json()
    books.append(data)
    return books


# 6.Ruta para añadir un libro mediante parámetros
# http://127.0.0.1:5000/v2/add_book?id=3&author=Tolkien&title=El seño de los anillos&first_sentence=La comarca&published=1950
@app.route('/v2/add_book', methods=["POST"])
def post_books_v2():
    book = {}
    book['id'] = int(request.args['id'])
    book['title'] = request.args['title']
    book['author'] = request.args['author']
    book['first_sentence'] = request.args['first_sentence']
    book['published'] = request.args['published']
    books.append(book)
    return books

# 7.Ruta para modificar un libro
@app.route("/v3/books", methods=["PUT"])
def put_book():
    id = int(request.args['id'])

    title = request.args.get('title', None)
    author = request.args.get('author', None)

    for book in books:
        if book["id"] == id:
            if title:
                book['title'] = title
            if author:
                book['author'] = author
    return books

# 8.Ruta para eliminar un libro
@app.route("/v4/books", methods=["DELETE"])
def del_book():
    id = int(request.args['id'])
    # id = int(id)
    for book in books:
        if book["id"] == id:
            books.remove(book)
    return books

# Esencial para correr la API
app.run()