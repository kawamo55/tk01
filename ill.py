#!/usr/bin/python3
import tkinter as tk
import wiringpi as wir
import numpy as np

# setup gpio and tk
wir.wiringPiSetupGpio()
rt=tk.Tk()
lb1=tk.Label(text="push exit button on stop program !!")
lb1.pack()
btn=tk.Button(text="--- exit ---",command=lambda: rt.quit())
btn.pack()

# control pin and time span
pino=[17,18,22,23]
tspn=300

# set pin
for i in range(0,len(pino)):
    wir.pinMode(pino[i],wir.GPIO.OUTPUT)

def tmloop():
    r=np.random.randint((1 << len(pino))-1)
    for i in range(0,4):
        if (r & (1 << i)):
           wir.digitalWrite(pino[i],1)
        else:
           wir.digitalWrite(pino[i],0)
    rt.after(tspn,tmloop)

tmloop()
rt.mainloop()

# reset pin
for i in range(0,len(pino)):
    wir.digitalWrite(pino[i],0)

