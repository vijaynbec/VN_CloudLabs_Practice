#1 Python Variables
x = 5
y = "John"
print(x)
print(y)
print('x'+'y')
#-----
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0
#-- below string and int will have same values
print(a)
print(b)
print(c)
#---disply type
x = 5
y = "John"
print(type(x))
print(type(y))
#--- difference of quotes
x = "John"
# is the same as
x = 'John'
print(x)
# difference of caps/small
a = 4
A = "Sally"
print(a)
print(A)
#----------------
#2 possible variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#---- invalid var names
my-var="john"
2myvar='john'
my var - 'john'

#3-- assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#4 Out variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "John"
print(x,y)

#---6 Global variables

 #1
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()  # pull x value from function
print("Python is " + x)  # pull x value from outside function

#2 same as above example with global field.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)