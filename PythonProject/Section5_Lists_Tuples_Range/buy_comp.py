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
        print("1: computer")
        print("2: cable")
        print("3: ipad")
        print("4: mac")
        print("5: hdmi")
        print("0: finish")
    current_choice=input()

print(comp_parts)