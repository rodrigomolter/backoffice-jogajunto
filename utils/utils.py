import configparser
import json

config = configparser.ConfigParser()
CONFIG_FILE = 'behave.ini'

class Utils:
  """
  Classe utilitária contendo métodos estáticos para realizar atividades diversas.

  Methods:
    get_api_url: Obtém a URL da API a partir do arquivo de configuração.
    get_app_url: Obtém a URL da aplicação a partir do arquivo de configuração.
    json_to_dict: Converte um arquivo JSON em um dicionário.
  """

  @staticmethod
  def get_api_url() -> str:
    """
    Obtém a URL da API a partir do arquivo de configuração.

    Returns:
      str: URL da API.
    """
    config.read(CONFIG_FILE)
    return config.get('behave.userdata', 'api_url')

  @staticmethod
  def get_app_url() -> str:
    """
    Obtém a URL da aplicação a partir do arquivo de configuração.

    Returns:
      str: URL da aplicação.
    """
    config.read(CONFIG_FILE)
    return config.get('behave.userdata', 'base_url')
  
  @staticmethod
  def json_to_dict(path: str) -> dict:
    """
    Converte um arquivo JSON em um dicionário.

    Args:
      path (str): Caminho para o arquivo JSON.

    Returns:
      dict: Dicionário com o conteúdo do arquivo JSON.
    """
    file_path = f'./schemas/{path}'
    with open(file_path, 'r') as file:
      schema = json.load(file)
    return schema
