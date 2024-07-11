# tools.py
from duckduckgo_search import DDGS
from praisonai_tools import BaseTool

class InternetSearchTool(BaseTool):
    name: str = "InternetSearchTool"
    description: str = "Search Internet for relevant information based on a query or latest news"

    def _run(self, query: str):
        ddgs = DDGS()
        results = ddgs.text(keywords=query, region='wt-wt', safesearch='moderate', max_results=5)
        return results
    
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools.reddit_search.tool import RedditSearchRun
# pip install tavily-python
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.utilities.you import YouSearchAPIWrapper
# pip install youtube_search
from langchain_community.tools import YouTubeSearchTool
# pip install wikipedia
from langchain_community.utilities import WikipediaAPIWrapper

class TavilyTool(BaseTool):
    name: str = "TavilyTool"
    description: str = "Search Tavily for relevant information based on a query."

    def _run(self, query: str):
        api_wrapper = TavilySearchAPIWrapper()
        results = api_wrapper.results(query=query, max_results=5)
        return results

class YouSearchTool(BaseTool):
    name: str = "You Search Tool"
    description: str = "Search You.com for relevant information based on a query."

    def _run(self, query: str):
        api_wrapper = YouSearchAPIWrapper()
        results = api_wrapper.results(query=query, max_results=5)
        return results

class WikipediaSearchTool(BaseTool):
    name: str = "WikipediaSearchTool"
    description: str = "Search Wikipedia for relevant information based on a query."

    def _run(self, query: str):
        api_wrapper = WikipediaAPIWrapper(top_k_results=4, doc_content_chars_max=100)
        results = api_wrapper.load(query=query)
        return results

# pip install open-interpreter
from interpreter import interpreter

class OpenInterpreterTool(BaseTool):
    name: str = "Open Interpreter Tool"
    description: str = "Use Open Interpreter configured to create and execute code based on natural language commands."

    def __init__(self):
        super().__init__()
        interpreter.auto_run = True

    def _run(self, code: str):
        result = interpreter.chat(code)
        return result

# pip install spider-client
from spider import Spider

class SpiderSearchTool(BaseTool):
    name: str = "Spider Search Tool"
    description: str = "Use Spider to search the web for relevant information based on a query."

    def __init__(self):
        super().__init__()

    def _run(self, query: str):
        spider = Spider()
        params = {
            "fetch_page_content": False,
            "limit": 5,
        }
        result = spider.search(query, params=params)
        return result

class SpiderScrapeTool(BaseTool):
    name: str = "Spider Scrape Tool"
    description: str = "Use Spider to scrape a single url for relevant information."

    def __init__(self):
        super().__init__()

    def _run(self, url: str):
        spider = Spider()
        params = {
            "return_format": "markdown",
            "limit": 5,
        }
        result = spider.scrape_url(url, params=params)
        return result

class SpiderCrawlTool(BaseTool):
    name: str = "Spider Crawl Tool"
    description: str = "Use Spider to crawl a whole website for relevant information."

    def __init__(self):
        super().__init__()

    def _run(self, url: str):
        spider = Spider()
        params = {
            "return_format": "markdown",
            "limit": 5,
        }
        result = spider.crawl_url(url, params=params)
        return result

# Example usage
if __name__ == "__main__":
    tool = OpenInterpreterTool()
    code = "Plot AAPL and META's normalized stock prices"
    output = tool._run(code)
    print(output)
