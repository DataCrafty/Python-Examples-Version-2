#Find square of a given list of elements using pow ().
def lis(my_lis):
    for i in my_lis:
        l=[(i,pow(i,2))]
        print(l)
lis([1,2,3,4,5])
[(1, 1)]