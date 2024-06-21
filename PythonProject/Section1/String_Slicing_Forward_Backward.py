
#        012345667
state = "karnataka"
print(state)

print(state[4])

print(state[2])

print(state[0])
#  0123456789
a="Norwegian Blue"
print(a)
print(a[3])  # display by certain position
print(a[4])
print(a[9])
print(a[3])
print(a[6])
print(a[8])
print()
print(a[-11]) # display by negative
print(a[-10])
print(a[-5])
print(a[-11])
print(a[-8])
print(a[-6])
print()
print(a[3-14])  # display by negative same as line#21
print(a[4-14])
print(a[9-14])
print(a[3-14])
print(a[6-14])
print(a[8-14])
print()
 # slicing  "  :  " is used, else it would be indexing
#    0123456789
a = "Norwegian Blue"
print(a[0:6])  # not including index 6
print(a[3:6])  # including  3 index , doe
print(a[6])
print(a[:6])
print(a[10:14])  # display the blue
print(a[10:])  # display the blue

print(a[:6])
print(a[6:])
print(a[:])  # start from begining and consume till the end

# slicing is negative
#    01234567890123
a = "Norwegian Blue"
     #   -14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
     #    N   o    r   w   e  g  i  a  n     B  l  u  e
print(a[-14:-8])  # negative slicing
print(a[0:6])
print(a[-4:])  # display the blue
print(a[-4:-1])  # display the blu

# slicing in steps
#    01234567890123
a = "Norwegian Blue"
print (a[0:6:3])  # Display Nw
print (a[10:14:])  # Blue
print (a[0:14:10])  # NB
#    012345678901234567890
b = "8,989,565,555,446,876"
#      [start value,stop value]
print(b[1::4])  # print only comma's
print(b[1::2])  # print second number after each comm;s
print(b[1::1])  # print first number after each comm;s
# sperating spl characters
b = "8\989/565?555{446}876"
print(b[1::4])  # print only seperators
print(b[1::2])  # print second number after each seperators
print(b[1::1])  # print first number after each each seperators
# replace with comma's and remove yje spl characters
b = "8\989/565?555{446}876"
specials = b[1::4]  # only seperators
print(specials)
numbers = "".join(char if char not in specials else " " for char in b).split()
print([int(val) for val in numbers])

# Slicing Backwords

alpha = "abcdefghijklmnopqrstuvwxyz"
 #         [start value: stop value: + is forward slicing and - is for backward]
print(alpha[25:0:-1])  # stop value 0 will skip the print of a
print(alpha[25::-1])   # remove the zero it print the "a" as well
print(alpha[::-1])   # remove the start and stop value it print the "a" as well

#        01234567890123456789012345
alpha = "abcdefghijklmnopqrstuvwxyz"
# print qpo
print(alpha[16:13:-1])
# print edcba
print(alpha[4::-1])
# last 8 character in reverse order
print(alpha[25:17:-1])