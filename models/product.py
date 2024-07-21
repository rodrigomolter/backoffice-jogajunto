from faker import Faker
import os

class Product():
  def __init__(self, name: str = None, description: str = None, category: str = None, price: str = None, image: str = None, shipment: str = None) -> None:

    categories = [
      "Roupas",
      "Calçados",
      "Acessorios"
    ]
    IMAGES_PATH = os.path.abspath("./media")
    images = [
      "bone.png",
      "camise_amarela.png",
      "camise_preta.png",
      "capa_celular_amarela.png",
      "casaco.png",
      "tenis_amarelo.png",
      "tenis_preto.png"
    ]
    fake = Faker("pt_BR")
    self.name = name or fake.company()
    self.description = description or f"{fake.safe_color_name()} {fake.catch_phrase()} {fake.bs()}"
    self.category = category or fake.random_element(elements=categories)
    self.price = price or fake.random_int(min=1)
    self.image = image or f"{IMAGES_PATH}\{fake.random_element(elements=images)}"
    self.shipment = shipment or fake.random_int(min=1)
