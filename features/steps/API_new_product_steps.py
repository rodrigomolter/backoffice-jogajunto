from behave import given, when, then
from models.product import Product

@given('que o usuário esteja autenticado')
def step_user_is_auth(context):
  assert context.api.has_auth()

@when('o usuário cadastra um novo produto com informações válidas')
def step_new_product_request(context):
  context.product = Product()
  context.response = context.api.create_product(context.product)
