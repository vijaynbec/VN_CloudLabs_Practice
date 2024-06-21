fruits = ["orange", "Orange", 20,
          "banana", "yellow", 25,
          "tomato", "red", 50,
          "chil", "green", 20]
print(len(fruits))
fruits1 = [("orange", "Orange", 20),   # as one tuple entry with 4 list
          ("banana", "yellow", 25),
          ("tomato", "red", 50),
          ("chil", "green", 20)]
print(len(fruits1))
# option-1
for i in fruits1:
     print("Item_name:{}, Item:{}, price:{}".format(fruits[0], fruits[1],fruits[2]))
# option-2
for item_name,color,price in fruits1:
     print("Item_name:{}, Item:{}, price:{}".format(item_name,color,price))

# Tuples           vs                List
#   {} get used                     [] get used
#   Immutable  (Can;t append)       Mutable (can append)
#    Fast                           Slow
# Less memory                        More memory
# can use as dictionry               Cannot use as dictionary
