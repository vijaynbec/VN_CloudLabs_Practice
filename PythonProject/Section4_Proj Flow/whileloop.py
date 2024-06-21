# listing, break, indexing examples
for i in range (10):
    print ("i is now has a value {}".format(i))

# identical to above for loop used to keep on reading the file untill end
i = 0
while i < 10:
    print("i is now has a value {}".format(i))
    i = i+1
print("*"*20)

direction = ["north","south","east","south"]
out=""
while out not in direction:
    out = input("enter the required direction to turn ")
    if out.casefold() == "quit":  # case
        print("Game over")
print("Good you came out")

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 ==0:
      break

# print not divisible by 3 and 5
for i in range (21):
    if i % 3 != 0 and 5 !=0:
        print(i)