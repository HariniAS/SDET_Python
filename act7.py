numbers = list ((input ("Enter 5 numbers seperated by comma: ").split(",") ))
print (numbers)
sum = 0
for x in numbers:
    sum = sum + int(x)
print ("Sum = ", sum)