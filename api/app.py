from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle


app = FastAPI(title="Heart Disease Prediction API")
app.mount("/static", StaticFiles(directory="website/static"), name="static")

# Allow website to communicate with API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Load trained model and scaler
with open("model/heart_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("model/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


@app.get("/")
def home():
    return FileResponse("website/templates/index.html")


@app.post("/predict")
def predict(data: PatientData):

    input_data = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "cp": data.cp,
        "trestbps": data.trestbps,
        "chol": data.chol,
        "fbs": data.fbs,
        "restecg": data.restecg,
        "thalach": data.thalach,
        "exang": data.exang,
        "oldpeak": data.oldpeak,
        "slope": data.slope,
        "ca": data.ca,
        "thal": data.thal
    }])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0][1]

    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease Detected"

    return {
        "prediction": int(prediction),
        "result": result,
        "probability": round(float(probability) * 100, 2)
    }