import math

def taylor(x):
    series = 0
    for n in range(16):
        a = (-1)**n*x**(2*n)/(math.factorial(2*n))
        series = series + a
    return series

def deg_to_rad(deg):
    rad = deg * math.pi / 180
    return rad

print('Would you like your value to be evaluated in radians or degrees?')
print('Type "rad" for radians and "deg" for degrees')

select = input()
select = select.lower()

if select == "rad":
    x = float(input('Enter the radian value '))
elif select == "deg":
    x = float(input('Enter the degree value '))
    x = deg_to_rad(x)
else:
    quit()

print('The cosine of ' + str(x) + ' is: ')
print(taylor(x))


input()

    
