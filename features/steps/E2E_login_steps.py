from behave import given, when, then
from pages.login_page import LoginPage
from models.user import User
from pages.product_page import ProductPage

@given('que o usuário esteja na página de login')
def step_open_register_page(context):
  context.page = LoginPage(context.browser)
  context.page.delete_browser_data()

@when('digitar o email válido')
def step_fill_valid_email(context):
  context.user = User()
  context.api.create_user({"email": context.user.email, "password": context.user.password })
  context.page.fill_email(context.user.email)

@when('preencher com a senha válida')
def step_fill_valid_password(context):
  context.page.fill_password(context.user.password)

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
