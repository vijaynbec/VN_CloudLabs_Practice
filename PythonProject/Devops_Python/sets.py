my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)  # Adding an element
print('my_set.add(6): ', my_set)
my_set.remove(3)  # Removing an element
print('my_set.remove(3): ', my_set)
# union
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)  # Union of sets
print("union_set = set1.union(set2) :Union", union_set)
intersection_set = set1.intersection(set2)  # Intersection of sets
print("intersection_set = set1.intersection(set2) : Intersection", intersection_set)
difference_set = set1.difference(set2)  # Difference of sets
print("difference_set = set1.difference(set2)  # Difference", difference_set)

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
server_name = 'server5'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
