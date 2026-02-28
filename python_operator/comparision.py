# Python Comparision Operator Learning Section.

a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= 10)  # True
print(b <= 3)   # False

# python chain comparision : a < b < c
# means : (a < b) and (b < c)



# questions practice section.

''' Operator Priority ''' 
 
print(10 > 5 == True)  # Output: False
print((10 > 5) == True)  # Output: True

''' boolean comparision '''
print(True == 1) # True
print(False == 0) # True

''' expression comparision '''
a = 8
b = 3
print(a * 2 >= b ** 2) # True

''' Multiple Comparisons '''
print(5 < 7 < 10) # True

''' Mixed Arithmetic + Comparison '''
x = 4
y = 6
print(x + y == x * y / 2) # False

''' Chained Comparison Logic '''
a = 5
print(1 < a < 10 < 7) # False

''' Type Comparison Trick '''
print(10 == 10.0) # True
print(10 is 10.0) # False

''' Boolean + Arithmetic Mix '''
x =  True
y =  False
print(x + 5 > y + 5) #True

''' Negative Number Comparison '''
print(-5 > -10) # True
print(-5 < -10) # False

''' Comparison Chain Expansion '''
print(4 > 3 == 3) # True

