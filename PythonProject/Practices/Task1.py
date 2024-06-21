"VIJAY"


x = int(input("Enter the number"))
y = x % 2
if y == 0:
  # print("Even")
  if x in range (2,5):
      print("Not Weird")
  elif x in range(6, 20):
      print("Weird")
  else:
      print("Not Weird")
else:
  # print("Odd")
  print("Weird")


# Given an integer, , perform the following conditional actions:
#
# If x is odd, print Weird
# If x is even and in the inclusive range of 2 to 5, print Not Weird
# If x is even and in the inclusive range of 6 to 20 , print Weird
# If x is even and greater than 20 print Not Weird