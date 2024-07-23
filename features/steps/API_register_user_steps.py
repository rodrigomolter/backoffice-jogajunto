from behave import given, when, then
from jsonschema import validate
from utils.utils import Utils

@given('que o usuário possua email e senha válidos')
def step_valid_email_password(context):
  assert context.user.email
  assert context.user.password

@when('o usuário envia a solicitação de criação de usuário')
def step_register_request(context):
  data = {
    "email": context.user.email,
    "password": context.user.password
  } 
  validate(instance=data, schema=Utils.json_to_dict("user_request.json"))
  context.response = context.api.create_user(data)

@then('a resposta deve possuir o status code 200')
def step_response_status_code_200(context):
  assert context.response.status_code == 200