# operators in python

# 1.Arithmetic Operator
a,b,c = 10,5,2

# addition
sum = a+b
print("Sum:",sum)
# substraction
difference = a-b
print("Difference:",difference)
# multiplication
product = a*b
print("Product:",product)
# division
division = a/b
print("Division:",division)
# mudulus
remainder = b%c
print("Remainder:",remainder)
# exponent
exponent = b**c
print("Exponent:",exponent)
# floor division
FloorDiv = b//c
print("Floor Division:",FloorDiv)


# 2.Comparison operator

a,b = 10,5

# equal to 
print("a = b is",(a == b))
# not equal to 
print("a != b is",(a != b))
# greater than
print("a > b is",(a > b))
# greater than or equal to 
print("a >= b is",(a >= b))
# less than
print("a < b is",(a < b))
# less than or equal to 
print("a <= b is",(a <= b))


# 3.Assignment operator

a,b = 10,5
a += b
print(a)

a,b = 10,5
a -= b
print(a)

a,b = 10,5
a *= b
print(a)

a,b = 10,5
a /= b
print(a)

a,b = 5,2
a %= b
print(a)

a,b = 5,2
a **= b
print(a)

a,b = 5,2
a //= b
print(a)


# 4.Bitwise Operator

a,b = 60,2
# binary AND
print(a & b)
# binary OR
print(a | b)
# binary XOR
print(a ^ b)
# binary ones complement
print(~ a)
# binary left shift
print(a >> b)
# binary right shift
print(a << b)


# 5.Logical operator

a,b,c,d = 10,5,2,1
# logical and
print((a > b) and (c > d))
# logical or
print((a > b) or (d > c))
# logical not
print(not(a > b))


# 6.Membership Operator

name = "Surya"
print("r" in name)
print("T" in name)
print("T" not in name)


# 7.Identity Operator

a,b,c = 10,10,5

print(a is b)
print(a is c)
print(a is not b)
