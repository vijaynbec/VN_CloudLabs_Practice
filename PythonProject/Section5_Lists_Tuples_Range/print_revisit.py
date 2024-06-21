name="Raj"
age = 20

print(name, age, "python" , 2023)
print(name, age, "python" , 2023,sep=",")
print(name, age, "python" , 2023,end=" ")
print()

            # challenge remove fry
menu = [["egg", "boil", "fry"],
        ["egg", "boil"],
        ["boil", "fry"],
        ["boil", "tea"],
        ["egg", "boil", "fry", "omlet"]]

# print statements
for meal in menu:
   for item in meal:
       if item != "fry":
           # print(item)
           print(item, end=", ")
   print()

            # challenge remove fry
menu = [["egg", "boil", "fry"],
        ["egg", "boil"],
        ["boil", "fry"],
        ["boil", "tea"],
        ["egg", "boil", "fry", "omlet"]]

# Approch #1 Print using join method
for meal in menu:
   for index in range(len(meal) - 1, -1, -1):
       if meal[index] == "fry":
           del meal[index]
   # print(meal)
   print(",".join(meal))