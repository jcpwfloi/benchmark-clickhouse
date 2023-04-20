import pandas as pd

keydf = pd.read_csv("key.csv", delimiter=" ", header=None)
valuedf = pd.read_csv("value.csv", header=None)

keys = keydf[1]
values = valuedf[1] * 1000.0
values = values.round().astype('int')

print("auto mapping = std::unordered_map<size_t, ssize_t> {", end="")

outputs = []

for i in range(len(keys)):
    outputs.append("{" + f"{keys[i]}, {values[i]}" + "}")

print(','.join(outputs), end="")

print("};")
