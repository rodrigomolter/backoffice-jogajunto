from selenium.webdriver.common.by import By

class RegisterPageLocators():
  EMAIL = (By.NAME, "email")
  PASSWORD = (By.NAME, "password")
  PASSWORD_CONFIRMATION = (By.NAME, "confirmPassword")
  REGISTER_FORM = (By.TAG_NAME, "form")
  MESSAGE_INVALID_EMAIL = (By.XPATH, "//p[contains(.,'Digite um e-mail válido')]")
  MESSAGE_REGISTERED_SUCESSFULLY = (By.XPATH, "//span[@class='sucess']")