from behave import given, when, then
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@given('que o usuário esteja na página de login')
def step_open_register_page(context):
  context.page = LoginPage(context.browser)
  context.page.open()

@when('digitar o email válido "{email}"')
def step_fill_valid_email(context, email):
  context.page.fill_email(email)

@when('preencher com a senha válida "{password}"')
def step_fill_valid_password(context, password):
  context.page.fill_password(password)

@when('clicar no botão "{btn_text}"')
def step_submit_login(context, btn_text):
  context.page.submit()

@then('deve ser redirecionado para a página de produto')
def step_is_at_product_page(context):
  context.page = ProductPage(context.browser)
  assert "Backoffice JogaJunto" in context.page.get_product_list_header().text

@then('receber a mensagem de sucesso "{message}"')
def step_receive_success_message(context, message):
  assert message in context.page.get_logged_in_sucessfully_message().text

# @when('tentar efetuar cadastro com o email inválido "{invalid_email}"')
# def step_fill_invalid_password(context, invalid_email):
#   context.page.fill_email(invalid_email)