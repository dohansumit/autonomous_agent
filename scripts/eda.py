import pandas as pd

df = pd.read_csv("dataset/news.csv")

print(df.head())
print(df.describe())