from datetime import datetime, timedelta
from agent.tools import get_search_tool
from agent.summarizer import get_summarizer_chain

def fetch_and_summarize_news(days: int = 1):
    """
    Main function:
    1. Build date-based search queries
    2. Search for AI news using Tavily
    3. Summarize each article using our LangChain chain
    4. Return structured results
    """

    search_tool = get_search_tool()
    summarizer = get_summarizer_chain()

    results_by_day = {}

    for i in range(days):
        target_date = datetime.now() - timedelta(days=1)
        date_str = target_date.strftime("%Y-%m-%d")
        display_date = target_date.strftime("%d %B, %Y")

        print(f" Searching news for {display_date}... ")

    query = f"artificial intelligence AI news {date_str}"
    raw_results = search_tool.invoke(query)

    # raw_results is a list of dicts with: url, title, content, score
    articles = []

    for article in raw_results[:4]:  # top 4 articles per day
        title = article.get("title", "No title")
        content = article.get("content", "")
        url = article.get("url", "")

        if not content or len(content) < 100:
            continue  # skip empty articles

        print(f"Summarizing: {title[:50]}...")

        summary = summarizer.invoke({
            "title": title,
            "content": content[:3000],  # limit tokens
            "date": display_date
        })

        articles.append({
            "title": title,
            "url": url,
            "summary": summary,
            "date": display_date
        })

    results_by_day[display_date] = articles

    return results_by_day

