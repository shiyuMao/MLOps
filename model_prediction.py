import pickle
from preprocessing import load_and_preprocess_data

def predict():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
        print("Model loaded from model.pkl")

        _, X_test, _, y_test = load_and_preprocess_data()
        test_sample = X_test[0].reshape(1, -1)
        prediction = model.predict(test_sample)
        print(f"Prediction for {test_sample.tolist()}: {prediction}")
        print(f"True label: {y_test[0]}")