from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.locators import ProductPageLocators
from models.product import Product

class ProductPage(BasePage):
  def __init__(self, webdriver: webdriver) -> None:
    super().__init__(webdriver, PATH="/products")
    self.locators = ProductPageLocators

  def open_add_product_modal(self) -> None:
    self.find_element(self.locators.NEW_PRODUCT_BTN).click()

  def fill_product_name(self, name: str) -> None:
    self.find_element(self.locators.INPUT_PRODUCT_NAME).send_keys(name)

  def fill_product_description(self, description: str) -> None:
    self.find_element(self.locators.INPUT_PRODUCT_DESCRIPTION).send_keys(description)
    
  def fill_product_category(self, category: str) -> None:
    self.find_element((By.XPATH, f"//input[@name='category'][@value='{category}']/ancestor::label")).click()

  def fill_product_price(self, price: str) -> None:
    self.find_element(self.locators.INPUT_PRODUCT_PRICE).send_keys(price)

  def fill_product_image(self, image: str) -> None:
    self.find_element(self.locators.INPUT_PRODUCT_IMAGE).send_keys(image)

  def fill_product_shipment(self, shipment: str) -> None:
    self.find_element(self.locators.INPUT_PRODUCT_SHIPMENT).send_keys(shipment)

  def submit_form(self) -> None:
    self.find_element(self.locators.NEW_PRODUCT_FORM).submit()

  def fill_product_form(self, product: Product) -> None:
    self.fill_product_name(product.name)
    self.fill_product_description(product.description)
    self.fill_product_category(product.category)
    self.fill_product_price(product.price)
    self.fill_product_image(product.image)
    self.fill_product_shipment(product.shipment)

  def get_product_list_header(self) -> WebElement:
    return self.find_element(self.locators.PRODUCT_LIST_HEADER)
  
  def get_logged_in_sucessfully_message(self) -> WebElement:
    return self.find_element(self.locators.MESSAGE_LOGGED_IN_SUCESSFULLY)