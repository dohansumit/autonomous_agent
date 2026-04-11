from fastapi import FastAPI, HTTPException
import joblib
import os

app = FastAPI()

MODEL_PATH = "models/model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

model = None
vectorizer = None


def load_artifacts():
    global model, vectorizer

    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model not found at {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    if os.path.exists(VECTORIZER_PATH):
        vectorizer = joblib.load(VECTORIZER_PATH)


# load artifacts when API starts
@app.on_event("startup")
def startup_event():
    load_artifacts()


@app.get("/")
def health():
    return {"status": "API running"}


@app.get("/predict")
def predict(text: str):

    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:

        if vectorizer:
            X = vectorizer.transform([text])
        else:
            X = [text]

        pred = model.predict(X)[0]

        return {
            "text": text,
            "prediction": str(pred)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))