sent = " Pete the cat went to beach"

print("1 split by")
work = sent.split()
print(work)

sent1 = """Pete the
        cat went
        to beach """

print("2 split ")
work = sent1.split()
print(work)

# example #2
num1="8,89,5,54,654,652,3,34,6"

print("3 by split")
print(num1.split(","))


print("4 by join")
print("".join(num1))

print("5 by split result as char")
new =num1.split(",")
print(new)


print("6 by list append with int values")
int_empty_lst = []
for index in new:
   int_empty_lst.append(int(index))
print(int_empty_lst)



# Take input from the user
