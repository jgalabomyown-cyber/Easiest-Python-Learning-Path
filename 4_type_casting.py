age = 12
name = "John Doe"

print('Hi, My name is ' + name + 'I am ' + str(age) + ' years old')
print(type(age))

# Implicit Type Casting
# Python automatically converts 'a' to int
a = 7
print(a, type(a))

# Python automatically converts 'b' to float
b = 2.5 
print(b, type(b))

# Automatically converts 'c' to float as the result says
c = a + b
print(c, type(c))

# Explicit Type Casting
# Programmer manually converts value's data type
# int(), float(), str()
d = 5
n = float(d)
print(n, type(n))

# float to int
e = 5.9
o = int(e)
print(o,type(o))

# type() function
a = 2
print(type(a))  # <class 'int'>

# round() function
print(round(3.14)) # 3
print(round(3.14, 1)) # 3.1 - second arg specifies decimal places

# abs() function / Absolute
print(abs(-25)) # 25
print(abs(25)) # 25