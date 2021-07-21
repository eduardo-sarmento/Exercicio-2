import sys
import multiprocessing
import time
import Exercicio2_client

# 
def main():
    process_number = int(sys.argv[1]) # Número de processos a ser criado
    size = int(sys.argv[2]) # quantidade de números a serem criados

    start_time = time.time()

    jobs = []

    # Cria processos e divide a quantidade m de requisicoes entre eles 
    for i in range(0, process_number):
        process_client = multiprocessing.Process(target=Exercicio2_client.client(size//process_number))
        jobs.append(process_client)

    # Inicia todos os jobs
    for j in jobs:
        j.start()

    # Assegura que todas os jobs terminaram
    for j in jobs:
        j.join()

    elapsed = time.time()-start_time

    print("All clients served. Elapsed: {}".format(elapsed))
if __name__ == "__main__":
    main()