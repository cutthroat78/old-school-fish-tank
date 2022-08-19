from tkinter import *
from w1thermsensor import W1ThermSensor
while True:
    sensor = W1ThermSensor()
    temp = sensor.get_temperature()
    win = Tk()
    win.geometry("650x250")
    temperature = "Fish Tank Temperature: \n" + str(temp) + " Degrees"
    label= Label(win, text=temperature, font=('Times New Roman bold',60))
    label.pack(padx=0, pady=250)
    label.after(5000, label.master.destroy)
    win.attributes('-fullscreen', True)
    win.mainloop()
