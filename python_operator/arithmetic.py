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
# a = 15,b = 4
# Print:
# addition
# division
# floor division
# remainder

a = 15
b = 4
print("Addition: ",a + b)
print("Division: ",a / b)
print("Floor Division: ",a // b)
print("Remainder: ",a % b)

# Q.2
# take a number from user and print its square using operator.

num = int(input("Enter your number: "))
print(num * num)

# Q.3
# Check whether a number is even or odd.

num = int(input("Enter your number: "))
if num % 2 == 0:
  print(num, "is even")
else:
  print(num, "is odd")






