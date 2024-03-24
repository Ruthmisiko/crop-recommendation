import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("/home/ruth/CLIMATE CHANGE/climatedata.csv")
df

# filter only PRECIPITATION data drop PARAMETER, and ANN cols
data = df[df['PARAMETER'] == 'PRECTOTCORR'].drop(columns=['PARAMETER', 'ANN']).reset_index(drop=True)
data.shape

data.head(10)

# Add index col, will help with where to base the future predictions
data['index'] = [i for i in range(0, data.shape[0])]

# Training a linear regression model
X = data[['index', 'YEAR']]
y = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']]

# Split the dataset into training and testing (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a model object
model = LinearRegression()

# Fit the model to the data (training)
model.fit(X_train, y_train)

# Save model to pickle file 

filename = 'weather_model.pickle'
pickle.dump(model, open(filename, 'wb'))


