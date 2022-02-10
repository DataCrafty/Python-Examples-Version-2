#Write a program by removing the empty list
def my_list(lst):
    for i in lst:
        if i != []:
            print(i)
my_list([[1,2,3],[],['a','b','d'],[],['python']])