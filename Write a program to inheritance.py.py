class car1:
	def m (self):
		#self.x1 = 'chandu'
		print ('its my car..')
class car2(car1):
	def m (self):
		#self.x2 = 50;
		print('its my car cost..')
class car3(car2):
	def m (self):
		#self.x3 = 20;
		print('this is new car..')
class car4(car2,car3):
	pass
n = class3()
n = m()

