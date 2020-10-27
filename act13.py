def sum(num):
    s=0
    for x in num:
        s=s+int(x)
    return s



num = list(input("Enter a few numbers for the list, seperated by comma: ").split(","))
print (num)
print (sum(num))