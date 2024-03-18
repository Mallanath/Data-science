# pandas | Compare DataFrames

import pandas as pd

dict = {"Fruits": ["mango", "apples", "banana", "papaya"],
        "Price": [100, 150, 50, 35],
        "Quantity": [15, 10, 10, 3]}

df = pd.DataFrame(dict)
print(df)

df2 = df.copy()

df2.loc[0, "Price"] = 120
df2.loc[1, "Price"] = 175
df2.loc[2, "Price"] = 70
df2.loc[0, "Quantity"] = 12
df2.loc[1, "Quantity"] = 15
df2.loc[2, "Quantity"] = 5

print(df2)

print(df.compare(df2))
print(df.compare(df2, align_axis=0))
print(df.compare(df2, keep_equal=True))
print(df.compare(df2, keep_shape=True))