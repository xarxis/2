#работа с таблицей
import pandas as pd
import json
a=pd.read_excel("tab_1.xlsx",index_col=0,header=None)
print(a)
b=a.to_json(orient="split")
b=json.loads(b)
print(b)
v_name=b["index"]
print(v_name[0])
v_data=b["data"]
print(int(v_data[0][0]))
d=a.to_json(orient="split")
d=json.loads(b)
print(b)
p_name=b["index"]
print(v_name[1])
p_data=b["data"]
print(int(v_data[2][2]))