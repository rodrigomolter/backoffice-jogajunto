from behave import given, when, then

@when('solicitar todos os produtos cadastrados')
def step_all_products_request(context):
  context.response = context.api.all_products()
