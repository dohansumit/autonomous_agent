from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="News Sentiment API")

MODEL_PATH = "models/model.pkl"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Model file not found. Run training first.")

model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict(text: str):

    pred = model.predict([text])[0]

    sentiment = "positive" if pred == 1 else "negative"

    return {
        "text": text,
        "prediction": sentiment
    }
@app.get("/health")
def health():
    return {"status": "ok"}

#
