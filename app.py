from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.predict import predict_output, model_version, model
from schema.user_input import BatchUserInput, UserInput
from schema.prediction_response import PredictionResponse, BatchPredictionResponse


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get("/health")
def health_check():
    return {
        "status": "ok", 
        "version": model_version,
        "model_loaded": model is not None
        }

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content=prediction)
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
    

    
@app.post("/predict/batch", response_model=BatchPredictionResponse)
def predict_batch(data: BatchUserInput):
    results = []

    try:
        for user in data.users:

            user_input = {
                "bmi": user.bmi,
                "age_group": user.age_group,
                "lifestyle_risk": user.lifestyle_risk,
                "city_tier": user.city_tier,
                "income_lpa": user.income_lpa,
                "occupation": user.occupation
            }

            prediction = predict_output(user_input)
            results.append(prediction)

        return {
            "total_predictions": len(results),
            "results": results
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )   