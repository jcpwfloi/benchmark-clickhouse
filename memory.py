import pandas as pd

df = pd.read_csv("memory.output", comment='#', header=None)
print(df.var() / (df.mean() ** 2))
