import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.normal(size=(6, 6)),
                  columns=[x for x in 'ABCDEF'])
print(df)
