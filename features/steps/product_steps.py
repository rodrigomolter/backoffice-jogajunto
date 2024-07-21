from behave import given, when, then
from pages.product_page import ProductPage
from models.product import Product

@given('que usuário esteja na página de cadastro')
def step_open_product_page(context):
  context.page = ProductPage(context.browser)
  context.page.open()
  context.page.open_add_product_modal()

@when('adicionar informações de produto na categoria "{category}"')
def step_fill_product_form(context, category):
  context.page.fill_product_form(Product(category=category))

@when('clicar em enviar novo produto')
def step_submit_new_product(context):
  context.page.submit_form()

@then('deve ser criado visualização de novo produto na home page')
def step_assert_new_product_in_product_list(context):
  ...