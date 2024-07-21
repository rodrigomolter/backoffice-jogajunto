from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import configparser

class BasePage():
  def __init__(self, webdriver, PATH) -> None:
    self.webdriver: webdriver = webdriver
    self.PATH: str = PATH
    # self.BASE_URL: str = configparser.ConfigParser().read('behave.ini').get('behave.userdata', 'base_url')
    self.BASE_URL: str = "https://projetofinal.jogajuntoinstituto.org"


  def find_element(self, locator: tuple[By, str]) -> WebElement:
    self.wait_element(locator)
    return self.webdriver.find_element(*locator)

  def find_elements(self, locator: tuple[By, str]) -> list[WebElement]:
    self.wait_element(locator)
    return self.webdriver.find_elements(*locator)
  
  def open(self) -> None:
    self.webdriver.get(str(self.BASE_URL + self.PATH))

  def wait_element(self, locator: tuple[By, str], timeout: float = 10) -> None:
    try:
        WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
