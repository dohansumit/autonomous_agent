from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


@app.get("/predict")
def predict(text: str):

    X = vectorizer.transform([text])   # convert text to features

    pred = model.predict(X)[0]

    return {"prediction": int(pred)}