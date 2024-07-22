# language: pt
Funcionalidade: Cadastro de produto na API
  Como colaborador do IJJ
  Eu quero poder cadastrar novos produtos
  Para conseguir manter um controle do estoque

  Cenário: Produto adicionado com sucesso
    Dado que o usuário esteja autenticado
    Quando o usuário cadastra um novo produto com informações válidas
    Então a resposta deve possuir o status code 200