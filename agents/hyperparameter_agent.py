import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import joblib


class HyperparameterAgent:

    def tune(self):

        print("Running hyperparameter tuning...")

        df = pd.read_csv("dataset/news.csv")

        X = df["text"]
        y = df["label"]

        vectorizer = CountVectorizer()

        X_vec = vectorizer.fit_transform(X)

        param_grid = {
            "C":[0.1,1,10]
        }

        grid = GridSearchCV(LogisticRegression(), param_grid)

        grid.fit(X_vec, y)

        best_model = grid.best_estimator_

        joblib.dump(best_model,"models/model.pkl")
        joblib.dump(vectorizer,"models/vectorizer.pkl")

        print("Best parameters:", grid.best_params_)