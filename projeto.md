test_name: Validar Fluxo de Tarefas

marks:
  - parametrize:
      key: todo_id
      vals: [1, 5, 15]

stages:
  - name: Buscar Tarefa Específica
    request:
      method: GET
      url: https://jsonplaceholder.typicode.com/todos/{todo_id}
    response:
      status_code: 200
      save:
        json:
          id_do_usuario: userId

  - name: Buscar Todas as Tarefas do Usuário
    request:
      method: GET
      url: https://jsonplaceholder.typicode.com/todos
      params:
        userId: "{id_do_usuario}"
    response:
      status_code: 200
      verify_response_with:
        function: utils:validar_lista_tarefas
