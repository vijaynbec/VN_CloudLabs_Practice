day="Saturday"
temprature = 30
raining = "True"
if day=="Saturday" and temprature > 26 and not raining:
    print(" Lets go Swimming")
else:
    print("Learn Python")
print("-" * 80)
if day=="Saturday" and temprature > 26 or not raining:
    print(" Lets go Swimming")
else:
    print("Learn Python")
print("-" * 80)
# Bolean expression
if 0:
    print("true")
else:
    print("false")
name = input("hay !! enter your name")
#if name:  # or we can as if name!=""
if name != "":
    print("Here you go {} !!".format(name))
else:
    print("enter your details")



