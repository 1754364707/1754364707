import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator
import os
import numpy as np
import matplotlib.pyplot as plt
from wfq import wfq_set

# def gui():


def set_wfq():
    """
    run wfq.py
    set wfq default
    :return:
    """
    PORT = int(PORT_temp.get().strip())
    SENDPORT = int(SENDPORT_temp.get().strip())
    A_weight = float(AWEIGHT_temp.get().strip())
    A_packetsize = int(APACKETSIEZE_temp.get().strip())
    B_weight = float(BWEIGHT_temp.get().strip())
    B_packetsize = int(BPACKETSIEZE_temp.get().strip())
    C_weight = float(CWEIGHT_temp.get().strip())
    C_packetsize = int(CPACKETSIEZE_temp.get().strip())
    wfq_set(PORT,SENDPORT,A_weight, A_packetsize,B_weight, B_packetsize,C_weight, C_packetsize)


def run_destination():
    """
    run destination file
    :return:
    """
    os.system("""
    ./destination
            """
              )


def run_source():
    """
    run source file
    :return:
    """
    os.system("""
    ./sources
            """
              )


window = tk.Tk()
# title
window.title("My project--zjsu || writen by : swx")
# window size
window.geometry('800x210')

# show first line
lbl = Label(window, text="Sender parameters", font=("宋体", 20), anchor="center")
lbl.pack()

# ##### sender config #######
port = Label(window, text='PORT:', font=("宋体", 15), anchor="w").place(x=20, y=50)
PORT_temp = StringVar()
PORT_temp.set('50000')  # default port
port_insert = Entry(window, width=10, font=("宋体", 15), textvariable=PORT_temp).place(x=95,y=48) # port

portsend = Label(window, text='PORTSEND:', font=("宋体", 15), anchor="w").place(x=0, y=80)
SENDPORT_temp = StringVar()
SENDPORT_temp.set('50001')  # default
portsend_insert = Entry(window,width=10,font=("宋体", 15), textvariable=SENDPORT_temp).place(x=95,y=80) # port

# weight config
A = Label(window, text='A_weight:', font=("宋体", 15), anchor="w").place(x=280, y=50)
AWEIGHT_temp = StringVar()
AWEIGHT_temp.set('1.0')  # default
A_insert = Entry(window,width=10,font=("宋体", 15),textvariable=AWEIGHT_temp).place(x=380,y=48) # port

B = Label(window, text='B_weight:', font=("宋体", 15), anchor="w").place(x=280, y=80)
BWEIGHT_temp = StringVar()
BWEIGHT_temp.set('2.0')  # default
B_insert = Entry(window,width=10,font=("宋体", 15),textvariable=BWEIGHT_temp).place(x=380,y=80) # port

C = Label(window, text='C_weight:', font=("宋体", 15), anchor="w").place(x=280, y=110)
CWEIGHT_temp = StringVar()
CWEIGHT_temp.set('0.5')  # default
C_insert = Entry(window,width=10,font=("宋体", 15),textvariable=CWEIGHT_temp).place(x=380,y=112) # port

# packet size config
A_packet = Label(window, text='A_packetsize:', font=("宋体", 15), anchor="w").place(x=550, y=50)
APACKETSIEZE_temp = StringVar()
APACKETSIEZE_temp.set('100')  # default
A_packet_insert = Entry(window,width=10,font=("宋体", 15),textvariable=APACKETSIEZE_temp).place(x=690,y=48) # port

B_packet = Label(window, text='B_packetsize:', font=("宋体", 15), anchor="w").place(x=550, y=80)
BPACKETSIEZE_temp = StringVar()
BPACKETSIEZE_temp.set('50')  # default
B_packet_insert = Entry(window,width=10,font=("宋体", 15),textvariable=BPACKETSIEZE_temp).place(x=690,y=80) # port

C_packet = Label(window, text='C_packetsize:', font=("宋体", 15), anchor="w").place(x=550, y=110)
CPACKETSIEZE_temp = StringVar()
CPACKETSIEZE_temp.set('100')  # default
C_packet_insert = Entry(window,width=10,font=("宋体", 15),textvariable=CPACKETSIEZE_temp).place(x=690,y=112) # port


# lbl = Label(window, text="Receiver parameters", font=("宋体", 20), anchor="center").place(x=270,y=180)
# run source.py #
# button1 = Button(window, text="run destination", command=run_destination,
# font=("宋体", 15)).place(x=100, y=150, height=30)

button2 = Button(window, text="set wfq configs", command=set_wfq, font=("宋体", 15)).place(x=200, y=150, height=30)
button3 = Button(window, text="Start!", command=run_source, font=("宋体", 15)).place(x=500, y=150, height=30)

window.mainloop()
