# Strings

a = "Welcome to Python Programming"

print(a)
print(a[0])
print(a[11:17])
print(a[11:])
print(a * 2)
print(a + " Language.")


# string formatting operator

# usage of %s for string, %i for integer
print("My name is %s and i am %i years old."%("Surya",20))
# usage of %d
print("The sum = %d" %(-12))
# usage of %i
print("The sum = %i" %(-12))
# usage of %u
print("The sum = %u" %(-12))


# string formatting functions

# 1.len(string) - return the length of the string
s = ("Learning python is fun!")
print("Length of ", s, "is:", len(s))

# 2.lower()
s = ("LEARNING PYTHON IS FUN!")
print(s.lower())

# 3.Upper()
s = "Learning Python is fun!"
print(s.upper())

# 4.swapcase()
s = "Learning Python is Fun!"
print(s.swapcase())

# 5.capitalize()
s = "learning python is fun!"
print(s.capitalize())

# 6.title() {Makes first character of all words capitalized.}
s = "learning python is fun!"
print(s.title())

# 7.lstrip() {Returns a copy of the string in which all the characters
# have been stripped(removed) from the beginning.the default character is whitespaces.}
s = "       learning Python is fun!"
print(s.lstrip())
s = "*******learning Python is fun!"
print(s.lstrip('*'))

# 8.rstrip() {Returns a copy of the string in which all the characters
# have been stripped(removed) from the ending.the default character is whitespaces.}
s = "Learning python is fun!       "
print(s.rstrip())
s = ("Learning python is fun!*******")
print(s.rstrip('*'))

# 9.strip() {Returns a copy of the string in which all the characters have been stripped(removed)
# fromo the beginning and end. It performs both lstrip() & rstrip().The default character is whitespaces.}
s = "       Learning Python is fun!       "
print(s.strip())
s = "******Learning Python is fun!******"
print(s.strip('*'))

# 10.max(str) {Returns the maxium alphabetical character from the string.}
s = "Surya"
print("Maximum character is:",max(s))

# 11.min(str) {Returns the minimun alphabetical character from the string.}
s = "Surya"
print("Minimum character is:",min(s))

# 12.replace(old,new,[max]) {Returns a copy of the string with all the occurrences of substringold is replaced
#  by new.The max is optional and if it is specified,the first occurrences specified in max are replaced.}
s = "Ram is in the class room.Gobinda is also in the class room."
print(s.replace('is','was'))
print(s.replace('is','was',1))

# 13.center(width,fillchar) {Returns a string centered in a length specified in the width variable.Padding is done using 
# the character specified in the fillchar.Default padding is space.}
s = "I am Learning Python programming language."
print(s.center(50,'*'))
print(s.center(50))

# 14.ljust(width,[fillchar]) {Returns a string left-justified in a length specified in the width variable.
# Padding is done using the character specified in the fillchar.Default padding is space.}
s = "I am Learning Python programming language."
print(s.ljust(50,'*'))
print(s.ljust(50))

# 15.rjust(width,[fillchar]) {Returns a string right-justified in a length specified in the width variable.
# Padding is done using the character specified in the fillchar.Default padding is space.}
s = "I am Learning Python programming language."
print(s.rjust(50,'*'))
print(s.rjust(50))

# 16.zfill(width) {The method zfill() pads string on the left with zero to fill the width.}
s = "I am learning Python Programming Language."
print(s.zfill(50))

# 17.count(str,beg = 0,end = len(string)) {Returns the number of occurrences of str in the range beg and end.}
s = "This is Python Programming"
print(s.count('n',0,12))
print(s.count('n',0,20))
print(s.count('n',0,30))

# 18.find(str,beg = 0,end = len(string) {Returns the index of str if str occurs in the range beg and end and returns -1 if it is not found.}
s = "This is Python Programming."
print(s.find('Pyth',0,10))
print(s.find('Pyth',0,20))

# 19.rfind(str,beg = 0,end = len(string)) {Same as find but searches backward in a string.}
s = "This is Python Programming."
print(s.rfind('Pyth',0,10))
print(s.rfind('Pyth',0,20))

# 20.index(str,beg = 0,end = len(string)) {Same as find but raises an exception if str is not found.}
s = "This is Python Programming."
print(s.index('thon',0,25))
# print(s.index('thy'))

