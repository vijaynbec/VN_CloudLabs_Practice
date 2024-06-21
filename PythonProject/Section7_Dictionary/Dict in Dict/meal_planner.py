from contents import pantry,recipes
# print(pantry)
# print(recipes)

for index,key in enumerate(recipes):          # use enumurate as display the value with zero index
    print(index+1, key)             # added one for index to start from 1

print ("*" * 80)

#---------------------------------------------------
display_dict = {}
for index,key in enumerate(recipes):
    display_dict[(index+1)] =  key
while True:
    print("Please chose recipes")
    for key, value in display_dict.items():
        print(f"{key}  - {value}")
    choice = input(":  ")
    if choice == "0":
        break


