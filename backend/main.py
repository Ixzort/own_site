from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",   # Next.js по умолчанию
    "http://localhost:8000",   # сам API (для тестов)
    # Добавь свои домены и фронтовые адреса по мере надобности
]

load_dotenv()

app = FastAPI(
    title="Solana Memecoin Backend",
    version="0",
    description="Backend API for Memecoin Site"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import market
app.include_router(market.router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "ok", "message": "Welcome to Memecoin Backend!"}