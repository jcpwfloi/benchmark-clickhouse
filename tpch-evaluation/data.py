import pandas as pd
import glob

names = sorted(glob.glob("*.csv"))

for name in names:
    df = pd.read_csv(name, comment='#')
    df = df[3000:]
    print(name, df['local_elapsed'].mean(), sep=',')
