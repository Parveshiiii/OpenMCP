import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from mcp.server.fastmcp import FastMCP
from tools.search import search
from tools.weather_forecast import get_forecast
from tools.sandbox import execute_python
from tools.url_extractor import fetch_url

mcp = FastMCP("OpenMCP")

# Register the tools
mcp.tool()(search)
mcp.tool()(get_forecast)
mcp.tool()(execute_python)
mcp.tool()(fetch_url)

