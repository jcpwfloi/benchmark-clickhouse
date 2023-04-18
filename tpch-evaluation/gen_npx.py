import pandas as pd
import glob
import re

csvs = glob.glob("*.csv")

ans = None

for csv in csvs:
    name = re.match(r"([\w.]+).csv", csv)[1]
    df = pd.read_csv(csv, comment='#')
    for i in [1, 2]:
        df = df.rename(columns={df.columns[i]: name + "_" + df.columns[i]})
    print(df)
    if ans is None:
        ans = df
    else:
        ans = ans.merge(df, how="outer", left_on="id", right_on="id")

print(ans)
