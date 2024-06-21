# Understanding Lists and List Data Structure
my_tuple = (1, 2, 3, 'apple', 'banana')
print("my list items: ", my_tuple)
print("my list index [3]: ", my_tuple[3])
print("length of my tuple: ",len(my_tuple))
# my_tuple.append('orange')  # Tuple addition is not an option as its immutable
# print("Append the list :", my_tuple)
# my_tuple.remove('apple')   # Tuple deletion is not an option as its immutable
# print("Remove the list apple :", my_tuple)
new_tuple = my_tuple + (10,11,12)
print("new_tuple = my_tuple + [10,11,12] :", new_tuple)
is_present = 'banana' in my_tuple  # Checks if 'banana' is in the list (True)
print("is_present = 'banana' in my_tuple: ", is_present)
print("Unpacking coordinates = (3, 4)")
coordinates = (3, 4)
x, y = coordinates
print("x, y = coordinates: x value", x)
print("x, y = coordinates: y value", y)
