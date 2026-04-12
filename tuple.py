# Tuple
''' A tuple is another sequence data type that is similar to the list.
A tuple consists of a number of values separated by commas.
Unlike lists, however, tuples are enclosed within parentheses.
To delete an entire tuple we can use 'del' statement.Because it's not possible 
to remove a single item from a tuple. Eg. del tuple '''

# example tuple program
tup1 = ('math','physics','chemistry','biology','english','odia')
tup2 = (90,79,75,70,89,88)

print(tup1) # print the complete tuple
print(tup1[0]) # print first element of the tuple
print(tup1[1:3]) # print tuple elements from 2st to 3rd
print(tup1[3:]) # print tuple elements from 4th till end
print(tup1 * 2) # print the tuple elements two times 
print(tup1 + tup2) # print concatenated tuples


# built-in Tuple Function

# 1.len(tuple) {Gives the total length of the table}
tup1 = ('math','physics','chemistry','biology','english','odia')
print(len(tup1))

# 2.max(tuple) {Returns item from the tuple with maximum value.}
tup1 = (90,79,75,70,89,88)
tup2 = (120,389,300,3.14,230)
print("Maximum value in:",tup1,"is",max(tup1))
print("Maximum value in:",tup2,"is",max(tup2))

# 3.min(tuple) {Returns item from the tuple with minimum value.}
tup1 = (90,79,75,70,89,88)
tup2 = (120,389,300,3.14,230)
print("Minimum value in:",tup1,"is",min(tup1))
print("Minimum value in:",tup2,"is",min(tup2))

# 4.tuple(seq) {Convert a list into tuple.}
lis = ['math','physics','chemistry','biology']
print("List:",lis)
print("Tuple:",tuple(lis))
