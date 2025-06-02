import requests
from bs4 import BeautifulSoup

class DataCollector:
    def fetch_wikipedia_summary(self, topic):
        try:
            response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}")
            if response.status_code == 200:
                return response.json().get("extract", "No summary found.")
            return "Wikipedia entry not found."
        except Exception as e:
            return f"Wikipedia error: {e}"

    def fetch_news_headlines(self, topic, api_key):
        try:
            url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=relevancy&apiKey={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                articles = response.json().get("articles", [])
                return "; ".join(article['title'] for article in articles[:3])
            return "News results not found."
        except Exception as e:
            return f"News API error: {e}"

    def fetch_arxiv_papers(self, topic):
        try:
            url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&start=0&max_results=3"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "xml")
                entries = soup.find_all('entry')
                titles = [entry.title.text.replace('\n', ' ').strip() for entry in entries]
                return "; ".join(titles) if titles else "No ArXiv papers found."
            return "ArXiv query failed."
        except Exception as e:
            return f"ArXiv error: {e}"

    def fetch_semantic_scholar(self, topic):
        try:
            url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit=3&fields=title,abstract"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                papers = data.get("data", [])
                titles = [p["title"] for p in papers]
                return "; ".join(titles) if titles else "No Semantic Scholar papers found."
            return "Semantic Scholar query failed."
        except Exception as e:
            return f"Semantic Scholar error: {e}"

    def collect(self, tasks: list, api_key: str) -> list:
        results = []
        for task in tasks:
            topic = task.split(":")[-1].strip()
            wiki = self.fetch_wikipedia_summary(topic)
            news = self.fetch_news_headlines(topic, api_key)
            arxiv = self.fetch_arxiv_papers(topic)
            semantic = self.fetch_semantic_scholar(topic)
            results.append({
                "task": task,
                "wikipedia": wiki,
                "news": news,
                "arxiv": arxiv,
                "semantic_scholar": semantic
            })
        return results
