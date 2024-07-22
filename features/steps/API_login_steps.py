from behave import given, when, then

@given('que o usuário esteja cadastrado na API com email e senha validos')
def step_valid_email_password(context):
  ...

@when('o usuário faz uma requisição para "/login" passando o email e senha')
def step_login_request(context):
  context.response = context.api.login(context.user)

@then('a resposta deve conter o token de acesso')
def step_response_must_have_acess_token(context):
  token = context.response.json()['token']
  assert token
  context.api.update_session(token)
  
@then('o schema da resposta deve ser valido')
def step_response_must_have_valid_schema(context):
  ...