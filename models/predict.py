import pickle
import pandas as pd


with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

model_version = "1.0.0"
model_name = "Insurance Premium Prediction Model"

class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]

    confidence = max(probabilities)

    class_probs = {
        label: round(float(probability), 4)
        for label, probability in zip(class_labels, probabilities)
    }

    return {
        "predicted_category": str(predicted_class),
        "confidence": round(float(confidence), 4),

        "risk_profile": {
            "bmi": round(float(user_input["bmi"]), 2),
            "age_group": user_input["age_group"],
            "lifestyle_risk": user_input["lifestyle_risk"],
            "city_tier": user_input["city_tier"]
        },

        "class_probabilities": class_probs,

        "model": {
            "name": model_name,
            "version": model_version
        }
    }