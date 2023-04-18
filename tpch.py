import clickhouse_driver
from multiprocessing import Pool
import random
import sys
import os
import time
import numpy as np

N = 100000
N_POOL = 128

lmb = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
print(f"#lambda={lmb}")

def query(id, sql, do_print=True):
    global connection
    start = time.time()
    try:
        connection.execute(sql)
    except e:
        print(e)
    client_elapsed = time.time() - start
    elapsed = connection.last_query.elapsed
    if do_print:
        print(f"{id},{elapsed},{client_elapsed}", flush=True)
    return elapsed

def worker_init():
    global connection
    connection = clickhouse_driver.Client(host="localhost", port=9000, database='tpc')

def get_query(num):
    sql_file = "tpch-clickhouse/ch%02d.sql" % num
    with open(sql_file, "r") as f:
        return f.read()

def get_random_query():
    return get_query(random.randint(1, 22))

def get_interarrival_time():
    return random.expovariate(lmb)

if __name__ == '__main__':
    with Pool(N_POOL, initializer=worker_init) as pool:
        for i in range(N):
            pool.apply_async(query, (i, get_random_query()))
            time.sleep(get_interarrival_time())
        pool.close()
        pool.join()
