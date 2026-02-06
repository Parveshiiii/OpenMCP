import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from mcp.server.fastmcp import FastMCP
from tools.search import search
from tools.weather_forecast import get_forecast
from tools.sandbox import execute_python
from tools.url_extractor import fetch_url
from connectors.resend import EmailSender

mcp = FastMCP("OpenMCP")

# Register the tools
mcp.tool()(search)
mcp.tool()(get_forecast)
mcp.tool()(execute_python)
mcp.tool()(fetch_url)

@mcp.tool()
async def send_email(to: list[str], subject: str, html: str) -> str:
    """
    Send an email using the Resend API.
    
    Args:
        to: List of email addresses to send to.
        subject: The subject of the email.
        html: The HTML content of the email body.
    """
    sender = EmailSender(to=to, subject=subject, html=html)
    result = await sender.send_mail()
    return str(result)

