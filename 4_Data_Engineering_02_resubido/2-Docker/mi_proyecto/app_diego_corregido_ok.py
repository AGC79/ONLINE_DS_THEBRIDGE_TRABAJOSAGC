from flask import Flask, jsonify, request
import sqlite3
import pickle
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

with open("data/modelo_advertising.pkl", "rb") as m:
    modelo = pickle.load(m)

@app.route("/")
def main():
    return "Api ventas"

# 1. Ofrezca la predicción de ventas a partir de todos los valores de gastos en publicidad. (/predict)
@app.route("/predict", methods = ["GET"])
def predict():
    """{'data': [[100, 100, 200]]}"""

    data = request.get_json()

    data_value = data.get("data", None)
    if not data_value:
        return {"error": "Datos no validos"}, 400
    try:
        pred = modelo.predict(data["data"])
        return {"prediction":pred[0]}, 200
    except Exception as e:
        return {"error":e}, 500
# 2. Un endpoint para almacenar nuevos registros en la base de datos que deberás crear previamente.(/ingest)
@app.route("/ingest", methods = ["POST"])
def ingest():
    """{'data': [[100, 100, 200, 3000], [200, 230, 500, 4000]]}"""
    data = request.get_json()
    data_value = data.get("data", None)
    if not data_value:
        return {"error": "Datos no validos"}, 400
    try:
        con = sqlite3.connect("data/advertising.db")
        cursor = con.cursor()
        query = "INSERT INTO campañas VALUES(?,?,?,?)"
        cursor.executemany(query, data["data"])
        con.commit()
        con.close()
        return {'message': 'Datos ingresados correctamente'}, 200
    except Exception as e:
        return {"error":e}, 500
# 3. Posibilidad de reentrenar de nuevo el modelo con los posibles nuevos registros que se recojan. (/retrain)
@app.route("/retrain", methods = ["POST"])
def retrain():
    try:
        con = sqlite3.connect("data/advertising.db")
        cursor = con.cursor()
        query = "SELECT * FROM campañas"
        resultado = cursor.execute(query).fetchall()
        con.close()
        df = pd.DataFrame(resultado)
        modelo.fit(df.iloc[:, :-1], df.iloc[:, -1])
        with open("data/modelo_advertising.pkl", "wb") as m:
            pickle.dump(modelo, m)
        return {'message': 'Modelo reentrenado correctamente.'}, 200
    except Exception as e:
        return {"error":e}, 500

app.run()