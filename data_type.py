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


#List(list)
names = ["Surya","Chandra","Basudev","Krishna"]
roll_no = [1,2,3,4]
print(names[3]) # output = Krishna
print(type(names))
print(type(roll_no))
# list is mutabel,means we can change the value of every current list value.
# example
names[3] = "Chandu"
print(names[3]) # output = Chandu


#Tuple(tuple)
names = ("Surya","Chandra","Basudev","Krishna")
roll_no = (1,2,3,4)
print(names[3]) # output = Krishna
print(type(names))
print(type(roll_no)) 
# tuple is just like list but we can not change the tuple value just like list,means tuple is imutable.


# Dictionary (dict)
# Stores data in key : value pair.
student_info = {
    "name":"Surya",
    "class":"xii",
    "roll_no":1,
    "stream":"science"
}
print(student_info)
print(student_info["name"]) # output = Surya
print(type(student_info))


# Type Conversion (Casting)
# Convert one type → another.
a = 3.00
b = int(a)
print(b) 
print(type(b)) # output = <class 'int'>

p = 10
q = float(p)
print(q) 
print(type(q)) # output = <class 'float'>

x = "10"
y = int(x)
print
print(type(y)) # output = <class 'int'>





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
