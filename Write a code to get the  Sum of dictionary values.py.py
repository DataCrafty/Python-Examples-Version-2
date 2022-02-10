#Sum of dictionary values?
def sum_dict(dict):
    sum = 0
    for i in dict.values():
        sum=sum+i
    return sum 
dict={'ani':120,'pandu':200,'chandu':300}
print('Sum :',sum_dict(dict))