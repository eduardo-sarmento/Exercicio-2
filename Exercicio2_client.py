import xmlrpc.client
import random
import sys
def client(n):
    numeros = n

    # Conecta com o servidor
    proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")
    multicall = xmlrpc.client.MultiCall(proxy)

    # Gera números e chama post e get do servidor
    for i in range(numeros):
        r = random.randint(-1000000,1000000)
        multicall.post(r)
        multicall.get(r)
        result = multicall()
        print(tuple(result))