import aiohttp
import asyncio


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = ["https://example.com", "https://google.com"]
    html = await asyncio.gather(*(fetch_url(url) for url in urls))
    # Parse and process the HTML content
    print(html)


# Running the web scraper
asyncio.run(main())
