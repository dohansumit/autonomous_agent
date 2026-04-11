import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import mlflow
import joblib
import os


class TrainingAgent:

    def run(self):

        print("🚀 Running Training Agent")

        df = pd.read_csv("dataset/news.csv")

        if df.empty:
            print("Dataset empty")
            return

        X = df["text"]

        analyzer = SentimentIntensityAnalyzer()

        labels = []

        for text in X:
            score = analyzer.polarity_scores(text)["compound"]

            if score >= 0:
                labels.append(1)
            else:
                labels.append(0)

        y = labels

        vectorizer = CountVectorizer()

        X_vec = vectorizer.fit_transform(X)

        models = {
            "logistic": LogisticRegression(max_iter=1000),
            "svm": SVC()
        }

        best_model = None
        best_score = 0

        mlflow.set_experiment("news_sentiment")

        for name, model in models.items():

            with mlflow.start_run(run_name=name):

                model.fit(X_vec, y)

                pred = model.predict(X_vec)

                score = accuracy_score(y, pred)

                print(name, "accuracy:", score)

                mlflow.log_param("model", name)
                mlflow.log_metric("accuracy", score)

                if score > best_score:
                    best_score = score
                    best_model = model

        os.makedirs("models", exist_ok=True)

        joblib.dump(best_model, "models/model.pkl")
        joblib.dump(vectorizer, "models/vectorizer.pkl")

        print("✅ Best model saved")