# Python Operator Learning Section.


a = 47
b = 5

print(a+b) # addition
print(a-b) # substraction
print(a*b) # multiplication
print(a/b) # division
# division always give answers in a floating point number.
print(a//b) # floor division
# floor division always remove the decimal and give the answer in integer value.
print(a%b) # remainder
# gives the remainder.
print(a**b) # power



# Questions Practice section.

# Q.1
''' a = 15,b = 4
 Print:
 addition
 division
 floor division
 remainder '''

a = 15
b = 4
print("Addition: ",a + b)
print("Division: ",a / b)
print("Floor Division: ",a // b)
print("Remainder: ",a % b)

# Q.2
'''take a number from user and print its square using operator.'''

num = int(input("Enter your number: "))
print(num * num)

# Q.3
''' Check whether a number is even or odd.'''

num = int(input("Enter your number: "))
if num % 2 == 0:
  print(num, "is even")
else:
  print(num, "is odd")
  
# Q.4  
''' Take input from user: Enter hours
                          Enter minutes
                          Enter seconds '''


# Calculate total seconds using operators.

hour = int(input("Enter hours: "))
minute = int(input("Enter minutes: "))
second = int(input("Enter seconds: "))
# 1 min = 60 seconds
# 1 hour = 3600 seconds
print(hour * 3600 + minute * 60 + second,'seconds')

# Q.5
''' Take a number from user and print:
 whether number is EVEN or ODD.
 whether divisible by 5.'''
 
num = int(input("Enter your number: "))
if num % 2 == 0 and num % 5 == 0:
  print('This is an even number and divisible by 5.')
elif num % 2 != 0 and num % 5 ==0:
  print('This is an odd number and divisible by 5.')
elif num % 2 ==0 and num % 5 != 0:
  print('This is an even number and not divisible by 5.')
else:
  print('This is ann odd number and not divisible by 5.')
  
# Q.6
''' take: principle,rate,time 
And print the simple intrest (SI). '''

p = int(input("Enter principle: "))
t = int(input("Enter time: "))
r = float(input("Enter rate: "))
si = p * t * r
print("Simple intrest is: ",si)

# Q.7
''' swap these two variables value without using third variable. '''

a = 10
b = 20

a = a + b # a = 30
b = a - b # b = 10
a = a - b # a = 20

print("a = ",a) # a = 20
print("b = ",b) # b = 10

# Q.8
''' find the out put of this: 5 + 2 * 3 ** 2.'''

print(5 + 2 * 3 ** 2) # 23





