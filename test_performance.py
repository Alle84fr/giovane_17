import pytest
import asyncio
import time
from httpx import AsyncClient, ASGITransport
from api_pagamentos import app

@pytest.mark.asyncio
@pytest.mark.parametrize("quantidade_requisicoes", [5, 20, 50])
async def test_performance_pagamentos(quantidade_requisicoes):
    transporte = ASGITransport(app=app)
    
    async with AsyncClient(transport=transporte, base_url="http://test") as cliente:
        inicio = time.perf_counter()
        
        # Dispara todas as requisições simultaneamente
        tarefas = [cliente.get("/processar") for _ in range(quantidade_requisicoes)]
        respostas = await asyncio.gather(*tarefas)
        
        fim = time.perf_counter()
        tempo_total = fim - inicio
        
        # Validações
        for resposta in respostas:
            assert resposta.status_code == 200
        
        print(f"\n{quantidade_requisicoes} reqs concluídas em {tempo_total:.2f}s")
        assert tempo_total < 3.5, f"Performance ruim: {tempo_total}s"
