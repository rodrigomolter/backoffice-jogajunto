from selenium import webdriver
from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/")
    self.locators = LoginPageLocators

  def fill_email(self, email: str) -> None:
    self.find_element(self.locators.EMAIL).send_keys(email)

  def fill_password(self, password: str) -> None:
    self.find_element(self.locators.PASSWORD).send_keys(password)

  def submit(self) -> None:
    self.find_element(self.locators.LOGIN_FORM).submit()

  def login_by_ui(self, email: str, password: str) -> None:
    self.fill_email(email)
    self.fill_password(password)
    self.submit()

  def get_alert(self) -> str:
    ...
    
  def is_auth(self, email: str) -> bool:
    ...