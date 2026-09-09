from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

APP_VERSION = "1.1.0"
MODEL_VERSION = "model-1"

app = FastAPI(title="student-ml-api")


class PredictRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": APP_VERSION,
        "model_version": MODEL_VERSION,
    }


@app.post("/predict")
def predict(payload: PredictRequest):
    result = payload.value * 2
    return {"input": payload.value, "prediction": result}