from behave import given, when, then
from pages.register_page import RegisterPage
from models.user import User

@given('que o usuário esta na página de registro de usuário')
def step_open_register_page(context):
  context.page = RegisterPage(context.browser)
  context.page.open()

@when('ele efetuar o cadastro com um email válido')
def step_fill_valid_email(context):
  context.user = User()
  context.page.fill_email(context.user.email)

@when('a com uma senha válida')
def step_fill_valid_password(context):
  register_page: RegisterPage = context.page
  register_page.fill_password(context.user.password)
  register_page.fill_password_confirmation(context.user.password)
  register_page.submit()

@then('deve receber a mensagem de erro "{message}"')
def step_receive_warning_message(context, message):
  assert message in context.page.get_invalid_email_message()

@then('deve receber a mensagem de sucesso "{message}"')
def step_receive_success_message(context, message):
  assert message in context.page.get_registered_sucessfully_message()

@when('tentar efetuar cadastro com o email inválido "{invalid_email}"')
def step_fill_invalid_password(context, invalid_email):
  context.page.fill_email(invalid_email)