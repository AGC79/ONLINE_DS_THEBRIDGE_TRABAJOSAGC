import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import sqlite3
from flask import Flask, jsonify, request
import pickle 

modelo_pred = pickle.load(open("data/modelo_advertising.pkl", "rb"))

def bbdd(query, params=()):
    conn = sqlite3.connect("data/advertising.db")
    cursor = conn.cursor()
    resultado = cursor.execute(query, params).fetchall()
    conn.commit() 
    conn.close()
    return resultado

app = Flask(__name__)
app.config["DEBUG"] = True

# Endpoint inicial
@app.route('/', methods=['GET'])
def main():
    return "API de predicciones"

# Obtener todos los datos de la BB.DD
@app.route('/datos', methods=['GET'])
def datos():
    res = bbdd("SELECT * FROM campañas")
    return jsonify(res)

# 1. Ofrezca la predicción de ventas a partir de todos los valores de gastos en publicidad. (/predict)
# consulta ejemplo: 
"""
{
  "data": [[100.5, 20.0, 50.0]]
}
"""
@app.route('/predict', methods=['GET']) 
def predict():
    datos_recibidos = request.get_json(force=True, silent=True)
    
    if datos_recibidos is None or 'data' not in datos_recibidos:
        return jsonify({'error': 'Faltan datos'}), 400

    input_data = datos_recibidos.get('data')
    
    try:
        prediction = modelo_pred.predict(input_data)
        return jsonify({'prediction': round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 2. Un endpoint para almacenar nuevos registros en la base de datos que deberás crear previamente.(/ingest)
# Los argumentos se pasan como un objeto json. Ejemplo:
"""
{
  "data": [
    [100, 100, 200, 3000],
    [200, 230, 500, 4000]
  ]
}
"""
@app.route('/ingest', methods=['POST']) 
def ingest():
    datos_recibidos = request.get_json()
    
    if not datos_recibidos or 'data' not in datos_recibidos:
        return jsonify({"error": "Formato incorrecto"}), 400

    registros = datos_recibidos.get('data')

    query = "INSERT INTO campañas (tv, radio, newspaper, sales) VALUES (?, ?, ?, ?)"
    
    for fila in registros:
        bbdd(query, (fila[0], fila[1], fila[2], fila[3]))

    return jsonify({'message': 'Datos ingresados correctamente'})


# 3. Posibilidad de reentrenar de nuevo el modelo con los posibles nuevos registros que se recojan. (/retrain)
@app.route('/retrain', methods=['POST']) 
def retrain():
    try:
        connection = sqlite3.connect('data/advertising.db') 
        df_bbdd = pd.read_sql("SELECT * FROM campañas", connection)
        connection.close()
  
        df_bbdd.columns = ['tv', 'radio', 'newspaper', 'sales']
        X = df_bbdd[['tv', 'radio', 'newspaper']]
        y = df_bbdd['sales']

        global modelo_pred

        try:
            modelo_pred.fit(X, y)
        except:
            modelo_pred = LinearRegression()
            modelo_pred.fit(X, y)

        with open('data/modelo_advertising.pkl', 'wb') as f:
            pickle.dump(modelo_pred, f)

        return jsonify({'message': 'Modelo reentrenado correctamente.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
