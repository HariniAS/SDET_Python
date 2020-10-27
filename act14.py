"""def fib(num):
    x=1
    y=1
    print (x)
    print (y)
    for i in range(2,num):
        if(i%2 ==0):
            x=x+y
            print (x)
        else:
            y=x+y
            print(y)

num=int(input("Enter the number of Fibonnaci numbers to generate: "))
fib(num)"""

def fib(num):
    if (num<=1):
        return num
    else:
        return (fib(num-1)+fib(num-2))

num = int(input("Enter the number of Fibonnaci numbers to generate: "))
for i in range(1,num):
    print(fib(i))
