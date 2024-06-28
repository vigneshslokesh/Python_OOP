# Question : The scond line consists of N space separated strings representing the first names of the people

# Output : Print a string in lowercase letters representing the name of the town of the given N people 
#          where the name of the town is the common substring and has the maximum length. 
#          If no such common prefix is found, then do not print anything.

def long_common_prefix(strs):
    if not strs:
        return "" #if there is no input of the string then it returns "empty"
    
    strs = [s.lower() for s in strs]
    strs.sort() #sorts the list in alphabetical order
    first = strs[0] #considers the first string in the array
    last = strs[-1] #considers the last string in the array 

    i=0 #index i initialized to 0
    while i<len(first) and i<len(last) and first[i]==last[i]: #the loop runs until the following statemengts become false
        # until i is less than the first string length and i is less than the last string length and the index value of the first and last string is similiar
        i+=1 #i is incremented and the index is moved to next position

    return first[:i] #once the statement becomes false the loop exits and the index i until which it is moved in first string is returned

n = int(input()) #no of string in the input
names = input().split() #splits the string i.e. "Alex Alice Alfred" ---> ['Alex','Alice','Alfred']

result = long_common_prefix(names)
print(result.lower()) #the answer (common prefix) returned in the lowercase 


