from selenium import webdriver
from pages.base_page import BasePage
from utils.locators import RegisterPageLocators

class RegisterPage(BasePage):

  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/register")
    self.locators = RegisterPageLocators

  def fill_email(self, email: str) -> None:
    self.find_element(self.locators.EMAIL).send_keys(email)

  def fill_password(self, password: str) -> None:
    self.find_element(self.locators.PASSWORD).send_keys(password)

  def fill_password_confirmation(self, password: str) -> None:
    self.find_element(self.locators.PASSWORD_CONFIRMATION).send_keys(password)

  def submit(self) -> None:
      self.find_element(self.locators.REGISTER_FORM).submit()

  def fill_form(self, email: str, password: str) -> None:
    self.fill_email(email)
    self.fill_password(password)
    self.fill_password_confirmation(password)

  def registered_sucessfully(self) -> str:
    return self.find_element(self.locators.MESSAGE_REGISTERED_SUCESSFULLY).text

  def invalid_email_message(self) -> str:
    return self.find_element(self.locators.MESSAGE_INVALID_EMAIL).text

  def register_by_api(self, email: str = None, password: str = None) -> None:
    ...
