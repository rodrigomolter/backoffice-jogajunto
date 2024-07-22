from behave import given, when, then

@given('que o usuário possua email e senha válidos')
def step_valid_email_password(context):
  assert context.user.email
  assert context.user.password

@when('o usuário envia a solicitação de criação de usuário')
def step_register_request(context):
  context.response = context.api.create_user(context.user)

@then('a resposta deve possuir o status code 200')
def step_response_status_code_200(context):
  assert context.response.status_code == 200