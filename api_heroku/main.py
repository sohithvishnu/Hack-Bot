from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_pipeline
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()



class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "ok", "model_version":"1.0.0"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}