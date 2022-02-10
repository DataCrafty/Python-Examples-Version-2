a = 6
b = 2
try:
	print(a/b)
	a = int(input('enter an number'))
	print(a)
except Exception as e:
	print('this is invalid divison')
finally:
	print('here we done with ur code')
	print('resorce closed')