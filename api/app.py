
from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/model.pkl")

@app.get("/predict")
def predict(text:str):

    pred = model.predict([text])

    return {"prediction":str(pred)}
