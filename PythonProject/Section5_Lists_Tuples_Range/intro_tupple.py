t =("a", "b", "c")  # perefer to use ()
print(t)

name = "tim"
age = 20
print(1, name, age, "Python",2020)
print((2, name, age, "Python",2020))
print()
# tuple
sample = "movie", "DDK", 1982  # tupple is immutable
print(1, sample)
print(2, sample[0])
print(3, sample[2])
# sample[2] = 2023  tupple item assignment fails as list. So its immutable
#tupple item assignment fails as list. So its immutable
# it saves memory for processing and protect data integrity
sample1 = ["movie", "DDK", 1982]  # list is mutable
print(1,sample1)
print(2, sample1[0])
print(3, sample1[2])
sample1[2] = 2023
print(4, sample1)  # changed the data
print()
# unpacking tuple
print("unpacking tupple")
data =7,"raj", 2023
x,y, z = data
print(x)
print(y)
print(z)
# unpacking tuple
print("unpacking list")
data =[7,"raj", 2023]
p,q, r = data
print(p)
print(q)
print(r)

