from fastapi import FastAPI
import joblib

app = FastAPI()

# load vectorizer and model
vectorizer = joblib.load("models/vectorizer.pkl")
model = joblib.load("models/model.pkl")


@app.get("/predict")
def predict(text: str):

    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    return {
        "text": text,
        "prediction": int(pred)
    }