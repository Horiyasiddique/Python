# (4) Type Conversion

# from integar to string
num = 12
print(type(num))
num = str(num)
print(type(num))

# from flot to string
flo = 3.141
print(type(flo))
flo = str(flo)
print(type(flo))

# from complex to string
cmplx = 3j
print(type(cmplx))
cmplx = str(cmplx)
print(type(cmplx))

# from string to integar 
word = "44"
print(type(word))
word = int(word)
print(type(word))

# from string to boolean
letter = "h"
print(type(letter))
letter = bool(letter)
print(type(letter))

# from number to boolean
# There are 7 truthy and falsy values 
# Falsy Values : - 0 0.0 False “” [] {} ()
# Truthy Values : - All the reaming values are truthy.
zero = 0
one = 1
print(type(zero))
print(type(one))
zero = bool(zero)
one = bool(one)
print(zero)
print(one)
print(type(zero))
print(type(one))