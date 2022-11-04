import pandas as pd
import json
import tkinter as tk
a=pd.read_excel("tab_1.xlsx",index_col=0,header=None)
#print(a)
b=a.to_json(orient="split")
b=json.loads(b)
print(b)
v_name=b["index"]
print(v_name[1])
v_data=b["data"]
print(int(v_data[1][0]))

d=a.to_json(orient="split")
d=json.loads(d)
print(d)
v_name=b["index"]
print(v_name[0])
v_data=b["data"]
print(int(v_data[0][0]))

q=a.to_json(orient="split")
q =json.loads(q)
print(q)
v_name=q["index"]
print(v_name[2])
v_data=q["data"]
print(int(v_data[2][0]))

x=a.to_json(orient="split")
x=json.loads(x)
print(x)
v_name=x["index"]
print(v_name[4])
v_data=x["data"]
print(int(v_data[4][0]))


import tkinter as tk
window=tk.Tk()
window.geometry("300x150")
def onclick():
    print(1)
voltage_tk=tk.Label(window,text=(v_name[0])+str("  ")+str(v_data[0][0]),font=("Arial",15))
voltage_tk.grid(column=0,row=0)

current_tk=tk.Label(window,text=(v_name[1])+str("  ")+str(v_data[1][0]),font=("Arial",15))
current_tk.grid(column=0,row=1)

power_tk=tk.Label(window,text=(v_name[2])+str("  ")+str(v_data[2][0]),font=("Arial",15))
power_tk.grid(column=0,row=2)

resistance_tk=tk.Label(window,text=(v_name[4])+str("  ")+str(v_data[4][0]),font=("Arial",15))
resistance_tk.grid(column=0,row=3)
resistance_tk=tk.Label(window,text=(v_name[3])+str("  ")+str(v_data[3][0]),font=("Arial",15))
resistance_tk.grid(column=0,row=4)
window.mainloop()
