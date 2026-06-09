from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import feedparser
import uvicorn


app = FastAPI(title='MCP FeedParser for FreeCodeCamp API')


@app.post('/freecodecamp_news_search')
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


@app.post('/fcc_channel_youtube_updates')
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


# @app.post('/filewrite')
# def filewrite(content: str, path: str) -> dict[str, str]:
#     """Requires content and file path to writent content to specified file. Agents should ensure that files have appropriate extensions"""

#     try:
#         with open(path, 'w', encoding='utf-8') as file:
#             file.write(content)
#     except Exception as e:
#         return {
#             "error": e
#         }
#     else:
#         return {
#             "success": True,
#             "message": 'File write successful'
#         }


mcp = FastApiMCP(app, name='MCP FeedParser for FreeCodeCamp')
mcp.mount_http()

if __name__ == "__main__":
    uvicorn.run('fastmcp_feedparser:app', host='localhost', port=8082, reload=True)
