splitString = "This string has\nmany\nlines"
print(splitString)
tabString = "1\t3\t4\t5\t tab string"
print(tabString)
print('the pet shop said "No no \sh sh \',u,?\,\\\'"')

print('the pet shop said "No no \sh '
      'sh \',u,?\,\\\'"')

anotherString="This string has been \
  split\
   again"
print(anotherString)


x = [10,45,32,35,16,18]
for y in x:
    if y % 7 == 0:
        print("Accept the number")
        break
else:         # else is following the for statements here
    print("It has a valid number")