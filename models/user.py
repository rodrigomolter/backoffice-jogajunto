from faker import Faker

class User():
  """
  Classe representando um usuário com email e senha gerados automaticamente ou fornecidos.

   Args:
    email (str, optional): Email do usuário. Se não fornecido, um email fictício será gerado.
    password (str, optional): Senha do usuário. Se não fornecida, uma senha fictícia será gerada.
  """
  def __init__(self, email: str = None, password: str = None) -> None:
    fake = Faker("pt_BR")
    self.email = email or fake.email()
    self.password = password or fake.password()
