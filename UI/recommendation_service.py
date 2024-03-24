# load the model from disk
import pickle
import numpy as np
crop_model_weight = "cropModel/crop_model.pickle"
crop_model = pickle.load(open(crop_model_weight, 'rb'))


def predict_recommendation (weather,model=crop_model):
    print("[+] Predicting recommendations")
    result = model.predict(weather)

    return result

# TEst recommendation
input_data_test = np.array([2, 1, 0.43])

recommendations = predict_recommendation(input_data_test.reshape(1, -1), crop_model)

print(recommendations)

