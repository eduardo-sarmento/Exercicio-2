import sys
import multiprocessing
import time
import Exercicio2_client

def main():
    process_number = int(sys.argv[1])
    size = int(sys.argv[2])
    jobs = []
    #process_server = multiprocessing.Process(target=Exercicio2_server.server())
    #jobs.append(process_server)
    for i in range(0, process_number):
        process_client = multiprocessing.Process(target=Exercicio2_client.client(size//process_number))
        jobs.append(process_client)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()
if __name__ == "__main__":
    main()