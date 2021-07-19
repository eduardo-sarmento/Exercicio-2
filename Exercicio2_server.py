from xmlrpc.server import SimpleXMLRPCServer

hashtable = {}

def get(x):
    print(hashtable[x])
    if x in hashtable.values():
        return hashtable[x]
    else:
        return None;

    

def post(x):
    hashtable[x] = x
    return True



    # A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(get, 'get')
server.register_function(post, 'post')
server.serve_forever()
print(hashtable.values())
