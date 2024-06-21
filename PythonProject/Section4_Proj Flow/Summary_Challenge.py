print("Please select from the below options")
print("1:\t learn Python")
print("2:\t learn AWS")
print("3:\t learn lamda")
print("0: \t exit")

while True:
    option = input()
    if option == "0":
        print("You have exited from the learning choice")
        break
    elif option in "123":
        print ("Your choice is {}".format(option))
    else:
        print("Please select from the below options")
        print("1:\t learn Python")
        print("2:\t learn AWS")
        print("3:\t learn lamda")
        print("0: \t exit")
    --------------------------------------using fuctions below
option="-"
while option != "0":
    if option in "123":
        print ("Your choice is {}".format(option))
    else:
        print("Please select from the below options")
        print("1:\t learn Python")
        print("2:\t learn AWS")
        print("3:\t learn lamda")
        print("0: \t exit")
    option = input()