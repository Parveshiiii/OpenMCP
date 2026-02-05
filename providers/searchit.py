"""
**Not for prodcution use**

use proxy to avoid rate-limits
searchit already have the proxy as a option you can check the repo from link below

link: https://github.com/OE-Void/Search-IT
"""
try:
    from searchit import Search
except ImportError as e:
    raise ImportError("The 'searchit' module is not installed. Please install it before running.") from e

class SearchTool:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def run(self):
        """Execute the search based on the configured type."""
        try:
            # Set defaults for optional parameters if they weren't passed
            search_type = getattr(self, "search_type", "text")
            proxy = getattr(self, "proxy", None)
            max_results = getattr(self, "max_results", 5)
            region = getattr(self, "region", "us-en")
            safesearch = getattr(self, "safesearch", "moderate")

            with Search(proxy=proxy) as s:
                if search_type == "text":
                    return s.text(
                        self.query,
                        region=region,
                        safesearch=safesearch,
                        max_results=max_results,
                        backend=getattr(self, "backend", "auto")
                    )
                elif search_type == "images":
                    return s.images(
                        self.query,
                        region=region,
                        safesearch=safesearch,
                        max_results=max_results,
                        size=getattr(self, "size", None),
                        color=getattr(self, "color", None)
                    )
                elif search_type == "videos":
                    return s.videos(
                        self.query,
                        region=region,
                        safesearch=safesearch,
                        max_results=max_results,
                    )
                elif search_type == "news":
                    return s.news(
                        self.query,
                        region=region,
                        safesearch=safesearch,
                        max_results=max_results,
                    )
                else:
                    raise ValueError(f"Unsupported search type: {search_type}")
        except Exception as e:
            return {"error": str(e)}

