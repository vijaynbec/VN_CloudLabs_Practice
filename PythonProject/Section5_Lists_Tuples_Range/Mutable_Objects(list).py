comp_parts = ["key",   #0   list
              "wire",  #1
              "bottle",  #2
              "cable"]  #3
lab_parts = comp_parts
print(id(comp_parts))
print(lab_parts)  # print before add
comp_parts += ["monitor"]
print(id(comp_parts))  # id wont change
print(comp_parts)  # monitor gets added to list
print(lab_parts)

print("#"*50)
a=b=c=d= lab_parts
print("Adding UPS")
b.append("UPS")
print(b)
print(d)