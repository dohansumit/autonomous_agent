import os
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

        # Ensure folders exist
        os.makedirs("models", exist_ok=True)
        os.makedirs("dataset", exist_ok=True)

        dataset_path = "dataset/news.csv"

        if not os.path.exists(dataset_path):
            raise FileNotFoundError("Dataset not found at dataset/news.csv")

        df = pd.read_csv(dataset_path)

        print(f"Loaded dataset with {len(df)} rows")

        # Sentiment labeling using VADER
        analyzer = SentimentIntensityAnalyzer()

        df["sentiment"] = df["text"].apply(
            lambda x: 1 if analyzer.polarity_scores(str(x))["compound"] > 0 else 0
        )

        X = df["text"]
        y = df["sentiment"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Vectorization
        vectorizer = TfidfVectorizer()

        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        model = LogisticRegression(max_iter=1000)

        # MLflow setup
        mlflow_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")

        mlflow.set_tracking_uri(mlflow_uri)
        mlflow.set_experiment("news_sentiment")

        print("Using MLflow server:", mlflow_uri)

        with mlflow.start_run():

            model.fit(X_train_vec, y_train)

            acc = model.score(X_test_vec, y_test)

            mlflow.log_metric("accuracy", acc)

            # Log model
            mlflow.sklearn.log_model(model, "model")

            # Log vectorizer
            mlflow.log_artifact("models/vectorizer.pkl") if os.path.exists("models/vectorizer.pkl") else None

            print("accuracy:", acc)

        # Save model locally for FastAPI inference
        joblib.dump(model, "models/model.pkl")
        joblib.dump(vectorizer, "models/vectorizer.pkl")

        print("✅ Model saved to models/")