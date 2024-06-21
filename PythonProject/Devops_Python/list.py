# Understanding Lists and List Data Structure
my_list = [1, 2, 3, 'apple', 'banana']
print("my list items: ", my_list)
print("my list index [3]: ", my_list[3])
print("length of my list: ",len(my_list))
my_list.append('orange')
print("Append the list :", my_list)
my_list.remove('apple')
print("Remove the list apple :", my_list)
new_list = my_list + [10,11,12]
print("new_list = my_list + [10,11,12] :", new_list)
is_present = 'banana' in my_list  # Checks if 'banana' is in the list (True)
print("is_present = 'banana' in my_list: ", is_present)