# language: pt
Funcionalidade: Login do usuário na API
  Como colaborador do IJJ
  Quero realizar o login na API
  Para acessar a conta e utilizar a API

  Cenário: Login com sucesso
    Dado que o usuário esteja cadastrado na API com email e senha validos
    Quando o usuário faz uma requisição para "/login" passando o email e senha
    Então a resposta deve possuir o status code 200
    E a resposta deve conter o token de acesso
    E o schema da resposta de login deve ser valido