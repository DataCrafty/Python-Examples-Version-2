#Using count and zip function
given_string = input('enter some strings:')
list_string = given_string.split()
freqwords = [list_string.count(c)]
for c in list_string:
	result_dict = dict(zip(list_string,freqwords))
print(result_dict)