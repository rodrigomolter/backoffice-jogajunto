from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import ProductPageLocators
from models.product import Product

class ProductPage(BasePage):
  """
  Classe representando a página de produtos, com métodos para interação com o formulário de adição de produtos.

    Args:
      webdriver (WebDriver): Instância do WebDriver para controle do navegador.

    Attributes:
      locators (ProductPageLocators): Localizadores dos elementos da página de produtos.
  """

  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/products")
    self.locators = ProductPageLocators

  def open_add_product_modal(self) -> None:
    """
      Abre o modal de adição de novo produto, clicando no botão "+ Adicionar".
    """
    self.find_element(self.locators.NEW_PRODUCT_BTN).click()

  def close_add_product_modal(self) -> None:
    """
    Fecha o modal de adição de novo produto, pressionando a tecla "ESC"
    """
    ActionChains(self.webdriver).send_keys(Keys.ESCAPE).perform()

  def fill_product_name(self, name: str) -> None:
    """
    Preenche o campo de nome do produto dentro da modal de adicionar novo produto.
    """
    self.find_element(self.locators.INPUT_PRODUCT_NAME).send_keys(name)

  def fill_product_description(self, description: str) -> None:
    """
    Preenche o campo de descrição do produto dentro da modal de adicionar novo produto.
    """
    self.find_element(self.locators.INPUT_PRODUCT_DESCRIPTION).send_keys(description)
    
  def fill_product_category(self, category: str) -> None:
    """
    Seleciona o radio button da categoria do produto dentro da modal de adicionar novo produto.
    As opções são:
      - Roupas
      - Calçados
      - Acessorios
    """
    self.find_element((By.XPATH, f"//label[contains(.,'{category}')]")).click()

  def fill_product_price(self, price: str) -> None:
    """
    Preenche o campo de preço do produto dentro da modal de adicionar novo produto.
    """
    self.find_element(self.locators.INPUT_PRODUCT_PRICE).send_keys(price)

  def fill_product_image(self, image: str) -> None:
    """
    Preenche o campo de imagem do produto dentro da modal de adicionar novo produto com o PATH da imagem.
    """
    self.find_element(self.locators.INPUT_PRODUCT_IMAGE).send_keys(image)

  def fill_product_shipment(self, shipment: str) -> None:
    """
    Preenche o campo de frete do produto dentro da modal de adicionar novo produto.
    """
    self.find_element(self.locators.INPUT_PRODUCT_SHIPMENT).send_keys(shipment)

  def submit_form(self) -> None:
    """
    Submete o cadastro de um novo produto.
    """
    self.find_element(self.locators.NEW_PRODUCT_FORM).submit()

  def fill_product_form(self, product: Product) -> None:
    """
    Preenche todos os campos  do formulário de adição de produto com os dados do produto.

    Args:
      product (Product): Product contendo as informações do produto.
    """
    self.fill_product_name(product.name)
    self.fill_product_description(product.description)
    self.fill_product_category(product.category)
    self.fill_product_price(product.price)
    self.fill_product_image(product.image)
    self.fill_product_shipment(product.shipment)

  def get_product_list_header(self) -> WebElement:
    """
    Obtém o cabeçalho da lista de produtos, com o texto "Backoffice JogaJunto".

    Returns:
      WebElement: O elemento Web do cabeçalho da lista de produtos.
    """
    return self.find_element(self.locators.PRODUCT_LIST_HEADER)
  
  def get_logged_in_sucessfully_message(self) -> WebElement:
    """
    Obtém o alert de login realizado com sucesso, no canto superior direito da página.

    Returns:
      WebElement: O elemento Web da mensagem de login realizado com sucesso.
    """
    return self.find_element(self.locators.MESSAGE_LOGGED_IN_SUCESSFULLY)

  def get_product_added_sucessfully_message(self) -> WebElement:
    """
    Obtém o alert de produto enviado com sucesso, no canto superior direito da página.

    Returns:
      WebElement: O elemento Web da mensagem de login realizado com sucesso.
    """
    return self.find_element(self.locators.PRODUCT_ADDED_SUCESSFULLY)

  def get_products_list(self) -> list[WebElement]:
    """
    Obtém a lista de todos os produtos que estão sendo exibidos.

    Returns:
      list[WebElement]: Lista de elementos Web dos produtos.
    """
    return self.find_elements(self.locators.PRODUCTS_LIST)

  def get_all_products_names(self) -> list[str]:
    """
    Obtém a lista dos nomes de todos os produtos que estão sendo exibidos.

    Returns:
      list[str]: Lista de nomes dos produtos.
    """
    names = [product.find_element(By.TAG_NAME, "h1").text for product in self.get_products_list()]
    return names
