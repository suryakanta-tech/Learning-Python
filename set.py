# Set
''' Set is an unoredred collection of unique items. Set is defined
by value separated by comma inside braces { }. '''

# example program of set{}
s1 = {1,2,3} # set of integer number
print(s1)
s2 = {1,2,3,2,3,1,2} # output contains only unique values
print(s2)
s3 = {1,3.14,44,'surya','basu'} # set of mixed data type
print(s3)
s4 = set([1,2,3]) # using set function to create set from a list
print(s4)
# s5 = {1,2,[3,4]} # sets cannot have mutable items
# print(s5) # hence not permited



# Built-in Set Function

# 1.len(set) - Returns the length or the total number of items in a set.
s1 = {'Surya',2.11,154,'kanta'}
print(len(s1))

# 2.max(set) - Returns item from the set with maximum value.
s1 = {234,3.13,5,34,77,999,444}
print("Maximum value in",s1,"is:",max(s1))

# 3.min(set) - Returns item from the set with minimum value.
x = {234,3.13,5,34,77,999,444}
print("Minimum value in",x,"is:",min(x))

# 4.sum(set) - Returns the sum of all items in the list.
x = {10,20,30,40,50}
print("Sum of",x,"is:",sum(x))

# 5.sorted(set) - Returns a new sorted set.The set does not sort itself.
x = {234,5,34,77,999,444}
y = sorted(x)
print("Before sorting:",x)
print("After sorting:",y)

# 6.enumerate(set) - Returns an enumerate object.It contains the index and
                   # the value of all items of set as a pair.
x = {234,5,34,77,999,444}
print("enumerate (set):",enumerate(x))

# 7.any(set) - Returns True, if the set contains at least one item, False otherwise.
x = set( )
print("any(set):",any(x))
y = {2,4,6,8,10}
print("any(set):",any(y))

# 8.all(set) - Returns True, if all the elements are true or the set is empty.
x = set( )
print("all(set):",all(x))
y = {2,4,6,8,10}
print("all(set):",all(y))



# Built-in Set Methods

# 1.set.add(obj) - Adds an element obj to a set.
s1 = {6,4,8,2,3}
print("Set before add element:",s1)
s1.add(10)
print("Set after add element:",s1)

# 2.set.remove(obj) - Removes an element obj from a set.
# Raises KeyError if the set is empty.
s1 = {6,4,8,2,3}
print("Set before remove element:",s1)
s1.remove(3)
print("Set after remove element:",s1)

# 3.set.discard(obj) - Removes an element obj from the set. Nothing happens
# if the element to be deleted is not in the set.
s1 = {6,4,8,2,3}
print("Set before discard:",s1)
s1.discard(3)
print("Set after discard:",s1) # element is present
s1.discard(9)
print("Set after discard:",s1) # element is not present

# 4.set.pop() - Removes and returns an arbitary set element.Raises KeyError if the set is empty.
s1 = {6,4,8,2,3}
print("Set before pop:",s1)
s1.pop()
print("Set after pop:",s1)

# 5.set1.union(set2) - Returns the union of two sets as a new set.
s1 = {2,4,6,8,10}
print("Set1:",s1)
s2 = {3,4,5,6,7}
print("Set2:",s2)
s3 = s1.union(s2) # unique value will be taken
print("Union:",s3) # returns the union set

# 6.set1.update(set2) - Update a set with the union of itself and others. The result will be stored in set1.
s1 = {1,3,5,7,9}
print("Set1:",s1)
s2 = {2,4,6,8,1}
print("Set2:",s2)
s1.update(s2) # unique value will be taken
print("Update method:",s1)

# 7.set1.intersection(set2) - Returns the intersection of two sets as a new set.
s1 = {1,3,5,7,9}
print("Set1:",s1)
s2 = {2,4,6,8,1}
print("Set2:",s2)
s3 = s1.intersection(s2)
print("Intersection:",s3)

# 8.set1.intersection_update() - Update the set with the intersection of 
# itself and another.The result will be store in set1.
a = {3,8,2,6}
print("Set1:",a)
b = {4,2,1,9}
print("Set2:",b)
a.intersection_update(b)
print("Intersection:",a)

# 9.set1.difference(set2) - Returns the difference of two or more
# sets into a new set.
a = {3,4,2,9}
print("Set1:",a)
b = {4,2,1,9}
print("Set2:",b)
c = a.difference(b)
print("Difference:",c)

# 10.set1.difference_update(set2) - Remove all elements of another set set2 from 
# set1 and the result is stored in set1.
a = {3,8,2,6}
print("Set1:",a)
b = {4,2,1,9}
print("Set2:",b)
a.difference_update(b)
print("Difference Update:",a)

# 11.set1.symmetric_difference(set2) - Returns the symmetric difference of 
# two sets as a new set.
a = {3,8,2,6}
print("Set1:",a)
b = {4,2,1,9}
print("Set2:",b)
c = a.symmetric_difference(b)
print("Symmetric Difference:",c)

# 12.set1.symmetric_difference_update(set2) - Update a set with the symmetric 
# difference of itself and another. 
a = {3,8,2,6}
print("Set1:",a)
b = {4,2,1,9}
print("Set2:",b)
a. symmetric_difference_update(b)
print("Symmetric Difference Update:",a)

# 13.set1.isdisjoint(set2) - Returns True if two sets have a null intersection.
a = {1,2,3,4}
print("Set1:",a)
b = {5,6}
print("Set2:",b)

print("Both sets have a null intersection:",a.isdisjoint(b))

# 14.set1.issubset(set2) - Returns True if set1 is a subset of set2.
a = {1,2,3,4}
print("Set1:",a)
b = {5,6,7,8,1,2,3,4}
print("Set2:",b)

print("Set1 is a Subset of Set2:",a.issubset(b))

# 15.set1.issuperset(set2) - Returns True if set1 is a super set of set2.
a = {1,2,3,4,5,6}
print("Set1:",a)
b = {5,6}
print("Set2:",b)

print("Set1 is a Superset of Set2:",a.issuperset(b))


# Frozenset
''' Frozenset is a new class that has the characteristics of a set, but its
elements cannot be changed once assigned. '''

# example of frozenset
a = frozenset({1,2,3,4})
print("Set1:",a)
b = frozenset({3,8})
print("Set2:",b)

print("Result of set1 intersection set2 is:",a.intersection(b))

