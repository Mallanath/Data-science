# Piviting and Melting

import pandas as pd

# dict = {"keys": ["k1", "k2", "k1", "k2"],
#         "Names": ["John", "mallanath","king", "David"],
#         "House": ["red", "blue", "green", "red"],
#         "Grades": ["3rd", "8th", "9th", "8th"]}

# df = pd.DataFrame(dict)
# print(df)
# print(df.pivot(index="keys", columns="Names", values=["House", "Grades"]))

dict = {"Names": ["John", "mallanath","king", "David"],
        "House": ["red", "blue", "green", "red"],
        "Grades": ["3rd", "8th", "9th", "8th"]}

df = pd.DataFrame(dict)
print(df)

print(df.melt(id_vars=["Names"], value_vars=["House", "Grades"], var_name="House&Grades", value_name="values"))