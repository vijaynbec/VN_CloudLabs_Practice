# Delete from slicing
dev = [1,66,6.6,79,99,100,152,153,155,186,188,525,556]
min_valid=100
max_valid=200
# process high values in the list

for index  in range(len(dev)-1, -1, -1):
    if dev[index] < min_valid or dev[index] > max_valid:
        print(index,dev)   # print for every occurrence of index
        del dev[index]
print(dev)


############ Reverese Itterates with examples
dev = [1,66,6.6,79,99,100,152,153,155,186,188,525,556]
min_valid=100
max_valid=200
top_index= len(dev) - 1
for index, value in enumerate(reversed(dev)):
    if value < min_valid or value > max_valid:
        print(top_index - 1, value)
        del(dev[top_index - index])
print(dev)

