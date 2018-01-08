x = 10
def rec(n):
    first = 1
    rate = 3
    sum = 1
    print (first)
    for i in range(n-1):
        second = first * rate
        print (second)
        first = second
        z = first * rate
        sum = sum + second
    print ('Sum = ' + str(sum))
rec(x)
