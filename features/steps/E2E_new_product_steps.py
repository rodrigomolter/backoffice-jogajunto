from behave import given, when, then
from jsonschema import validate
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from models.product import Product
from models.user import User
from utils.utils import Utils

@given('que usuário esteja na página de cadastro')
def step_open_product_page(context):
  login_page = LoginPage(context.browser)
  login_page.delete_browser_data()
  context.user = User()
  data = {
      "email": context.user.email,
      "password": context.user.password
    }
  validate(instance=data, schema=Utils.json_to_dict("user_request.json"))
  login_page.create_and_login_by_api(data, context.api)

  context.page = ProductPage(context.browser)
  context.page.open()
  context.page.open_add_product_modal()

@when('adicionar informações de produto na categoria "{category}"')
def step_fill_product_form(context, category):
  context.product = Product(category=category)
  context.page.fill_product_form(context.product)

@when('clicar em enviar novo produto')
def step_submit_new_product(context):
  context.page.submit_form()

@then('deve ser criado visualização de novo produto na home page')
def step_assert_new_product_in_product_list(context):
  context.page.close_add_product_modal()
  context.page.get_product_added_sucessfully_message()
  products = context.page.get_all_products_names()
  assert products[-1] == context.product.name
