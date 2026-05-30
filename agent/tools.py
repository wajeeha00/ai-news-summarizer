from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()

def get_search_tool():
    """
    TavilySearchResults is a pre-built LangChain tool.
    max_results=5 means fetch top 5 articles per search.
    """
    search_tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",     # deeper search, better results
        include_answer=True,         # Tavily gives a quick answer too
        include_raw_content=True,    # full article content, not just snippet
    )
    return search_tool