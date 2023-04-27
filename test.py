from tpch import *

worker_init()

for i in [1,3,4,5,6,7,8]:
    query(i, get_query(i))
