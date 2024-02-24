# load the model from disk
import pickle
import numpy as np
weather_model_weight = "weatherModel/weather_model.pickle"
crop_model_weight = "cropModel/crop_model.pickle"
weather_model = pickle.load(open(weather_model_weight, 'rb'))
crop_model = pickle.load(open(crop_model_weight, 'rb'))

# Function to predict rainfall in the future
def predict_weather(model, base_index, base_year, num_months):
    print("[+] Predicting weather")
    predictions = []

    for i in range(num_months):
        future_index = base_index + i
        future_year = base_year + (future_index // 12)
        future_month = future_index % 12

        future_data = np.array([[future_index, future_year]])
        future_prediction = model.predict(future_data).reshape(-1)
        predictions.append(future_prediction[future_month])

    return np.array(predictions)

def predict_recommendation (weather,model):
    print("[+] Predicting recommendations")
    result = model.predict(weather)

    return result

# Predicting rainfall in future
base_index = 100 #data.shape[0]  # Use the last index in the dataset
base_year = 2023  # Use the last year in the dataset
num_months = 3  # Predict 3 months into the future

weather_predictions = predict_weather(weather_model, base_index, base_year, num_months).reshape(1, -1)
# print(f"The predictions for the next {num_months} months are:", predictions)

recommendations = predict_recommendation(weather_predictions, crop_model)

print(recommendations)