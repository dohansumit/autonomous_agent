import os


class APIAgent:

    def run(self):

        print("Generating FastAPI service")

        api_code = """
from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/model.pkl")

@app.get("/predict")
def predict(text:str):

    pred = model.predict([text])

    return {"prediction":str(pred)}
"""

        os.makedirs("api", exist_ok=True)

        with open("api/app.py","w") as f:
            f.write(api_code)