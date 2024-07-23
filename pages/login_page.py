from selenium import webdriver
from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from models.user import User
from services.api_service import ApiService

class LoginPage(BasePage):
  """
  Classe representando a página de login, com métodos para interação com o formulário de login.
  
  Args:
    webdriver (WebDriver): Instância do WebDriver para controle do navegador.

  Attributes:
    locators (LoginPageLocators): Localizadores dos elementos da página de login.
  """
  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/")
    self.locators = LoginPageLocators

  def fill_email(self, email: str) -> None:
    """
    Preenche o campo de email no formulário de login.

    Args:
      email (str): Email a ser inserido no campo de email.
    """
    self.find_element(self.locators.EMAIL).send_keys(email)

  def fill_password(self, password: str) -> None:
    """
    Preenche o campo de senha no formulário de login.

    Args:
      password (str): Senha a ser inserida no campo de senha.
    """
    self.find_element(self.locators.PASSWORD).send_keys(password)

  def submit(self) -> None:
    """
    Submete o formulário de login.
    """
    self.find_element(self.locators.LOGIN_FORM).submit()

  def login_by_ui(self, email: str, password: str) -> None:
    """
    Realiza o login através da interface do usuário.

    Args:
      email (str): Email do usuário para realizar login.
      password (str): Senha do usuário para realizar login.
    """
    self.fill_email(email)
    self.fill_password(password)
    self.submit()

  def login_by_api(self, data: dict, api: ApiService) -> None:
    """
    Realiza o login através da API e salva a session (jwt token) no local storage.

    Args:
      data (dict): Dados de login do usuário.
      api (ApiService): Instância do serviço de API.
    """

    token: str = api.login(data).json()["token"]
    self.webdriver.execute_script('localStorage.setItem("auth", "true")')
    email = data['email']
    self.webdriver.execute_script(f'localStorage.setItem("user", "\\"{email}\\"")')
    self.webdriver.execute_script(f'localStorage.setItem("jwt", "{token}")')

  def create_and_login_by_api(self, data: dict, api: ApiService) -> None:
    """
    Cria um novo usuário e realiza o login através da API, salvando a session (jwt token) no local storage.

    Args:
      data (dict): Dados do novo usuário a ser criado.
      api (ApiService): Instância do serviço de API para criação de usuário e autenticação.
    """
    api.create_user(data)
    self.login_by_api(data, api)