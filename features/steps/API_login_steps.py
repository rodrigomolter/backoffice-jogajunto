from behave import given, when, then
from jsonschema import validate
from utils.utils import Utils

@given('que o usuário esteja cadastrado na API com email e senha validos')
def step_valid_email_password(context):
  ...

@when('o usuário faz uma requisição para "/login" passando o email e senha')
def step_login_request(context):
  data = {
      "email": context.user.email,
      "password": context.user.password
  } 
  validate(instance=data, schema=Utils.json_to_dict("user_request.json"))
  context.response = context.api.login(data)

@then('a resposta deve conter o token de acesso')
def step_response_must_have_acess_token(context):
  token = context.response.json()['token']
  assert token
  context.api.update_session(token)
  
@then('o schema da resposta de login deve ser valido')
def step_response_must_have_valid_schema(context):
  validate(instance=context.response.json(), schema=Utils.json_to_dict("login_response.json"))