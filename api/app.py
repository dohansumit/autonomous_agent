from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="News Sentiment API")

MODEL_PATH = "models/model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"


# Check if model files exist
if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Model file not found. Run training first.")

if not os.path.exists(VECTORIZER_PATH):
    raise RuntimeError("Vectorizer file not found. Run training first.")


# Load model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


@app.get("/")
def root():
    return {"message": "News Sentiment API is running"}


@app.get("/predict")
def predict(text: str):

    # Convert text → vector
    text_vec = vectorizer.transform([text])

    # Predict sentiment
    pred = model.predict(text_vec)[0]

    sentiment = "positive" if pred == 1 else "negative"

    return {
        "text": text,
        "prediction": sentiment
    }