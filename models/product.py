from faker import Faker
import os

fake = Faker("pt_BR")
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
    
    product = self.random_product()

    self.name = name or product['name']
    self.description = description or product['description']
    self.category = category or product['category']
    self.price = price or product['price']
    self.image = image or product['image']
    self.shipment = shipment or product['shipment']

  def random_product(self) -> dict:
    products = [
      {
        "name": ["Boné", "Chapéu", "Gorra", "Cap"],
        "description": ["Um boné estiloso", "Chapéu confortável", "Gorra descolada", "Cap moderno"],
        "category": "Acessorios",
        "image": "bone.png"
      },
      {
        "name": ["Camisa Amarela", "Blusa Amarela", "Camiseta Amarela", "Top Amarelo"],
        "description": ["Camisa de algodão amarela", "Blusa leve e fresca", "Camiseta vibrante", "Top para o verão"],
        "category": "Roupas",
        "image": "camisa_amarela.png"
      },
      {
        "name": ["Camisa Preta", "Blusa Preta", "Camiseta Preta", "Top Preto"],
        "description": ["Camisa básica preta", "Blusa clássica preta", "Camiseta essencial", "Top elegante"],
        "category": "Roupas",
        "image": "camisa_preta.png"
      },
      {
        "name": ["Capa de Celular Amarela", "Capinha Amarela", "Proteção de Celular Amarela", "Case Amarelo"],
        "description": ["Capa de celular resistente", "Capinha colorida e protetora", "Proteção amarela para o seu celular", "Case brilhante"],
        "category": "Acessorios",
        "image": "capa_celular_amarela.png"
      },
      {
        "name": ["Casaco", "Jaqueta", "Blazer", "Sobretudo"],
        "description": ["Casaco quente para o inverno", "Jaqueta confortável", "Blazer elegante", "Sobretudo para dias frios"],
        "category": "Roupas",
        "image": "casaco.png"
      },
      {
        "name": ["Tênis Amarelo", "Tênis Esportivo Amarelo", "Shoe Amarelo", "Tênis Casual Amarelo"],
        "description": ["Tênis esportivo vibrante", "Shoe amarelo para atividades físicas", "Tênis casual confortável", "Tênis para o dia a dia"],
        "category": "Calçados",
        "image": "tenis_amarelo.png"
      },
      {
        "name": ["Tênis Preto", "Tênis Esportivo Preto", "Shoe Preto", "Tênis Casual Preto"],
        "description": ["Tênis esportivo básico", "Shoe preto versátil", "Tênis casual para todas as ocasiões", "Tênis elegante e discreto"],
        "category": "Calçados",
        "image": "tenis_preto.png"
      }
    ]
    random = fake.random_element(elements=products)
    
    product = {
        "name": f"{fake.random_element(elements=random['name'])} de {fake.bairro()}",
        "description": fake.random_element(elements=random['description']),
        "category": random['category'],
        "price": fake.random_int(min=1),
        "image": os.path.abspath(f"./media/{random['image']}"),
        "shipment": fake.random_int(min=1)
    }
    return product