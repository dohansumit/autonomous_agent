import pandas as pd

data = {
    "text":[
        "Market is going up",
        "Stocks crashed today",
        "Investors are optimistic"
    ],
    "label":[1,0,1]
}

df = pd.DataFrame(data)

df.to_csv("dataset/news.csv",index=False)

print("Dataset created")