import pandas as pd
table = {'Apples' : pd.Series([35, 41],
                              index=['2017 Sales', '2018 Sales']),
         'Bananas' : pd.Series([21, 34],
                               index=['2017 Sales', '2018 Sales'])}

df = pd.DataFrame(table)

print(df)