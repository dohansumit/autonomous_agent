class APIAgent:

    def run(self):

        print("Generating FastAPI service")

        api_code = """
from fastapi import FastAPI
import joblib
import os

app = FastAPI()

MODEL_PATH = "models/model.pkl"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("Model not found")

model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status":"ok"}


@app.get("/predict")
def predict(text:str):

    pred = model.predict([text])[0]

    sentiment = "positive" if pred==1 else "negative"

    return {"prediction":sentiment}
"""

        os.makedirs("api", exist_ok=True)

        with open("api/app.py","w") as f:
            f.write(api_code)