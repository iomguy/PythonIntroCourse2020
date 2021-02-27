# расчёт обменного курса

class CurrencyConverter:  
  def __init__(self, currency_x = 1):
    self.currency_x = currency_x

  def currency_converter(self):
    currency_y = self.currency_x * 28
    return (currency_y)

c = CurrencyConverter()
c.currency_x = 2
print(c.currency_converter())

# хорошо, а если значение < 0?

# c = CurrencyConverter()
# c.currency_x = -2
# print(c.currency_converter())