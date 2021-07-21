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



# Abre servidor na porta 8000
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Registra funcoes a serem requeridas
server.register_multicall_functions()
server.register_function(get, 'get')
server.register_function(post, 'post')

# Serve requisicoes indefinidamente
server.serve_forever()
print(hashtable.values())
