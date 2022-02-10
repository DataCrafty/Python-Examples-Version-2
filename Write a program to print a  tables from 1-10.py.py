def table ():
	for i in range(1,11):
		print('___') 
		for j in range(1,11):
			print(i,'x',j,'=',i*j)
table()


def reverse_s(n):
	n=str(n)
	reverse=n[::-1]
	if n==reverse:
		print("polindrome")

		
	else:
		print("not")
reverse_s('767')

			
	
def num(value):
	return(" ".join(value[::-1]))
print(num("1234"))


# def s(n):
# 	for each in n:
# 		print(n[::-1])
# s = ("9293")
# print(ecah,end = '  ')


# def palindrome(s):
# 	if(s==s[::-1]):
# 		print('ýes')
# 	else:
# 		print('no')
# palindrome(797)