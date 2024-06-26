import asyncio
import json
import time
from asyncio import sleep

import requests
import logging

logfile = open('logfile', 'w')
logging.basicConfig(filename="api.log",  filemode='w')
logger = logging.getLogger()


async def fetch(url):
    print("Fetching %s" % (url))
    response_text = requests.get(url)
    json_data = json.loads(response_text.text)
    await sleep(1)
    logger.info(json.dumps(json_data))
    logfile.write(json.dumps(json_data))


async def main():
    await asyncio.gather(fetch("https://jsonplaceholder.typicode.com/users"),
                         fetch("https://restcountries.com/v2/all"), fetch(
            "https://raw.githubusercontent.com/russ666/all-countries-and-cities-json/master/countries.json"))


start_time = time.perf_counter()
asyncio.run(main())
elapsed_time = time.perf_counter() - start_time
print("Time Taken to Complete %f" % (elapsed_time))
