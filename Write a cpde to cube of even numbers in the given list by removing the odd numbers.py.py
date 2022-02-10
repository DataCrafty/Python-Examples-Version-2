#Write a cpde to cube of even numbers in the given list by removing the odd numbers
def c(x):
    for i in x:
# here cubing values
        s = i**3
#which is cubed and it has to divisible by 2
        if s%2 == 0:
#print which is divisible by 2 after cubing values 
            print(s)
    
    
c((1,2,3,4,5,6,8))