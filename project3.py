import numpy as np
from sklearn.linear_model import LinearRegression

year = np.array([2010, 2012, 2015, 2018, 2020]).reshape(-1, 1)
price = np.array([200000, 250000, 300000, 400000, 500000])

model = LinearRegression()
model.fit(year, price)

predicted_price = model.predict([[2022]])

print("Predicted Car Price:", predicted_price)
