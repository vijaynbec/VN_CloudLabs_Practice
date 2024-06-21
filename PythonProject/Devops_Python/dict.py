my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

print(my_dict['name'])  # Output: John
print(my_dict['city'])  # Output: New York

my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
print("my_dict['age'], my_dict['occupation'] - updated dict ", my_dict)

for key, value in my_dict.items():
    print(key,value)
