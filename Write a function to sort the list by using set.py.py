#Write a function to sort the list by using set
def diff(lis1,lis2):   # using set  
    return list(set(lis1)-set(lis2))
lis1 = [1,2,3,4,5,6,9,67,45]
lis2 = [1,2,3,3,5,7,98]
print(diff(lis1,lis2))