# 21.rindex(str,beg = 0,end = len(string)) {Same as index but searches backward in a string.}
s = "This is Python Programming."
print(s.rindex('thon',0,25))
# print(s.rindex('thy'))

# 22.startswith(suffix, beg = 0, end = len(string)) {It returns True if  the string begins with the
# specified suffix, otherwise return False.}
s = "Pythin Programming is Fun!"
print(s.startswith('Pro',5,25))
print(s.startswith('Pro',7,25))

# 23.endswith(suffix, beg = 0, end = len(string)) {It returns True if the strings end with the
# specified suffix, otherwise return False.}
s = "Python Programming is Fun!"
print(s.endswith('ing',5,25))
print(s.endswith('ing',5,18))

# 24.isdecimal() {Returns True if a unicode string contains only decimal characters and False otherwise.
# To define a string as unicode string,prefix 'u' to the front of the quotation mark.}
s = u"This is Python 1234"
print(s.isdecimal())
s = "Python"
print(s.isdecimal())
s = u"1234"
print(s.isdecimal())

# 25.isalpha() {Returns True if string has at least 1 character and all characters are alphabetic and False otherwise.}
s = "Python 1234"
print(s.isalpha())
s = "1234"
print(s.isalpha())
s = "Python"
print(s.isalpha())

# 26.isalnum() {Returns True if string has at least 1 character and all characters are 
# alphanumeric and False otherwise.}
s = "Python1234***"
print(s.isalnum())
s = "Python1234"
print(s.isalnum())

# 27.isdigit() {Returns True if string contains only digits and False otherwise.}
s = "***Python1234"
print(s.isdigit())
s = "Python1234"
print(s.isdigit())
s = "124"
print(s.isdigit())

# 28.islower() {Returns True if string has at least 1 cased character and all cased 
# character are in lowercase and False otherwise.}
s = "Python Programming."
print(s.islower())
s = "python Programming."
print(s.islower())
s = "python programming."
print(s.islower())

# 29.isupper() {Returns True if string has at least 1 cased character and all cased 
# character are in uppercase and False otherwise.}
s = "python programming."
print(s.isupper())
s = "Python programming."
print(s.isupper())
s = "PYTHON PROGRAMMING."
print(s.isupper())

# 30.isnumeric() {Returns True if a unicode string contains only numeric characters and False otherwise.}
s = "Python12344"
print(s.isnumeric())
s = "12345"
print(s.isnumeric())

# 31.isspace() {Returns True if string contains only whitespace characters and False otherwise.}
s = "Python Programming."
print(s.isspace())
s = "  "
print(s.isspace())

# 32.istitle() {Returns True if string is properly 'titlecased' and False otherwise.Title case means each 
# word in a sentence begins with uppercase letter.}
s = "Pythin programming."
print(s.istitle())
s = "Python Programming."
print(s.istitle())

# 33.expandtabs(tabsize=8) {It returns a copy of the string in which tab character ie.'\t' are expanded
# using spaces using the given tabsize.The default tabsize is 8.}
s = "Python\tProgramming\tis\tfun."
print(s.expandtabs())
s = "Python\tProgramming\tis\tFun."
print(s.expandtabs(10))

# 34.join(seq) {Returns a string in which the string elements of sequence have been joined by a separetor.}
s = "_"
seq = ('Python','Programming.')
print(s.join(seq))
s = "+"
seq = ("Python "," Programming")
print(s.join(seq))

# 35.split(str = "",num = string.count(str)) {Returns a list of all the words in the string, using str as the
# separator (splits on all whitespace if left unspecified),optionally limiting the number of splits to num.}
s = "Python Programmin is Fun."
print(s.split(' '))
s = "Python Programmin is Fun."
print(s.split('*'))
s = "Python Programmin is Fun."
print(s.split(' ',2))

# 36.splitlines(num = string.count('\n')) {Split string at all (or num) NEWLINEs and returns a list of each line with
# NEWLINEs removed.If num is specified,it is assumed that line breaks need to be included in the lines.}
s = "Python\nProgramming\nis\nFun."
print(s.splitlines())
print(s.splitlines(0))
print(s.splitlines(1))






