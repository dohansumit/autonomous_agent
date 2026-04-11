import pandas as pd
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class HyperparameterAgent:

    def tune(self):

        print("Running hyperparameter tuning...")

        df = pd.read_csv("dataset/news.csv")

        # Generate sentiment labels (same logic as training agent)
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

        best_acc = 0
        best_C = None

        for C in [0.1, 1, 10]:

            model = SVC(C=C)

            with mlflow.start_run():

                model.fit(X_train_vec, y_train)

                acc = model.score(X_test_vec, y_test)

                mlflow.log_param("C", C)
                mlflow.log_metric("accuracy", acc)

                print(f"C={C} accuracy={acc}")

                if acc > best_acc:
                    best_acc = acc
                    best_C = C

        print("Best hyperparameter:", best_C)
        print("Best accuracy:", best_acc)