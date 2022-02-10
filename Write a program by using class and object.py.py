	
class computer:
	def __init__(self):
		self.A = 20;
		print("enter a name")

class keyboard(computer):   
	def __init__(self):
		self.x1 = 10
		super().__init__()    #we are calling super class constructor with this statement 
a=keyboard()   # creating keyboard class object that is refered by 'a' reference variable then it invoke the kayboard class constructor 
print(a.A)
print(a.x1)      #we are calling instance variable with the "a" reference object.

