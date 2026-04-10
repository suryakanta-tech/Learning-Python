# List in Python
''' List is an order sequence of items. '''

# example program of list
first_list = ['abcd',1234,3.14,'Surya']
second_list = ['Surya',20]

print(first_list) # print complete list
print(first_list[0]) # print first element of the list
print(first_list[1:3]) # print elements from second till third
print(first_list[2:]) # print elements from third till end
print(second_list *2) # print the list 2 times
print(first_list + second_list) # concatenated two lists

# example program of list update
list = ['Sethi','Kumar','Mahesh','Surya']
print("Item at position 3 =",list[3])
list[3] = "Basu" # update third position string value 
print("Item at position 3 =",list[3])
print("Items at position 0 and 1 is",list[0],"and",list[1])
list[0] = "xyz"; list[1] = "Soumya" # update zero and first position string value
print("Items at position 0 and 1 is",list[0],"and",list[1])

# example program of list Deletion (remove item)
fruit_list = ['apple','mango','grapes','guava','banana']
print("List before deletion:",fruit_list)
del fruit_list[2]
print("List after deletion:",fruit_list)


# Built-in List Functions

# 1.len(list) {Gives the total length of the string.}
x = ['abcd','surya',3.14]
print(len(x))

# 2.max(list) {Return items from the list with maximum value.}
x = [10,100,1000,10000,100000]
y = [9,99,999,9999,99999]
print("Maximum value in",x,"is",max(x))
print("Maximum value in",y,"is",max(y))

# 3.min(list) {Return items from the list with minimum value.}
x = [10,100,1000,10000,100000]
y = [9,99,999,9999,99999]
print("Minimum value in",x,"is",min(x))
print("Minimum value in",y,"is",min(y))

# 4.map(aFunction,aSequence) {The map(aFunction,aSequence) function applies a passed-in function
# to each item in an iterable object and returns a list containing all the function call results.}
s = input("Enter a list (space separated):")
lis = [int(x) for x in s.split()]
print(lis)


# Built-in List Method

# 1.list.append(obj) {This method appends an object obj passed to the existing list.}
x = ['abcd',3.14,444,'Surya']
print("List before append:",x)
x.append(100)
print("List after append:",x)

# 2.list.count(obj) {Returns how many times the object obj appears in a list.}
x = ['abcd',111,444,3.14,'Surya',444,'abcd',444]
print(x.count(444))
print("The number of times",444,"appears in",x,"is =",x.count(444))

# 3.list.remove(obj) {Remove objects obj from the list.}
x = ['abcd',100,3.14,444]
print("List before remove:",x)
x.remove(3.14)
print("List after remove:",x)

# 4.list.index(obj) {Returns index of the object obj if found, otherwise
# raise an exception indicating that value does not exist.}
x = ['abcd',444,3.24,'Surya']
print(x.index(3.24))

# 5.list.extend(seq) {Appends the contents in a sequence seq passed to a list.}
x = ['abcd',100,3.14,'Surya']
y = ['python','java']
x.extend(y)
print(x)

# 6.list.reverse() {Reverse objects in a list.}
x = ['abcd',100,3.14,'Surya']
x.reverse()
print(x)

# 7.list.insert(index,obj) {Returns a list with object obj inserted at the given index.}
x = ['abcd',100,3.14,'Surya']
print("List before insert:",x)
x.insert(2,999)
print("List after insert:",x)

# 8.list.sort([func]) {Sorts the items in a list and returns the list. If a function is 
# provided, it will compare using the function provided.}
x = [890,147,2.43,100,3.14]
print("List before sorting:",x)
x.sort()
print("List after sortig:",x)

# 9.list.pop(obj = list[-1]) {Removes or returns the last object obj from a list.}
x = ['abcd',147,3.14,'Surya']
print("List before poping:",x)
x.pop(-1)
print("List after poping:",x)