from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/processar")
async def processar_pagamento():
    await asyncio.sleep(1.5) # Simula processamento
    return {"status": "pagamento_aprovado"}
