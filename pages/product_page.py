from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from utils.locators import ProductPageLocators

class ProductPage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/products")
    self.locators = ProductPageLocators

  def get_product_list_header(self) -> WebElement:
    return self.find_element(self.locators.PRODUCT_LIST_HEADER)
  
  def get_logged_in_sucessfully_message(self) -> WebElement:
    return self.find_element(self.locators.MESSAGE_LOGGED_IN_SUCESSFULLY)