import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/USA_Housing.csv')
print(df)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 11)

# Mostramos todos los shapes
print("Tamaño de todo el dataframe:", X.shape)
print("Train features shape:", X_train.shape)
print("Train target shape:", y_train.shape)
print("Test features shape:", X_test.shape)
print("Test target shape:", y_test.shape)

lm = LinearRegression()
lm.fit(X_train, y_train)

pred = lm.predict(X_test)

print("MAE: ", metrics.mean_absolute_error(y_test, pred))