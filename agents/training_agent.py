import os
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

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

        if "text" not in df.columns:
            raise ValueError("Dataset must contain a 'text' column")

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

        # Build pipeline (vectorizer + model)
        pipeline = Pipeline([
            ("vectorizer", TfidfVectorizer()),
            ("model", LogisticRegression(max_iter=1000))
        ])

        # MLflow setup
        mlflow_uri = os.getenv("MLFLOW_TRACKING_URI", "file:./mlruns")

        mlflow.set_tracking_uri(mlflow_uri)
        mlflow.set_experiment("news_sentiment")

        print("Using MLflow server:", mlflow_uri)

        with mlflow.start_run():

            pipeline.fit(X_train, y_train)

            acc = pipeline.score(X_test, y_test)

            mlflow.log_metric("accuracy", acc)

            # Log full pipeline
            mlflow.sklearn.log_model(
                pipeline,
                artifact_path="model"
            )

            print("accuracy:", acc)

        # Save model locally for FastAPI inference
        joblib.dump(pipeline, "models/model.pkl")

        print("✅ Model saved to models/model.pkl")