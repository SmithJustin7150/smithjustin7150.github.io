from math import factorial, pi

print('Enter in a value for degrees')
x = float(input())

def cosine(x):
    for i in rnage (0, 16, 2):
        y = (-1)**i*x**(2*i)/factorial(i)
    return y

def deg_rad(deg):
    rad = deg * pi / 180
    return rad

print('The value of your degree value converted to radians is ')
print(deg_rad(x))
