para="Norwegian Blue"
for character in para:  # keep checking on letter
    print(character)
print ("<>" * 15)

# printing all special character in the string
number = "7,56:545>4545,9?89 999/89"
specials = ""
print(specials)
for char in number:
    if not char.isnumeric():
        specials = specials + char
print(specials)
values = "".join(char if char not in specials else " " for char in number).split()
print([int(val) for val in values])
print ("<>" * 15)
# take entry from user
number = input("Please enter numbers with any specials ")
specials = ""
print(specials)
for char in number:
    if not char.isnumeric():
        specials = specials + char
print(specials)
values = "".join(char if char not in specials else " " for char in number).split()
print([int(val) for val in values])
print ("<>" * 15)
# take entry from user and sum with all numbers
number = input("Please enter numbers with any specials ")
specials = ""
print(specials)
for char in number:
    if not char.isnumeric():
        specials = specials + char
print(specials)
values = "".join(char if char not in specials else " " for char in number).split()
print(sum([int(val) for val in values]))

# find the upper case letter
quote = """Public Order, Irrigation, Roads, the Fresh-Water."""
for char in quote:
    if char.isupper():
        print(char)
print ("<>" * 15)
for char in quote:
    if char.islower():
        print(char)
        