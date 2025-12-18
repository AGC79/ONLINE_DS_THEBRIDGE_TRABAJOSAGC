import funciones as f
import variables as v

df = f.leer(v.path)
f.graficos(df)
X, y = f.x_y(df, v.target)
X_train, X_test, y_train, y_test = f.split_X_y(X, y, v.tamano_test, v.semilla)
X_train_s, X_test_s = f.escalado(X_train, X_test, v.escalado)
print(X_train_s)