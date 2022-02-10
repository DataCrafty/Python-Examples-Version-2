 #Write a program to add two lists by using map function and outpit should be in the tuple
def s(list1, list2):
    return list1+list2

my_list1 = [2,3,4,5,6,7,8,9]
my_list2 = [4,8,12,16,20,24,28]

updated_list = map(s, my_list1,my_list2)
print(updated_list)
print(tuple(updated_list))
