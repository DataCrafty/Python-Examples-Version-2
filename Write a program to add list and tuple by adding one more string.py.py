 #Write a program to add list and tuple by adding one more string?
def s(list1,tuple2):
    return list1+"_"+tuple2
my_list = ['hi','how','u']
my_tuple =('chandu','r')
updated_list = map(s,my_list,my_tuple)
print(updated_list)
print(list(updated_list))