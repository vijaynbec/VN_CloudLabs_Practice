available_part = {
"1":  'computer',
"2":  'monitor',
"3":  'keyboard',
"4":  'mouse',
"5":  'RAM',
"6":  'cable'
}

current_choice = None
parts_list = []  # create a empty list

while current_choice !="0":

    if current_choice in available_part:
        chosen_part = available_part[current_choice]
        if chosen_part in parts_list:
            print(f"removing {chosen_part}")
            parts_list.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            parts_list.append(chosen_part)
        print(f"Your list now contains: {parts_list}")
    else:
        print("Please add options from the list:")
        for key, value in available_part.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")