#print prime numbers between 100 to 200
for num in range(100,200):
    if all(num%i != 0 for i in range(2,num)):
        print(num)

#write a sortin function without using the list.sort function(descending order)
list = [1,22, 16, 16,45, 8]

newlist = []

while list:
    min = l[0]
    for x in list:
        if x > min:
            min = x
    newlist.append(min)
    list.remove(min)

print(newlist)        