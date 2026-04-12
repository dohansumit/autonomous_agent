import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class TrainingAgent:

    def run(self):

        print("🚀 Running Training Agent")

        df = pd.read_csv("dataset/news.csv")

        analyzer = SentimentIntensityAnalyzer()

        df["sentiment"] = df["text"].apply(
            lambda x: 1 if analyzer.polarity_scores(x)["compound"] > 0 else 0
        )

        X = df["text"]
        y = df["sentiment"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2
        )

        vectorizer = TfidfVectorizer()

        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        model = LogisticRegression()

        mlflow.set_tracking_uri("http://localhost:5000")
        mlflow.set_experiment("news_sentiment")

        with mlflow.start_run():

            model.fit(X_train_vec, y_train)

            acc = model.score(X_test_vec, y_test)

            mlflow.log_metric("accuracy", acc)
            mlflow.sklearn.log_model(model, "model")

            print("accuracy:", acc)

        # Save model locally
        joblib.dump(model, "models/model.pkl")
        joblib.dump(vectorizer, "models/vectorizer.pkl")

        print("✅ Model saved")