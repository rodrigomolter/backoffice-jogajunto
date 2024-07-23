from selenium import webdriver
from pages.base_page import BasePage
from utils.locators import RegisterPageLocators

class RegisterPage(BasePage):
  """
  Classe representando a página de registro, com métodos para interação com o formulário de registro.

  Args:
    webdriver (WebDriver): Instância do WebDriver para controle do navegador.

  Attributes:
    locators (RegisterPageLocators): Localizadores dos elementos da página de registro.
  """
  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/register")
    self.locators = RegisterPageLocators

  def fill_email(self, email: str) -> None:
    """
    Preenche o campo de email no formulário de registro.
    """
    self.find_element(self.locators.EMAIL).send_keys(email)

  def fill_password(self, password: str) -> None:
    """
    Preenche o campo de senha no formulário de registro.
    """
    self.find_element(self.locators.PASSWORD).send_keys(password)

  def fill_password_confirmation(self, password: str) -> None:
    """
    Preenche o campo de confirmação de senha no formulário de registro.
    """
    self.find_element(self.locators.PASSWORD_CONFIRMATION).send_keys(password)

  def submit(self) -> None:
    """
    Submete o cadastro de um novo usuário
    """
    self.find_element(self.locators.REGISTER_FORM).submit()

  def fill_form(self, email: str, password: str) -> None:
    """
    Preenche o formulário de registro com email e senha.
    Preenche os campos:
      - Email
      - Senha
      - Confirmação de senha

    Args:
      email (str): Email a ser inserido no formulário.
      password (str): Senha a ser inserida no formulário.
    """
    self.fill_email(email)
    self.fill_password(password)
    self.fill_password_confirmation(password)

  def get_registered_sucessfully_message(self) -> str:
    """
    Obtém a mensagem de que o registro do novo usuário foi feito com sucesso

    Returns:
      str: A mensagem de registro realizado com sucesso.
    """
    return self.find_element(self.locators.MESSAGE_REGISTERED_SUCESSFULLY).text

  def get_invalid_email_message(self) -> str:
    """
    Obtém a mensagem de que o email utilizado no cadastro é inválido.

    Returns:
      str: A mensagem de email inválido.
    """
    return self.find_element(self.locators.MESSAGE_INVALID_EMAIL).text