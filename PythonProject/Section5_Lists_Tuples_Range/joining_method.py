costco = ["shirt",
           "pan",
           "rice",
           "salt",
           "oil",
           "pizza"
          ]
print("-" *10)
print(costco)

print("-" *10)
for item in costco:
     print(item)

print("-" *10)
print(", ".join(costco))

print("-" *10)
sepe = "|"
result=sepe.join(costco)
print(result)
print("-" *10)
sepe = ", "
result=sepe.join(costco)
print(result)

# join works for homegeneous items
costco = ["shirt",
           "pan",
           "rice",
           "salt",
           # 44,  # added to list
           "pizza"
          ]

print("work only for homegeneous items")
print(" ".join(costco))