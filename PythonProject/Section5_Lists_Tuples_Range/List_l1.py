

comp_parts = ["key",   #0   list
              "wire",  #1
              "bottle",  #2
              "cable"]  #3
print(comp_parts)  # before modify
comp_parts[0] = "mouse"
print(comp_parts)  # after modify
#  slicing [start pos: ending pos] replacing item frm list
comp_parts[2:3]=["pad"]
print(comp_parts)  # after modify
####################################

# Delete from slicing
#dev = [1,66,6.6,79,99,100,152,153,155,186,188,525,556]
dev = [525,556]
#del dev[0:2]  # this deletion work
print(dev)
min_valid=100
max_valid=200
# process low values in the list
stop=0
for number,value in enumerate(dev):
    if value >= min_valid:
        stop=number
        break
print(stop)
del dev[:stop]
print(dev)

# process high values in the list
start=0
for index  in range(len(dev)-1, -1, -1):
    if dev[index] <= max_valid:
        start=index + 1
        break
print(start)
del dev[start:]
print(dev)

