import pandas as pd
import numpy as np


def neg_red(x):
    return f"color:{'red' if x < 0 else 'white'}"


df = pd.DataFrame(np.random.normal(size=(6, 6)), columns=[x for x in 'ABCDEF'])
print(df)
df.style.applymap(neg_red)
print(df)
