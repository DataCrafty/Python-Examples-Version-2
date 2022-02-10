
#  single leading underscrore:_var is to give a hint to the other
#pogrammer that do not change the value/behaviour of this variable or method
class Test:
	def __init__(self):
		self.x = 31
		
		self.__y = 34
	def __str__(self):
		return "helo..."
	
t =Test()
print(t._Test__y)


pass_= 809
def_ =60

