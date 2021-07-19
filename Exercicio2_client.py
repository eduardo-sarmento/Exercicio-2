import xmlrpc.client
import random
import sys
def client(n):
    numeros = n
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    multicall = xmlrpc.client.MultiCall(proxy)
    for i in range(numeros):
        r = random.random()
        multicall.post(r)
        multicall.get(r)
        result = multicall()
        print(tuple(result))
        #print("hashtable inserted=%r, hashtable[x]=%d" % tuple(result))