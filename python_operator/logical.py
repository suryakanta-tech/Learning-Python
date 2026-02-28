# Python Logical Operator Learning Section.

# 'and' Operator

# Both conditions must be True
age = 20
print(age > 18 and age < 35) # True

'''
True and True = True
True and False = False
False and True = False
False and False = False

'''


# 'or' Operator

# only one condition must be True
age = 20
print(age > 18 or age < 10) # True

'''
True or True = True
True or False = True
False or True = True    
False or False = False

'''


# 'not' Operator

# reversed the result
age = 20
print(not age > 18) # False



# Queations practice section.

# 1.
print(10 > 5 and 3 < 1) # False
# 2.
print(7 == 7 or 5 > 10) # True

# 3.
print(not(8 > 3)) # False
# 4.
age = 17
print(age >= 18 and age <= 60) # False
# 5.
print(True or False and False) # True
