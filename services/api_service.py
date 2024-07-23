import requests
from requests import Response
from models.product import Product
from models.user import User
from utils.utils import Utils

class ApiService:
  """
  Classe para serviços da API, incluindo criação de usuários, login e manipulação de produtos.
  """

  BASE_URL: str = Utils.get_api_url()

  def __init__(self) -> None:
    self.session = requests.Session()

  def update_session(self, token: str) -> None:
    """
    Atualiza o cabeçalho das requests adicionando/atualizando o Bearer token utilizado para a autenticação da API.
    Args:
      token (str): Token Bearer para autorização das requests.
    """
    self.session.headers.update({'Authorization': f'Bearer {token}'})

  def revogate_session(self) -> None:
    """
    Remove o Bearer token do cabeçalho, removendo a autenticação nas requests da API.
    """
    self.session.headers.pop('Authorization', None)

  def has_auth(self) -> bool:
    """
    Verifica se a session atual esta com o Bearer token no cabeçalho.

    Returns:
      bool: True se o cabeçalho de autorização estiver presente, False caso contrário.
    """
    return 'Authorization' in self.session.headers

  def close_session(self) -> None:
    """
    Fecha a sessão de requisições.
    """
    self.session.close()

  def create_user(self, data: dict) -> Response:
    """
    Cria um novo usuário na API.

    Args:
      data (dict): Dados do usuário a serem enviados para criação.

    Returns:
      Response: Resposta da requisição de criação do usuário.
    """
    url = f"{self.BASE_URL}/register"
    response = self.session.post(url, json=data)
    return response

  def login(self, data: dict) -> Response:
    """
    Realiza o login de um usuário na API.

    Args:
      data (dict): Dados de login a serem enviados.

    Returns:
      Response: Resposta da requisição de login.
    """
    url = f"{self.BASE_URL}/login"
    response = self.session.post(url, json=data)
    return response
  
  def create_product(self, product: Product) -> Response:
    """
    Cria um novo produto na API.

    Args:
      product (Product): Objeto Product contendo os dados do produto.

    Returns:
      Response: Resposta da requisição de criação do produto.
    """
    url = f"{self.BASE_URL}/"
    data = {
      "name": product.name,
      "description": product.description,
      "price": product.price,
      "category": product.category,
      "shipment": product.shipment
    } 
    files = {
      "image": open(product.image, "rb")
    }
    response = self.session.post(url, data=data, files=files)
    files['image'].close()
    return response

  def all_products(self) -> Response:
    """
    Obtém a lista de todos os produtos da API.

    Returns:
      Response: Resposta da requisição para obter todos os produtos.
    """
    url = f"{self.BASE_URL}/"
    response = self.session.get(url)
    return response
