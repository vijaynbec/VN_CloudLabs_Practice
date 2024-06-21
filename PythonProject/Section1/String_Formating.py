for i in range(1,6):
   # print (" No. {0} square is {1} and cubed as {2}".format(i, i*2, i**3)) # not alligned
    print(" Alligned No.{0:1} square is {1:2} and cubed as {2:3}".format(i, i * 2, i ** 3))


for i in range(1,6):
   # Left alligned
    print(" Alligned No.{0:1} square is {1:<2} and cubed as {2:<3}".format(i, i * 2, i ** 3))
 # right allign
    print(" Alligned No.{0:1} square is {1:>2} and cubed as {2:>3}".format(i, i * 2, i ** 3))

# f string
name="vijay"
age=22
print(name + f" is {age} years old")
print(f" PI  is approx { 22/7 :2}")

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

# print only numbers
#       0123456789
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
num = print(data[0::5])
print(data[0:-1:5])
print(data[:-1:5])
print(data[-1])
alpha = print(data[2::5])  # printing the alpha letters only
