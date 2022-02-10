#Write a code by using union method as well as sort the elements in the given sets
def s(x,y,z):
    return x,y
x = {'d','a','s','f','e'}
y = {'c','x','w','f'}
z = {'a','s','d','k','g'}
​
s = x.union(y,x)
print(sorted(s))