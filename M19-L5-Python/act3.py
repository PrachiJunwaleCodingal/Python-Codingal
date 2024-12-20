#Maths Operators

import math 
print('The Floor value of 10.5 is : ', str(math.floor(10.5)))
print('The Ceiling value of 10.5 is : ', str(math.ceil(10.5)))


x = 12
y = -16

print('The value of x after copying the sign from y is: ' + str(math.copysign(x,y)))

print('Absolute value of -10 and 20 are:' + str(math.fabs(-10)) + ', ' +str(math.fabs(20)))

print('The GCD of 24 and 56 : ' +str(math.gcd(24, 56)))