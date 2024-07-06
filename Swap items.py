
def swaplist(mylist):
    
    mylist[0],mylist[-1] = mylist[-1],mylist[0]
    return mylist

input_str = input("Enter the list items: ")
mylist = [int(item) for item in input_str.split()]

print(swaplist(mylist))

#swap elements at given positions 

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))