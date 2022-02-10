#  by using def  function
# reverse of the pattern 
def star(row):
    for i in range((row+1)-1,-1,-1):
        print(' * '*i)
        print()
star(6)