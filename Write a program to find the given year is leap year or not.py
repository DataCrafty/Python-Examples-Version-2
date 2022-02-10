#Finding leap year or not
year = int(input("enter the year :"))
def leap():
    if ((year%4 == 0)and(year%100 != 0)):
        print("%d is a leap year" % year)
    else:
        print("%d is not a leap year" % year)

leap()