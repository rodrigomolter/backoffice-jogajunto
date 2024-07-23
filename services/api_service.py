import requests
from requests import Response
from models.product import Product
from models.user import User
from utils.utils import Utils

class ApiService:
  BASE_URL: str = Utils.get_api_url()

  def __init__(self) -> None:
    self.session = requests.Session()

  def update_session(self, token: str) -> None:
    self.session.headers.update({'Authorization': f'Bearer {token}'})

  def revogate_session(self) -> None:
    self.session.headers.pop('Authorization', None)

  def has_auth(self) -> bool:
    return 'Authorization' in self.session.headers

  def close_session(self) -> None:
    self.session.close()

  def create_user(self, data: dict) -> Response:
    url = f"{self.BASE_URL}/register"
    response = self.session.post(url, json=data)
    return response
      
  def login(self, data: dict) -> Response:
    url = f"{self.BASE_URL}/login"
    response = self.session.post(url, json=data)
    return response
  
  def create_product(self, product: Product) -> Response:
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
    url = f"{self.BASE_URL}/"
    response = self.session.get(url)
    return response
