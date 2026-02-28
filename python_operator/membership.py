# membership operator

# 1. 'in' operator
fruit = "apple"
print('a' in fruit) # True
print('z' in fruit) # False

fruits_list = ['apple','banana','guava','grapes','watermelon']
print('guava' in fruits_list) # True
print('jackfruit' in fruits_list) # False

# Membership in Dictionary: (In dictionaries, membership checks keys, not values.)
my_info = {
    'name':"Surya",
    'age':20,
    'course':"Python"
}
print('age' in my_info)
#example
passwords = ['python123','surya@34','12345678','#kanta@babu12']
print('surya@34' in passwords)


# 2. 'not in' Operator : Opposite of in.
fruit = "apple"
print('a' not in fruit) # False
print('z' not in fruit) # True

fruits_list = ['apple','banana','guava','grapes','watermelon']
print('guava' not in fruits_list) # False
print('jackfruit' not in fruits_list) # True

