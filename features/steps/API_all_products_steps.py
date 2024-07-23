from behave import given, when, then
from jsonschema import validate
from utils.utils import Utils

@when('solicitar todos os produtos cadastrados')
def step_all_products_request(context):
  context.response = context.api.all_products()

@then('o schema da resposta deve ser valido')
def step_response_must_have_valid_schema(context):
  validate(instance=context.response.json(), schema=Utils.json_to_dict("products_list_response.json"))