server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
print(" list of server and ips")

print("list  status is", server_config.get('server1').get('status'))

for key, value in server_config.items():
    print(key)
    # if key="server1":
    #     print ("Hi I am in")    print(value)
print(server_config['server1'].get('ip'))


def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")