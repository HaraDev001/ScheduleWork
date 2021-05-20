import pandas as pd
import os

df = pd.DataFrame({'name': ['Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello','Raphael', 'Donatello',],
                   'mask': ['red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple','red', 'purple',],
                   'weapon': ['sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff','sai', 'bo staff',]})

df.to_csv(r"file3.txt",index=False, sep='\t', mode='a', header=False,encoding='utf-8-sig')