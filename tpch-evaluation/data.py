import pandas as pd
import glob

names = sorted(glob.glob("*.csv"))

print("load,lambda,E[T]")

for name in names:
    df = pd.read_csv(name, comment='#')
    A = df.copy()
    A = A.sort_values(by="n")
    lmb = 1.0 / A["A"].diff().mean()
    df = df[3000:]
    print(name.replace(".csv", ""), lmb, df['T'].mean(), sep=',')
