class Calculadora:
  def add(self, a, b):
      return a + b

  def subtrai(self, a, b):
      return a - b

  def multiplica(self, a, b):
      return a * b

  def divide(self, a, b):
      if b == 0:
          raise ValueError("Não é possível dividir por 0!")
      return a / b
