para="Norwegian Blue"
letter=input("Enter the input char")
if letter in para:
    print(" '{}' is found in {}".format(letter,para))
else:
    print(" Sorry couldn't find it {}".format(para))
print ("<>" * 15)
# checking with not in
letter=input("Enter the input char")
if letter not in para:
    print(" '{}' is not found in {}".format(letter,para))
else:
    print(" Hurry you found in {}".format(para))
## If challenge
Name = input("Please enter your name: ")
age = int(input("please enter your age: "))
if 18 <= age < 31:
    print(" {} you are eligible for vacation, your age is {} ".format(Name,age))
else:
    print(" Sorry you are not eligible")