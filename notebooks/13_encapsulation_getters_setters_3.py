class CurrencyConverter:
 
	def __init__(self, currency_x_input = 1):
		self._currency_x = currency_x_input

	def currency_converter(self):
		currency_y = self.get_currency_x() * 28
		return (currency_y)

	@property
	def currency_x(self):
		print ('inside getter method')
		return self._currency_x

	@currency_x.setter
	def currency_x(self, currency_value):
		if currency_value < 0:
 			raise ValueError("Currency can't be negative")
		print ('inside setter method')
		self._currency_x = currency_value

c = CurrencyConverter(2)
# print(c.currency_x)
# c.currency_x = 5
# print(c.currency_x)
# c.currency_x = -1
