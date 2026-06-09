from fastapi import FastAPI
import feedparser
from fastmcp import FastMCP


# app = FastAPI(title='MCP FeedParser for FreeCodeCamp API')
mcp = FastMCP(name='MCP FeedParser for FreeCodeCamp API')

@mcp.tool('freecodecamp_news_search')
def freecodecamp_news_search(query: str, max_results: int = 3) -> dict[str, list[dict[str, str]]]:
    res = feedparser.parse('https://www.freecodecamp.org/news/rss')
    query_lower = query.lower().strip()
    results = []
    for feed in res.entries:
        if (len(results) >= max_results):
            break
        if (query_lower in feed.title.lower() or query_lower in feed.description.lower()):
            results.append({
                'title': feed.get('title', ''),
                'url': feed.get('link', ''),
                'desc': feed.get('description', ''),
            })
    return {'results': results}


@mcp.tool('fcc_channel_youtube_updates')
def fcc_channel_youtube_updates(query: str, max_results: int = 3) -> dict[str, list[dict[str, str]]]:
    res = feedparser.parse(
        'https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ')

    query_lower = query.lower().strip()
    results = []
    for feed in res.entries:
        if (len(results) >= max_results):
            break
        if (query_lower in feed.title.lower() or query_lower in feed.description.lower()):
            results.append({
                'title': feed.get('title', ''),
                'url': feed.get('link', ''),
                'desc': feed.get('description', ''),
            })
    return {'results': results}


if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0')
