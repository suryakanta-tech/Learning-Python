# 'if-else' Condition/Statement

# 'if' Condition Practice Section

# syntax
''' if statement:
     code '''

# How Python Reads It
'''
if condition is True - run the code
if condition is False - skip the code
'''
# example.1 (if condition is True)
age = 20
if age >= 18:
  print("You can drive a bike.")

# example.2 (if condition is false)
age = 16
if age >= 18:
  print("You can drive a bike.")


# Questions Practice Section

# Q.1
''' Create a program: number = 50
print "Big number" if number > 40 '''

number = 50
if number > 40:
  print("Big number.")
  
  
  
# 'if-else' Condition Practice Section

# syntax
''' if statement:
    code_if_true
else:
    code_if_false '''

# example
num = 75
if num % 2 == 0:
  print("Even")
else:
  print("Odd")


# Questions Practice Section

# Q.1
''' Create program: marks = 60
print Pass if marks ≥ 40 otherwise Fail '''

marks = 60
if marks >= 40:
  print("Pass")
else:
  print("Fail")
  
  
  
  # 'elif' Statement (Multiple Decisions)

# Syntax
''' if statement:
      code_if_true
    elif statement:
      code_if_true
    elif statement:
      code_if_true
    else:
      code_if_false '''

# Python checks top → bottom. First TRUE condition runs.

# Example.1 - Marks Grade System
marks = 92
if marks >=90:
  print("Grade A,Pass")
elif marks >= 80:
  print("Grade B,Pass")
elif marks >= 70:
  print("Grade C,Pass")
elif marks >= 60:
  print("Grade D,Pass")
elif marks >= 40:
  print("Grade E,Pass")
else:
  print("Grade F,Fail")

# Example.2 — Number Check
number = 0
if number > 0:
  print("Positive Number")
elif number < 0:
  print("Negative Number")
else:
  print("Zero")


# Questions Practice Section

# Q.1
''' Create program: temperature = 35
        Print:
          "Cold" if < 15
          "Normal" if 15–30
          "Hot" otherwise '''

temperature = 35
if temperature < 15:
  print("Cold")
elif temperature >= 15 and temperature <= 30:
  print("Normal")
else:
  print("Hot")

# Q.2
''' Take number from user and check this number is divisible by 3 and 5 or not. '''

num = 61
if num % 3 == 0 and num % 5 == 0:
  print("Divisible by both 3 and 5.")
elif num % 3 == 0:
  print("Divisible by 3.")
elif num % 5 == 0:
  print("Divisible by 5.")
else:
  print("Not Divisible.")



