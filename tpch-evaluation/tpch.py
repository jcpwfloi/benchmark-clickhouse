import clickhouse_driver
from multiprocessing import Pool
import random
import sys
import os
import time
import numpy as np

N = 20000
N_POOL = 100

def get_query(num):
    sql_file = "../tpch-clickhouse/ch%02d.sql" % num
    with open(sql_file, "r") as f:
        return f.read()

queries = [""]

for i in range(1, 23):
    queries.append(get_query(i))

lmb = float(sys.argv[1])
print(f"#lambda={lmb}")
print("#,query,T,clickhouse+tcp,clickhouse")

query_start = []

def query(id, query_id, sql):
    global connection
    start = time.time()
    try:
        connection.execute(sql)
    except e:
        print(e)
    client_elapsed = time.time() - start
    elapsed = connection.last_query.elapsed
    #print(f"{id},{elasped},{client_elapsed}", flush=True)
    return id, query_id, client_elapsed, elapsed

def worker_init():
    global connection
    connection = clickhouse_driver.Client(host="localhost", port=9000, database='tpcm')

def get_interarrival_time():
    return random.expovariate(lmb)

def print_stats(result):
    id, query_id, client_elapsed, elapsed = result
    local_elapsed = time.time() - query_start[id]
    print(f"{id},{query_id},{local_elapsed},{client_elapsed},{elapsed}", flush=True)

def print_error(e):
    print(e, flush=True, file=sys.stderr)

if __name__ == '__main__':
    with Pool(N_POOL, initializer=worker_init) as pool:
        for i in range(N):
            query_id = random.randint(1, 22)
            query_start.append(time.time())
            result = pool.apply_async(query, (i, query_id, queries[query_id]), callback=print_stats, error_callback=print_error)
            time.sleep(get_interarrival_time())
        pool.close()
        pool.join()
