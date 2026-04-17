def validar_lista_tarefas(resposta):
    """
    Valida se o retorno é uma lista e contém a chave 'completed'
    """
    dados = resposta.json()
    assert isinstance(dados, list), "O retorno não é uma lista"
    assert any("completed" in tarefa for tarefa in dados), "Nenhuma tarefa contém a chave 'completed'"
    return True
