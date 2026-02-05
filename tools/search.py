import asyncio
from providers.searchit import SearchTool

async def search(
    query: str,
    max_results: int = 5,
    search_type: str = "text",
    region: str = "us-en",
    safesearch: str = "moderate",
    backend: str = "auto",
    size: str | None = None,
    color: str | None = None,
    proxy: str | None = None
) -> list | dict:
    """
    Search the web using various providers (Google, Bing, DuckDuckGo, etc.).

    Args:
        query: The search term.
        max_results: Number of results to return (default: 5).
        search_type: Type of search ('text', 'images', 'videos', 'news') (default: 'text').
        region: Region code (e.g., 'us-en') (default: 'us-en').
        safesearch: Safesearch level ('on', 'moderate', 'off') (default: 'moderate').
        backend: Specific backend or 'auto' (default: 'auto').
        size: Image size filter (e.g., 'Wallpaper', 'Large') (optional, images only).
        color: Image color filter (optional, images only).
        proxy: Proxy URL string (optional).
    """
    tool = SearchTool(
        query=query,
        max_results=max_results,
        search_type=search_type,
        region=region,
        safesearch=safesearch,
        backend=backend,
        size=size,
        color=color,
        proxy=proxy
    )
    # The searchit library is synchronous, so we offload it to a thread
    # to avoid blocking the async event loop of the MCP server.
    return await asyncio.to_thread(tool.run)
