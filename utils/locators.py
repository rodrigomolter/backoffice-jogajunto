from selenium.webdriver.common.by import By

class RegisterPageLocators():
  """
  Locators da página de Registro de Usuário.
  """
  EMAIL = (By.NAME, "email")
  PASSWORD = (By.NAME, "password")
  PASSWORD_CONFIRMATION = (By.NAME, "confirmPassword")
  REGISTER_FORM = (By.TAG_NAME, "form")
  MESSAGE_INVALID_EMAIL = (By.XPATH, "//p[contains(.,'Digite um e-mail válido')]")
  MESSAGE_REGISTERED_SUCESSFULLY = (By.XPATH, "//span[@class='sucess']")

class LoginPageLocators():
  """
  Locators da página de Login.
  """
  EMAIL = (By.NAME, "email")
  PASSWORD = (By.NAME, "password")
  LOGIN_FORM = (By.TAG_NAME, "form")

class ProductPageLocators():
  """
  Locators da página de Produto.
  """
  PRODUCT_LIST_HEADER = (By.CSS_SELECTOR, "header>h1")
  MESSAGE_LOGGED_IN_SUCESSFULLY = (By.XPATH, "//div[@role='status'][contains(.,'logado com sucesso')]")
  PRODUCT_ADDED_SUCESSFULLY = (By.XPATH, "//div[@role='status'][contains(.,'Produto enviado com sucesso!!')]")
  NEW_PRODUCT_BTN = (By.CSS_SELECTOR, "header>button")
  INPUT_PRODUCT_NAME = (By.NAME, "name")
  INPUT_PRODUCT_DESCRIPTION = (By.NAME, "description")
  INPUT_PRODUCT_PRICE = (By.NAME, "price")
  INPUT_PRODUCT_IMAGE = (By.NAME, "image")
  INPUT_PRODUCT_SHIPMENT = (By.NAME, "shipment")
  NEW_PRODUCT_FORM = (By.TAG_NAME, "form")
  PRODUCTS_LIST = (By.XPATH, "//*[@id='root']/header/section[2]/div/div/div/div")