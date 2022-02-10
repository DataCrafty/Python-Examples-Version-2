class mobile:
	def __init__(self):
		self.x1 = 10;
		print("hiii")
class nokia(mobile):
	def __init__(self):
		self.x1= 20;
		print("hello")
class vivo(nokia):
	def __init__(self):
		self.x1 = 40;
		print("hoo....")
		
class readme(vivo):
	pass

n = readme()
print(n.x1)



