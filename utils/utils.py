import configparser
import json

config = configparser.ConfigParser()
class Utils:
  
  def get_api_url() -> str:
    config.read('behave.ini')
    return config.get('behave.userdata', 'api_url')

  def get_app_url() -> str:
    config.read('behave.ini')
    return config.get('behave.userdata', 'base_url')
  
  def json_to_dict(path: str) -> dict:
    file_path = f'./schemas/{path}'
    with open(file_path, 'r') as file:
      schema = json.load(file)
    return schema