x = 10
def fib(n):
    first = 1
    second = 1
    sum = 2
    print (first)
    print (second)
    for i in range(n-2):
        third = first + second
        print (third)
        first = second
        second = third
        sum = sum + third
    print ('Sum = ' + str(sum))

fib(x)
