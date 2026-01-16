from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .schemas import CarFeatures, predictionResponse
from .model import predict_price, load_artifacts

app = FastAPI(title="Car Price Prediction API", version="1.0")


from pathlib import Path
from . import model

@app.on_event("startup")
def startup_event():
    # Fix paths - artifacts are one directory up from the app folder
    # main.py is in app/, so parent is app/, parent.parent is car_price_api/
    base_dir = Path(__file__).resolve().parent.parent
    model.MODEL_PATH = base_dir / "random_forest_model.pkl"
    model.COLS_PATH = base_dir / "feature_columns.pkl"
    load_artifacts()


@app.get("/")
def test():
    return JSONResponse(
        status_code=200,
        content={"success": True, "message": "this is a test route"}
    )


@app.post("/predict", response_model=predictionResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return predictionResponse(prediction_price=price)
