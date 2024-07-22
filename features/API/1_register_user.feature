Funcionalidade: Registro de novo usuário na API
  Como colaborador do IJJ
  Eu quero poder me registrar
  Para conseguir usufruir da API

  Cenário: Novo Usuário registrado com sucesso
    Dado que o usuário possua email e senha válidos
    Quando o usuário envia a solicitação de criação de usuário
    Então a resposta deve possuir o status code 200