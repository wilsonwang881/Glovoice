import serial
import time
import Client

# -*- coding: utf-8 -*-

# # Serial port parameters
serial_speed = 115200
serial_port = '/dev/tty.HC-06-DevB' # bluetooth shield hc-06


if __name__ == '__main__':

    file = open("capture.txt","w")#declare txt
    
    print ("conecting to serial port ...")
    ser = serial.Serial(serial_port, serial_speed, timeout=1)
    a = "1"
    one = a.encode("utf-8")
    #ser.write(one)

    print ("recieving message from arduino ...")
    #ser.flushInput()

    

    
	
    for i in range(100):
        #ser.flushInput()
        data = ser.readline()
        
        #print(data)
        file.write(data.decode("utf-8"))
        
        #time.sleep(0.05)
	    
    file.close()
    print(data)
    print ("finish program and close connection!")
