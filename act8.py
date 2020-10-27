numbers = list(input("enter a set of numbers seperated by comma: ").split(","))
l = len(numbers)
print (numbers)
if (numbers[0]==numbers[l-1]):
    print (True)
else:
    print (False)
