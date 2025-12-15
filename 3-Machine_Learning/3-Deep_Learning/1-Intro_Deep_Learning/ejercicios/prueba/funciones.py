import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


def leer(path):
    df = pd.read_csv(path)
    return df

def x_y(df, target):
    X = df.drop(columns = [target])
    y = df [target]
    return X, y

def split_X_y(X, y, test_size, semilla):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=semilla)

    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)

    return X_train, X_test, y_train, y_test

def escalado(X_train, X_test, escalado = None):
    if escalado != None:  
        if escalado == "StandardScaler":
            sc = StandardScaler()
            sc.fit(X_train)
            X_train_sc = sc.transform(X_train)
            X_test_sc = sc.transform(X_test)
            return X_train_sc, X_test_sc
        elif escalado == "MinMaxScaler":
            mms = MinMaxScaler()
            mms.fit(X_train)
            X_train_mms = mms.transform(X_train)
            X_test_mms = mms.transform(X_test)
            return X_train_mms, X_test_mms
    else:
        return X_train, X_test
    
def graficos(dataframe):
    plt.figure(figsize=(8,8))
    sns.heatmap(dataframe.corr(), annot=True, cmap="coolwarm", vmin=-1)
    plt.title("Matriz de correlación")

    # plt.figure(figsize=(8,8))
    sns.pairplot(dataframe)
    plt.title("Pairplot")
    plt.show()





