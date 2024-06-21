# Lists are ordered collections of elements. The order in which elements are added
# is preserved. Elements can be accessed by their index. - Mutable and allow duplicates
my_list = [1, 2, 3, 4, 5]
print("list items: ", my_list)
print(my_list[0])  # Output: 1
# Sets are unordered collections of unique elements.
# The order in which elements are added is not preserved.
# Elements cannot be accessed by their index. - Mutable and not allow duplicates
my_set = {1, 2, 3, 4, 5}
print("sets :", my_set)
# Lists
if 3 in my_list:
    print("3 is in the list")

# Sets
if 3 in my_set:
    print("3 is in the set")

#########################################

# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")