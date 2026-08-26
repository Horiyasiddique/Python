# (4) String
# string take more space than other data types.

# ord() convert charater into its uni code
a = "h"
print(ord(a))

# chr() convert uni code into its character
b = 104
print(chr(b))

# String Indexing
str = "Python"
print(str[1]) # Positive indexing
print(str[-2]) # Negative Indexing
print(str[-3], str[4])

# String Slicing
str2 = "Hello Python!"
print(str2[6:12:1]) 
# first is "starting point", second is "Stop point", last is "steps value" & keep a note if we use stop at 4 it will slice till 3 only.