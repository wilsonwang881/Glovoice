import serial
import time
# -*- coding: utf-8 -*-

# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06-DevB' # bluetooth shield hc-06


if __name__ == '__main__':
    
    print ("conecting to serial port ...")
    ser = serial.Serial(serial_port, serial_speed, timeout=1)
    a = "1"
    one = a.encode("utf-8")
    #ser.write(one)

    print ("recieving message from arduino ...")
    ser.flushInput()
	
    while(1):
        ser.flushInput()
        data = ser.readline()
        #ser.write(b'200')
        
        print(data)
        time.sleep(0.05)
	    
        
    print ("finish program and close connection!")
