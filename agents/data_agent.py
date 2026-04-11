from agents.research_agent import ResearchAgent
from tools.credential_manager import get_api_key
import requests
import pandas as pd
import os


class DataAgent:

    def __init__(self):

        self.research_agent = ResearchAgent()

    def run(self):

        print("📥 Running Data Agent")

        # discover API
        api_url = self.research_agent.find_data_source()

        # ask credential manager
        api_key = get_api_key("NewsAPI")

        url = f"{api_url}&apiKey={api_key}"

        print("Fetching data from NewsAPI...")

        response = requests.get(url)

        data = response.json()

        if "articles" not in data:

            print("API error:", data)

            return

        texts = []

        for article in data["articles"]:

            title = article.get("title")

            if title:
                texts.append(title)

        if len(texts) == 0:

            print("⚠ No data returned from API")

            texts = [
                "Market is rising",
                "Stocks crashed today",
                "Investors optimistic"
            ]

        df = pd.DataFrame({"text": texts})

        os.makedirs("dataset", exist_ok=True)

        df.to_csv("dataset/news.csv", index=False)

        print("Dataset saved to dataset/news.csv")