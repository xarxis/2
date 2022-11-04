import tkinter as tk
import json
with open('weather.json','r') as f:
    weather=json.load(f)
    temp=weather["fact"]["temp"]
    condition = weather["fact"]["condition"]

    window = tk.Tk()
    window.geometry("300x150")

temp_tk= tk.Label(window ,text="Температура"+str(temp))
temp_tk.grid(column=0,row=0)

temp_image = tk.PhotoImage(file="gradus.png")
temp_image1=tk.Label(image=temp_image)
temp_image1.grid(column=1,row=0)

condition_tk= tk.Label(window ,text="Погода"+str(condition))
condition_tk.grid(column=0,row=1)

overcast_image = tk.PhotoImage(file="oblako.png.")
overcast_image1=tk.Label(image=overcast_image)
overcast_image1.grid(column=1,row=1)
window.mainloop()