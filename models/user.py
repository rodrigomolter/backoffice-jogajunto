from faker import Faker

class User():
  def __init__(self, email: str = None, password: str = None) -> None:
    fake = Faker()
    self.email = email or fake.email()
    self.password = password or fake.password()
