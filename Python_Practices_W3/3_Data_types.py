# Python has the following data types built-in by default, in these categories:
#------------------------------------
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
#------------------------------------

# Setting data types

x = "Hello World"	#str
print(x, 'its a string')
x = 20	# int
print(x, 'its a integer value')
x = 20.5	# float
print(x, 'its a float')
x = 1j	# complex
print(x, 'its a complex')
x = ["apple", "banana", "cherry"]	# list
print(x, 'its a list')
x = ("apple", "banana", "cherry")	# tuple
print(x, 'its a tuple')
x = range(6)	# range
print(x, 'its a range(6)')
x = {"name" : "John", "age" : 36}	# dict
print(x, 'its a dictionary')
x = {"apple", "banana", "cherry"}	# set
print(x, 'its a set')
x = frozenset({"apple", "banana", "cherry"})	# frozenset
print(x, 'its a frozenset')
x = True	# bool
print(x, 'its a boolean')
x = b"Hello"	# bytes
print(x, 'its shows displays bytes')
x = bytearray(5)	# bytearray
print(x, 'its shows displays bytearrays')
x = memoryview(bytes(5))	# memoryview
print(x, 'its shows displays memoryview')
x = None	# NoneType
print(x, 'its shows displays NoneType')

