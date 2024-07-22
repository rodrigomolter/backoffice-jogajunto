# language: pt
Funcionalidade: Cadastro de produto no Backoffice
  Como colaborador do IJJ
  Eu quero acessar a página de cadastro
  Para conseguir cadastrar novos produtos

  Contexto: Usuário na tela de cadastro de produto
    Dado que usuário esteja na página de cadastro

  Esquema do Cenário: Produto adicionado com sucesso
    Quando adicionar informações de produto na categoria "<categoria>"
    E clicar em enviar novo produto
    Então deve ser criado visualização de novo produto na home page

    Exemplos: 
    | categoria  |
    | Roupas     |
    | Calçados   |
    | Acessorios |