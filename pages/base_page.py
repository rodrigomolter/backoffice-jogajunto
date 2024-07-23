from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.utils import Utils
class BasePage():
  def __init__(self, webdriver, PATH) -> None:
    self.webdriver: webdriver = webdriver
    self.PATH: str = PATH
    self.BASE_URL: str = Utils.get_app_url()

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

  def delete_browser_data(self) -> None:
    self.open()
    self.webdriver.execute_script("window.localStorage.clear();")
