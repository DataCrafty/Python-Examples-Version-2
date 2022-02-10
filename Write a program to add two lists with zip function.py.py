#Write a program to add two lists with zip function
def func(lst1,lst2):
    for x,y in zip(lst1,lst2):
        print(x+y,end =' ')
func(['m','na','i','chan'],['y','me','s','dra'])