from tpch import *
import time
import sys

rounds = 10
cutoff = 4
stats = []

worker_init()

start = time.time()

for round in range(rounds):
    for i in [1,3,4,5,6,7,8]:
        print(f"running round {round} query {i}")
        elapsed = query(i, get_query(i), do_print=False)
        if round > cutoff:
            stats.append(elapsed)

print(stats)

