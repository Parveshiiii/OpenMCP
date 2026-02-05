import requests
from bs4 import BeautifulSoup
import asyncio

def _get_text_from_url(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # raise error if request failed
    
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\n", strip=True)

async def fetch_url(url: str):

    return await asyncio.to_thread(_get_text_from_url, url)


