# readlines good for the short memory as it converts to list which fits into memory
read_example = open('sa_readlines.txt', 'r')
print(read_example.readlines())
read_example.close()