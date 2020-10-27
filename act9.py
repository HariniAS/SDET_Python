list1 = [1,2,3,4,5]
list2 = list(input("Enter s set of numbers seperated by comma: ").split(","))
print ("list1 is: ", list1)
print ("list2 is: ", list2)
list3 = list()
for x in list1:
    if (int(x)%2 != 0):
        list3.append(x)
for y in list2:
    if (int(y)%2 == 0):
        list3.append(y)

print ("list 3 (odd numbers from list 1 & even numbers from list 2) is: ", list3)