import clickhouse_driver
from multiprocessing import Pool
import random
import sys
import os
import time
import numpy as np

N = 20000
N_POOL = 100

lmb = float(sys.argv[1])
print(f"#lambda={lmb}")
print("id,local_elapsed,remote_elapsed")

query_start = []

def query(id, sql):
    global connection
    start = time.time()
    try:
        connection.execute(sql)
    except e:
        print(e)
    client_elapsed = time.time() - start
    elapsed = connection.last_query.elapsed
    #print(f"{id},{elasped},{client_elapsed}", flush=True)
    return id, elapsed

def worker_init():
    global connection
    connection = clickhouse_driver.Client(host="localhost", port=9000, database='tpcm')

def get_query(num):
    sql_file = "../tpch-clickhouse/ch%02d.sql" % num
    with open(sql_file, "r") as f:
        return f.read()

def get_random_query():
    return get_query(random.randint(1, 22))

def get_interarrival_time():
    return random.expovariate(lmb)

def print_stats(result):
    id, elapsed = result
    local_elapsed = time.time() - query_start[id]
    print(f"{id},{local_elapsed},{elapsed}", flush=True)

def print_error(e):
    print(e, flush=True, file=sys.stderr)

if __name__ == '__main__':
    with Pool(N_POOL, initializer=worker_init) as pool:
        for i in range(N):
            query_start.append(time.time())
            result = pool.apply_async(query, (i, get_random_query()), callback=print_stats, error_callback=print_error)
            time.sleep(get_interarrival_time())
        pool.close()
        pool.join()
