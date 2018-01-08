def function(n):
    y = n ** 2 + 3 * n + 1
    return y
acc = 0
for i in range(2,6):
    print(function(i))
    print ('+')
    acc = acc + function(i)

print (acc)
