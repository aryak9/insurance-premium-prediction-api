from pydantic import BaseModel, Field
from typing import Dict


class RiskProfile(BaseModel):
    bmi: float = Field(
        ...,
        description="Body Mass Index calculated from weight and height"
    )
    age_group: str = Field(
        ...,
        description="Age group calculated from the user's age"
    )
    lifestyle_risk: str = Field(
        ...,
        description="Lifestyle risk calculated from smoking status and BMI"
    )
    city_tier: int = Field(
        ...,
        description="City tier calculated from the user's city"
    )


class ModelInfo(BaseModel):
    name: str = Field(
        ...,
        description="Name of the prediction model"
    )
    version: str = Field(
        ...,
        description="Version of the prediction model"
    )


class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="Predicted insurance premium category"
    )

    confidence: float = Field(
        ...,
        ge=0,
        le=1,
        description="Model confidence for the predicted category"
    )

    risk_profile: RiskProfile

    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes"
    )

    model: ModelInfo


class BatchPredictionResponse(BaseModel):
    total_predictions: int
    results: list[PredictionResponse]