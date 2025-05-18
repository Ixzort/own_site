from fastapi import APIRouter, HTTPException
from coingecko import get_token_marketcap
from redis_client import redis_client
from schemas.market import MarketCapResponse

router = APIRouter()

TOKEN_ID = "solana"  # поменяешь на свой id позже

@router.get("/marketcap", response_model=MarketCapResponse)
async def get_marketcap():
    cache_key = f"marketcap:{TOKEN_ID}"
    cached = await redis_client.get(cache_key)
    if cached:
        import json
        return MarketCapResponse(**json.loads(cached))
    data = await get_token_marketcap(TOKEN_ID)
    if not data:
        raise HTTPException(status_code=404, detail="Token not found")
    import json
    await redis_client.set(cache_key, json.dumps(data), ex=60)
    return MarketCapResponse(**data)



@router.get("/marketcap")
async def get_marketcap():
    # Заглушка — потом тут будет обращение к CoinGecko
    return {
        "price": 0.01,
        "market_cap": 100000
    }
