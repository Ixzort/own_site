from pydantic import BaseModel

class MarketCapResponse(BaseModel):
    price: float
    market_cap: float
