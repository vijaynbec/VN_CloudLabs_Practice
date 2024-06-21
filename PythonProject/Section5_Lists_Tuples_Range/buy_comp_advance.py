available_parts = ["computer","cable","ipad","mac","hdmi","DVD"]
# if we add DVD in the menu list, just we need to include in the available list print
# will add DVD bu no disply message
current_choice ="-"
comp_parts = []  # create empty list and build the list based on the customer input
while current_choice != '0':
    if current_choice in '12345':
        print("adding {}".format(current_choice))
        if current_choice == '1':
            comp_parts.append("computer")
        elif current_choice == '2':
            comp_parts.append("cable")
        elif current_choice == '3':
            comp_parts.append("ipad")
        elif current_choice == '4':
            comp_parts.append("mac")
        elif current_choice == '5':
            comp_parts.append("hdmi")

    else:
        print("please enter options below ")
        for i in available_parts:
        #    print(i) # this will just give a items in list not choice of number
            print ("{0}: {1}".format(available_parts.index(i)+1, i))
        # it disply with index number and item
        #   print ("{}: {1}".format(available_parts.index(i)+1, i)) will not work

    current_choice=input()

print(comp_parts)

# re-erite same module

available_parts = ["computer","cable","ipad","mac","hdmi","DVD",
                   "Printer"]
# if we add printer in the menu list, just we need to include in the available list print
# will add printer bu no disply message
validchoice=[]       # build the indexing using empty string with index number
for i in range (1, len(available_parts) +1 ):
    validchoice.append(str(i))
print(validchoice)

current_choice ="-"
comp_parts = []  # create empty list and build the list based on the customer input
while current_choice != '0':
    #if current_choice in '12345':
    if current_choice in validchoice: # declared in line 37 to 40
        print("adding {}".format(current_choice))  # print the numbers
        index = int(current_choice) -1   # this is to get the index value of current choice
        chosen_parts = available_parts[index]  # get the item name based on index
        comp_parts.append(chosen_parts)
    else:
        print("please enter options below ")
        for i in available_parts:
        #    print(i) # this will just give a items in list not choice of number
            print ("{0}: {1}".format(available_parts.index(i)+1, i))
        # it disply with index number and item
    current_choice=input()
print(comp_parts)

# rewrite  Add and remove the items from the list
available_parts = ["computer","cable","ipad","mac","hdmi","DVD",
                   "Printer"]
# if we add printer in the menu list, just we need to include in the available list print
# will add printer bu no disply message
validchoice=[]       # build the indexing using empty string with index number
for i in range (1, len(available_parts) + 1):
    validchoice.append(str(i))
print(validchoice)
current_choice = "-"
comp_parts = []  # create empty list and build the list based on the customer input
while current_choice != '0':
    #if current_choice in '12345':
    if current_choice in validchoice: # declared in line 37 to 40
        index = int(current_choice) - 1   # this is to get the index value of current choice
        chosen_parts = available_parts[index]  # get the item name based on index
        if chosen_parts in comp_parts:
            print("Removing part {}".format(current_choice))
            comp_parts.remove(chosen_parts) # remove from list
        else:
            print("Adding part {}".format(current_choice))
            comp_parts.append(chosen_parts)
        print("Your list contains {} ".format(comp_parts))
    else:
        print("please enter options below ")
        for number, i in enumerate(available_parts): #  print(i) #
            print ("{0}: {1}".format(number + 1, i))
        # it disply with index number and item
    current_choice=input()
print(comp_parts)