# language: pt
Funcionalidade: Login do usuário no Backoffice
  Como colaborador do IJJ
  Quero realizar o login mediante preenchimento das informações solicitadas na plataforma de backoffice
  Para acessar a conta e visualizar as informações do seu perfil

  Contexto: Usuário na tela de login
    Dado que o usuário esteja na página de login

  Cenário: Login com sucesso
    Quando digitar o email válido 
    E preencher com a senha válida
    E clicar no botão "Iniciar Sessão"
    Então deve ser redirecionado para a página de produto
    E receber a mensagem de sucesso "logado com sucesso"