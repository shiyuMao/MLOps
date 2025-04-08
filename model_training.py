from sklearn.ensemble import RandomForestClassifier
import pickle
import time
from model_evaluation import evaluate_model
from preprocessing import load_and_preprocess_data

def train_model():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # Create a Random Forest Classifier and train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    start = time.time()
    model.fit(X_train, y_train)
    end = time.time()
    print(f"Model training completed in {end - start:.2f} seconds.")

    # Evaluate the classifier and fairness
    evaluate_model(model, X_test, y_test)

    # Save the trained model to 'model.pkl'
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
        print("Model saved as model.pkl")