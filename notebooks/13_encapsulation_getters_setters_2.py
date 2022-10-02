class CurrencyConverter:
 
 def __init__(self, currency_x = 1):
   self.set_currency_x(currency_x)

 def currency_converter(self):
   currency_y = self.get_currency_x() * 28
   print(f"converted value is: {currency_y}")
   return (currency_y)

 #implementing new getter method
 def get_currency_x(self):
   print(self.currency_x)
   return(self.currency_x)

 #implementing new setter method
 def set_currency_x(self, currency_value):
   if currency_value < 0:
     raise ValueError("Currency can't be negative")
   self.currency_x = currency_value

# CurrencyConverter(-2)

c = CurrencyConverter(2)
# в геттере уже есть функционал вывода переменной
c.get_currency_x()
c.set_currency_x(3)
c.currency_converter()
c.set_currency_x(-4)
