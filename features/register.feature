# language: pt
Funcionalidade: Registro de novo usuário no Backoffice
  Como colaborador do IJJ
  Eu quero poder me registrar
  Para conseguir usufruir da aplicação

  Contexto: Usuário na tela de registro
    Dado que o usuário esta na página de registro de usuário
  @skip
  Cenário: Registro com sucesso
    Quando ele efetuar o cadastro com um email válido
    E a com uma senha válida
    Então deve receber a mensagem de sucesso "Usuário cadastrado com sucesso"

  Cenário: Registro com email inválido
    Quando tentar efetuar cadastro com o email inválido "jogajunto@instituto,com"
    E a com uma senha válida
    Então deve receber a mensagem de erro "Digite um e-mail válido"