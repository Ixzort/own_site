import aiohttp

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

async def get_token_marketcap(token_id: str):
    params = {
        "ids": token_id,
        "vs_currencies": "usd",
        "include_market_cap": "true"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(COINGECKO_URL, params=params) as resp:
            data = await resp.json()
            if token_id in data:
                return {
                    "price": data[token_id]["usd"],
                    "market_cap": data[token_id]["usd_market_cap"]
                }
            else:
                return None
