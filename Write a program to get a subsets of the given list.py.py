# Write a program to get a subsets of the given list.
class list:
	def sortlist(self,given_list):
		return self.printsubsets([],sorted(given_list))
	def printsubsets(self,curr,given_list):
		if given_list:
			return self.printsubsets(curr,given_list[1:])+self.printsubsets(curr +[given_list[0]],given_list[1:])
		return [curr]
given_list = [2,4,3,5,7,4]
my_list = list()
print('subsets of the given list:',given_list,':')
print(list().sortlist(given_list)) 