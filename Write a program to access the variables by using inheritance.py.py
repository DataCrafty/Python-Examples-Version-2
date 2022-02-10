class car:
	def __init__(self):
		self.x = 10;
		print('car object')
class bmw(car):
	def __init__(self):
		self.x = 20;
		print('bmw object')
class bmw_3_series(bmw):
	pass
class bmw_7_series(bmw):
	def __init__(self):
		self.x = 30;
		super().__init__();
		print('bmw_7_series object')
class benz(car):
	def __init__(self):
		print('benz object')
		self.x = 40
		super().__init__();
class test(benz,bmw_7_series,bmw_3_series):
	def __init__(self):
		self.x = 50
		super().__init__();

		print('test object')
t = test()
print(t.x)	
