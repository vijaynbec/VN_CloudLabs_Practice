#example:
for index, character in enumerate("abcdefghijklmnopqrstuvwzyz"):
    print(index+1,character)



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
        #for i in available_parts:
        #    print ("{0}: {1}".format(available_parts.index(i)+1, i))
        for number,i in enumerate(available_parts):
            print("{0}: {1}".format(number+1, i))

    current_choice=input()

print(comp_parts)


