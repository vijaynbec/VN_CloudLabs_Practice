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
    current_choice = input("> ")