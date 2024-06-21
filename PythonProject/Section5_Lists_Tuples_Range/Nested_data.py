fruits1 = [("orange", "Orange", 20,   # as one tuple entry with 4 list
            [(1, "Kroger0"),(2, "walmart0")] ),
          ("banana", "yellow", 25,
            [(1, "Kroger1"),(2, "walmart1")]),
          ("tomato", "red", 50,
            [(1, "Kroger2"),(2, "walmart2")]),
          ("chil", "green", 20,
           [(1, "Kroger3"),(2, "walmart3")])
          ]
for item_name,color,price,shops in fruits1:
     print("Item_name:{}, Item:{}, price:{},  shops: {} ".format(item_name,color,price,shops))

print()
fr = fruits1[2]
print(fr)

shops = fr[3]
print(shops)

shop = shops[1]
print(shop[1])
print()
print("all in one line shop code")
shop = fruits1[2][3][1][1]
print(shop)
print()
print("step by step indexing")
print(fruits1[2])
print(fruits1[2][3])
print(fruits1[2][3][1])
print(fruits1[2][3][1][1])
