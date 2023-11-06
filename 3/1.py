import asyncio

import aiohttp


async def weather_generator():
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41"
            async with session.get(url) as response:
                yield await response.json()


async def main():
    async for weather_data in weather_generator():
        print(weather_data)
        await asyncio.sleep(5)



asyncio.run(main())
