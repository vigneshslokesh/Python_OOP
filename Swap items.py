
def swaplist(mylist):
    
    mylist[0],mylist[-1] = mylist[-1],mylist[0]
    return mylist

input_str = input("Enter the list items: ")
mylist = [int(item) for item in input_str.split()]

print(swaplist(mylist))