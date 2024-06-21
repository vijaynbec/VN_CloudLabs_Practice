# nested lists

menu = [["egg", "boil", "fry"],
        ["egg", "boil"],
        ["boil", "fry"],
        ["boil", "tea"],
        ["egg", "boil", "fry", "omlet"]]
for meal in menu:
    if "fry" not in meal:
        print(meal)
        for item in meal:
            print(meal)

            # challenge remove fry
menu = [["egg", "boil", "fry"],
        ["egg", "boil"],
        ["boil", "fry"],
        ["boil", "tea"],
        ["egg", "boil", "fry", "omlet"]]

# Approch #1
# for meal in menu:
#    for index in range(len(meal) - 1, -1, -1):
#        if meal[index] == "fry":
#            del meal[index]
#    print(meal)

# Approch #2
for meal in menu:
   for item in meal:
       if item != "fry":
           print(item)