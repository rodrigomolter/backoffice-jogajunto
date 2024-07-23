from faker import Faker
import os

class Product:
  """
  Classe representando um produto com atributos gerados automaticamente ou fornecidos.

  Args:
    name (str, optional): Nome do produto. Se não fornecido, um nome falso será gerado.
    description (str, optional): Descrição do produto. Se não fornecida, uma descrição falsa será gerada.
    category (str, optional): Categoria do produto. Se não fornecida, uma categoria será selecionada.
    price (str, optional): Preço do produto. Se não fornecido, um preço falso será gerado.
    image (str, optional): Caminho da imagem do produto. Se não fornecido, uma imagem será selecionada.
    shipment (str, optional): Informações de remessa do produto. Se não fornecida, informações falsas serão geradas.
  """

  def __init__(
      self, 
      name: str = None, 
      description: str = None, 
      category: str = None, 
      price: str = None, 
      image: str = None, 
      shipment: str = None
      ) -> None:

    categories = [
      "Roupas",
      "Calçados",
      "Acessorios"
    ]
    images = [
      "bone.png",
      "camisa_amarela.png",
      "camisa_preta.png",
      "capa_celular_amarela.png",
      "casaco.png",
      "tenis_amarelo.png",
      "tenis_preto.png"
    ]

    fake = Faker("pt_BR")

    selected_image = fake.random_element(elements=images)
    IMAGES_PATH = os.path.abspath(f"./media/{selected_image}")

    self.name = name or fake.company()
    self.description = description or f"{fake.safe_color_name()} {fake.catch_phrase()} {fake.bs()}"
    self.category = category or fake.random_element(elements=categories)
    self.price = price or fake.random_int(min=1)
    self.image = image or IMAGES_PATH
    self.shipment = shipment or fake.random_int(min=1)
