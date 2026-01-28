import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import sqlite3
from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True

with open("data/modelo_advertising.pkl", "rb") as m:
    model = pickle.load(m)

# Endpoint inicial
@app.route('/', methods=['GET'])
def main():
    return "API ventas"

# 1. Ofrezca la predicción de ventas a partir de todos los valores de gastos en publicidad. (/predict)
@app.route("/predict", methods=["GET"])
def predict():
    """"{'data': [[100, 100, 200]]} """
    data = request.get_json()
    data_value = data.get("data", None)
    if not data_value:
        return {"error": "Datos no validos"}, 400
    try:
        prediction = model.predict(data["data"])
        return {"prediction":prediction[0]}, 200
    except Exception as e:
        return {"error":e}, 500

# 2. Un endpoint para almacenar nuevos registros en la base de datos que deberás crear previamente.(/ingest)
# {'data': [[100, 100, 200, 3000], [200, 230, 500, 4000]]}
@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.get_json()
    data_value = data.get("data", None)
    if not data_value:
        return {"error": "Datos no validos"}, 400
    
    try:
        con = sqlite3.connect("data/advertising.db")
        cursor = con.cursor()
        query = "INSERT INTO campañas VALUES(?, ?, ?, ?)"
        cursor.executemany(query, data["data"])
        con.commit()
        con.close()
        return {'message': 'Datos ingresados correctamente'}, 200
    except Exception as e:
        return {"error": e}, 500
    

# 3. Posibilidad de reentrenar de nuevo el modelo con los posibles nuevos registros que se recojan. (/retrain)
@app.route("/retrain", methods=["POST"])
def retrain():
    try:
        con = sqlite3.connect("data/advertising.db")
        cursor = con.cursor()
        query = "SELECT * FROM campañas"
        resultado = cursor.execute(query).fetchall()
        con.close()
        df = pd.DataFrame(resultado)
        model.fit(df.iloc[:, :-1], df.iloc[:, -1])
        with open("data/modelo_advertising.pkl", "rb") as m:
            model = pickle.dump(model, m)
            return {'message': 'Modelo reentrenado correctamente.'}, 200

    except Exception as e:
        return {"error": e}, 500

app.run()
