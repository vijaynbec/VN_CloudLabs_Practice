log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]
print(log_file)

for msg in log_file:
    print('times')
    if 'INFO' in msg:
        print(msg)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print("break at 3:", number)
for number in numbers:
    if number == 3:
        continue
    print("continue at 3:", number)


# servers=("server1","server2","server3")
# for server in servers: #"${servers[@]}":
#     print('yes')


