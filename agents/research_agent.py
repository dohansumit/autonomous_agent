import requests


class ResearchAgent:

    def find_data_source(self, topic="stock market"):

        print("🔎 Research Agent searching for news APIs...")

        sources = {
            "newsapi": "https://newsapi.org/v2/everything?q=stock%20market",
            "gnews": "https://gnews.io/api/v4/search?q=stock",
            "finnhub": "https://finnhub.io/api/v1/news?category=general"
        }

        selected_source = "newsapi"

        print("Selected data source:", selected_source)

        return sources[selected_source]