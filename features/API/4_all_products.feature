# language: pt
Funcionalidade: Visualização dos produtos na API
  Como colaborador do IJJ
  Eu quero poder visualizar os produtos cadastrados
  Para conseguir manter um controle do estoque

  Cenário: Visualizar todos os produtos
    Dado que o usuário esteja autenticado
    Quando solicitar todos os produtos cadastrados
    Então a resposta deve possuir o status code 200
    E o schema da resposta deve ser valido