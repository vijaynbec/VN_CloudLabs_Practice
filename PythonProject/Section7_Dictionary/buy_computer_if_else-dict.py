available_part = {
"1":  'computer',
"2":  'monitor',
"3":  'keyboard',
"4":  'mouse',
"5":  'RAM',
"6":  'cable'
}
current_choice = None
while current_choice !="0":
    if current_choice in available_part:
        selected_part = available_part[current_choice]
        print(f"adding {selected_part}")
    else:
        print("please select options")
        for key, value in available_part.items():
            print (f"{key}:  {value} ")
        print("0  to exit")
    current_choice = input("> ")
