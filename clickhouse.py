import clickhouse_driver
from multiprocessing import Pool
import random
import sys
import os
import time
import numpy as np

N = 100000
N_POOL = 100

queries = ""

with open("queries.sql", "r") as f:
    queries = f.read()

queries = queries.split('\n')[:-1]

def query(id, sql):
    global connection
    start = time.time()
    try:
        connection.execute(sql)
    except e:
        print(e)
    client_elapsed = time.time() - start
    elasped = connection.last_query.elapsed
    print(f"{id},{elasped},{client_elapsed}", flush=True, file=sys.stderr)

def worker_init():
    global connection
    connection = clickhouse_driver.Client(host="localhost", port=9000, database='default')

def get_query(num):
    return queries[num]

def get_random_query():
    return get_query(random.randint(0, 43))

def get_interarrival_time():
    return random.expovariate(0.1)

if __name__ == '__main__':
    with Pool(N_POOL, initializer=worker_init) as pool:
        for i in range(N):
            pool.apply_async(query, (i, get_random_query()))
            time.sleep(get_interarrival_time())
        pool.close()
        pool.join()
