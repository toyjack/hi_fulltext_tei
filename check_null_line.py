import pandas as pd
from pandas.core.base import NoNewAttributesMixin
from tqdm import tqdm
import time

e08=pd.read_csv('./data/TBL_M_E08_list.txt',sep='\t',na_values='null',header=None)
e22=pd.read_csv("./data/e22.zip", sep="\t", header=None)
def get_null_cols(data):
  results=[]
  for col in data:
    for cell in data[col]:
      if not pd.isnull(cell):
        results.append("not_all_null")
        break
    results.append("all_null")
  return results

# print(e22.head())
e22_header_isNull= get_null_cols(e22)
print(e22_header_isNull)