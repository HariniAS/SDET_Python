numbers = tuple((input("Enter a set of numbers seperated by comma: ").split(",")))
print ("Received tuple is: ", numbers)

print ("Numbers in the tuple that are divisible by 5: ")
for x in numbers:
    if(int(x)%5 == 0):
        print(x)
    else:
        continue
