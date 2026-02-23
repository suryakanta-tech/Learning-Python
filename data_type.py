# DATA TYPE LEARNING SECTION

x = 10        # number
name = "Ram"  # text

# int
a = 10
print(type(a)) # output = <class 'int'>

# float
b = 3.14
print(type(b)) # output = <class 'float'>

#string
c = "Surya"
print(type(c)) # output = <class 'str'>

# boolean
# boolean only two type 1.True,2.False
is_student = True
print(type(is_student)) # output = <class 'bool'>



# DATA TYPE QUESTIONS PRACTICE SECTION

# Q.1
# Create variables:
# age (int)
# height (float)
# name (string)
# student (boolean)

# Print their types.

age = 20
print(type(age))

height = 5.5
print(type(height))

name = "Surya"
print(type(name))

student = True
print(type(student))


# Q.2
# Convert "50" into integer and add 10.

a = int("50")
print(a+10) # 60


# Q.3
# Create a list of 5 numbers and print the 3rd number.

number_list = [10,20,30,40,50]
print(number_list[2]) # 30


# Q.4 
# Create dictionary: name → your name
                   # city → your city
                   # age → your age

my_info  = {
    "name":"Suryakanta",
    "city":"Bhubaneswar",
    "age" :20
}
print(my_info)
# now print only the name.
print(my_info["name"])
