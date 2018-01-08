from math import factorial, pi

print('Enter a number in radians')
x = int(input())

def cosine(x):
    for i in range (0, 16, 2):
        y = (-1)**i*x**(2*i)/factorial(i)
    return y

print('The value of your radian valueafter its factorial is ')
print(cosine(x))



