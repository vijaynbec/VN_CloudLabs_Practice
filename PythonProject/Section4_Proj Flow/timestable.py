# for loop inside other loop
for i in range (1,5):
    for j in range (1,6):
        print("{0} in time {0} is {2}".format(j,i,i*j))
    print ("*" * 80)
