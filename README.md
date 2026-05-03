## Name : D DEVIKA

## REG NO : 212224100010

## Title

Car Price Prediction using Machine Learning

## About

This project predicts the price of a car based on its manufacturing year using Linear Regression. It demonstrates how data analytics can be used to understand trends and make predictions.

## Algorithm

Start

Import required libraries

Define input data (car manufacturing year)

Define output data (price)

Create Linear Regression model

Train the model

Predict price for new year

Display result

Stop

## Code

import numpy as np
from sklearn.linear_model import LinearRegression

year = np.array([2010, 2012, 2015, 2018, 2020]).reshape(-1, 1)
price = np.array([200000, 250000, 300000, 400000, 500000])

model = LinearRegression()
model.fit(year, price)

predicted_price = model.predict([[2022]])

print("Predicted Car Price:", predicted_price)

## Screenshot

<img width="1920" height="1200" alt="Screenshot (200)" src="https://github.com/user-attachments/assets/dd085826-d00e-4aff-90fe-9d50a8e8a29d" />


## Conclusion

This project demonstrates how Machine Learning can be used to predict car prices based on year. It shows the importance of data in making future predictions.
