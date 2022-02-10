#write a function to the polyndram number?
def s(n):
    a=(n[::-1])
    if a==n:
        print('enter the number is polyndram')
    else:
        print('enter the number is not polyndram')
n = input('enter the number to check polyndram or not..')
s(n)