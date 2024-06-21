read_example = open('sampleread.txt', 'r')
# # extra line between eac new lines
# for line in read_example:
#     print(line)    # extra line between eac new lines
#     print(len(line))
# no extra line between eac new lines
for no_line in read_example:
    print(no_line, end='')           # no extra line between eac new lines
    print(no_line.strip())       # rstrip helps for right string strip and lstrip helps for left hand
    print(len(no_line))
read_example.close()
