# block line end with "  :  "

for i in range(1,5):
    print ("No. {} squared {}". format(i, i**2))
    print ("*" * 70)

name = input("please enter the name: ")
age = int(input("How old are you {} ?".format(name)))  # int expect the value as int
print(age)

# if else statements
name = input("please enter the name: ")
age = int(input("How old are you {} ?".format(name)))  # int expect the value as int
print(age)
if age > 18:
    print("{} is old enough to Vote".format(name))
else:
    print ("Please come back after {0}".format(18 - age))

# elif statements
name = input("please enter the name: ")
age = int(input("How old are you {} ?".format(name)))  # int expect the value as int
print(age)
if age > 18:
    print("{} is old enough to Vote".format(name))
elif age == 110:
    print("{} sorry you may not enough to live".format(name))
else:
    print("{} please come back after {1}".format(18 - age))


x=5
y=7
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")