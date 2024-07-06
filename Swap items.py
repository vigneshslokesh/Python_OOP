
def swaplist(mylist):
    
    mylist[0],mylist[-1] = mylist[-1],mylist[0]
    return mylist

mylist = [1, 5, 6, 8, 11]

print(swaplist(mylist))