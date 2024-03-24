import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import datetime

# WEATHER MODELING 

df = pd.read_csv("../climatedata.csv")

# features = ["YEAR", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "County"]

# Convert month names to numerical values (1 for January, 2 for February, etc.)
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
for month in months:
    df[month] = pd.to_numeric(df[month])

# Encode county names to numerical values using one-hot encoding
df = pd.get_dummies(df, columns=['County'])

models = {}
for i in df["PARAMETER"].unique().tolist():
  data = df.copy()
  data = data[data['PARAMETER']==i].drop(columns=["PARAMETER", "ANN"], axis=1)

  # Prepare features (X) and target variable (y)
  X = data.drop(columns=["APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])
  y = data["NOV"]  # Predicting rainfall amount for April, you can change this for other months

  # Create and train the linear regression model
  model_name = f"model_{i.lower()}" # Dynamic model name
  model = LinearRegression()
  model.fit(X, y)
  models[model_name] = model


# Define function to construct example data
# Get current year and set as default if not provided

def construct_input_data(month=None, county_to_set_1=None):
    year = np.random.randint(2000, 2024)
    # Start with empty dictionary
    input_data = {
        "YEAR": [year],
        "JAN": [0],
        "FEB": [0],
        "MAR": [0],
    }

    # Set county values
    for county in df.columns:
        if county.startswith("County_"):
            if county == f"County_{county_to_set_1}":
                input_data[county] = [1]
            else:
                input_data[county] = [0]

    return input_data

def get_predictions(input_data):
    return  np.array([model.predict(example_df)[0] for model in models.values()])

# Example usage
year = 2000
month = "DEC"
county_to_set_1 = "NAIROBI"
example_data = construct_input_data(month, county_to_set_1)
print("Example data:")
print(example_data)

# Example prediction for a given year, month (encoded as numbers), and county
example_df = pd.DataFrame(example_data)
example_prediction = get_predictions(example_df)

print("[+] Example prediction", example_prediction)