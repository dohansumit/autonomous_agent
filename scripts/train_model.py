import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("dataset/news.csv")

X = df["text"]
y = df["label"]

vectorizer = CountVectorizer()

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()

model.fit(X_vec,y)

joblib.dump(model,"models/model.pkl")
joblib.dump(vectorizer,"models/vectorizer.pkl")

print("Model trained")