import pyttsx3
import time
import os
import bluetooth
import serial
import tkinter
from pyttsx3 import *
from bluetooth import *
from tkinter import *

#from Arduino_Database import *  # something wrong w

serial_speed = 9600
serial_port = 'COM7'

def speak(Engine, Database_info):
    Engine.say(Database_info)
    Engine.runAndWait()     #future check if this command is necessary

#def movements_Arduino():     #which  parameters?
#    data = ser.readline()
#    example = data.decode('utf-8')
#    print(example)
#    try:
#        log.insert('1.0', example)      # basic example of printing instead of the print function below
#    except IndexError:
#          print("RECEIVED INCOMPLETE DATA\n")

#def print_example(master, *args, **kwards):
#    f = Frame(master, height = 20, width = 60)
#    f.pack_propagate(0)
#    label = Label (f, *args, **kwards)
#    label.pack(fill=BOTH, expand=1)

class Database_RealWorld():
    def movements_Database():
        Database_info = 'word'      #have a command to read what is being sent
        if Database_info != " ":    #need database to send " " when info is finished
            log.insert(Database_info, " ")
            speak(Engine, Database_info)
            movements_Database()    #call the function again to check if there are new words    



if __name__ == '__main__':
    ser = serial.Serial(serial_port, serial_speed, timeout=0)
    
    Engine = pyttsx3.init()
   
    master = Tk()
    #master.wm_title("GloVoice")
    #log = Text(master, width=30, height=35, takefocus=0)
  
    #movements_Arduino()
    data = ser.readline()
    example = str(data.decode('utf-8'))
    print("hey")
    print(str(data))
    ser.close()
    #send = Arduino_Database()
    #send.movements_Arduino()
    # have a wait command between sending information and receiving it
    #receive = Database_RealWorld()
    #receive.movements_Database()

    master.mainloop()
