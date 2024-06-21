
# listing, break, indexing examples
shop_list=["milk","egg","bread","spam","rice","salt","spam","leaf"]
for item in shop_list:
    if item !="spam":
        print("then buy " + item)
print ("*" * 25)
# same result using continue
for item in shop_list:
    if item =="spam":
        continue
    print("then buy " + item)
print ("*" * 25)
# use break
for item in shop_list:
    if item =="spam":
        break
    print("then buy " + item)
print ("*" * 25)
# use indexing
shop_list=["milk","egg","bread","spam","rice","salt","spam","leaf"]
to_find = "spam"
found_at = None
#index in range
for index in range(len(shop_list)):
    if shop_list[index] == to_find:
        found_at = index
print("Item found at position {}".format(found_at))
print ("*" * 25)
for item in range(len(shop_list)):
    if shop_list[item] == to_find:
        found_at = item
        break
print("Item found at position {}".format(found_at))