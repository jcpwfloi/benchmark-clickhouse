from tpch import *

worker_init()

for i in range(1, 23):
    query(i, get_query(i))
