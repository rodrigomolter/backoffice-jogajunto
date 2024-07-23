from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.utils import Utils
class BasePage():
  """
  Classe base para todas as páginas, fornecendo métodos comuns de interação com elementos da página.

  Attributes:
      webdriver (WebDriver): Instância do WebDriver para controle do navegador.
      PATH (str): Caminho relativo da URL da página.
      BASE_URL (str): URL base da aplicação obtida via Utils.
  """
  def __init__(self, webdriver, PATH) -> None:
    self.webdriver: webdriver = webdriver
    self.PATH: str = PATH
    self.BASE_URL: str = Utils.get_app_url()

  def find_element(self, locator: tuple[By, str]) -> WebElement:
    """
    Encontra um elemento na página baseado no seu locator.

    Args:
        locator (tuple[By, str]): Localizador do elemento (By, valor).

    Returns:
        WebElement: O elemento Web encontrado.
    """
    self.wait_element(locator)
    return self.webdriver.find_element(*locator)

  def find_elements(self, locator: tuple[By, str]) -> list[WebElement]:
    """
    Encontra todos os elementos disponíveis na página com base no locator.

    Args:
        locator (tuple[By, str]): Localizador dos elementos (By, valor).

    Returns:
        list[WebElement]: Lista de elementos Web encontrados.
    """
    self.wait_element(locator)
    return self.webdriver.find_elements(*locator)
  
  def open(self) -> None:
    """
    Abre a URL da página.
    """
    self.webdriver.get(str(self.BASE_URL + self.PATH))

  def wait_element(self, locator: tuple[By, str], timeout: float = 10) -> None:
    """
    Espera até que o elemento esteja presente na página.

    Args:
        locator (tuple[By, str]): Localizador do elemento (By, valor).
        timeout (float): Tempo máximo de espera em segundos. Padrão é 10 segundos.

    Raises:
        TimeoutException: Se o elemento não for encontrado dentro do tempo especificado.
    """
    try:
        WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))

  def delete_browser_data(self) -> None:
    """
      Abre a página e limpa os dados do localStorage.
      Não exclui os cookies.
    """
    self.open()
    self.webdriver.execute_script("window.localStorage.clear();")
