from recommendation_service import predict_recommendation
from weather_service import get_predictions, construct_input_data
import datetime
import numpy as np
from models import generate




def serve_recomm_requests(month, county):
    month_mapping = {
    "January": "JAN",
    "February": "FEB",
    "March": "MAR",
    "April": "APR",
    "May": "MAY",
    "June": "JUN",
    "July": "JUL",
    "August": "AUG",
    "September": "SEP",
    "October": "OCT",
    "November": "NOV",
    "December": "DEC"
    }
    month = "December"
    
    if month in month_mapping:
        month_abbrev = month_mapping[month]
    else:
        print("Invalid month name.")


    input_data = construct_input_data(month_abbrev, county)
    # predictions = get_predictions(input_data).reshape(1, -1)
    predictions = generate(input_data).reshape(1, -1)
    
    print("Predictios", predictions)

    recommendations = predict_recommendation(predictions)
    
    return {"weather": predictions, "recommendations": recommendations}

print("[+] Recommendations from Servie", serve_recomm_requests("March", "BUNGOMA"))