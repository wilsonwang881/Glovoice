################################ Part 1: Bluetooth Device ########################################
import serial.tools.list_ports
import serial
import time
from sys import exit
import atexit

# function call when exiting the program
@atexit.register
def goodbye():
    print ("You are now leaving the Glovoice client.")
    conn.request("POST","/logout")

#Welcome information
print('Welcome to Glovice')
print('Checking available ports')

#Checking available port and print
list = serial.tools.list_ports.comports()
connected = []

# append the connected device to a list
for element in list:
    connected.append(element.device)

print('Available ports:')

# show all the serial ports with detailed information
if connected:
    for element in list:
        print(element)
else:
    print('No device connected')
    exit()

#Select port
device = str(input('Please enter the device from the above list: '))

#Serial port parameters, HC06
serial_speed = 115200

print ("Conecting to serial port ...")

#Test connectionn to the Bluetooth device
ser = serial.Serial(device, serial_speed, timeout=1)
a = "1"
one = a.encode("utf-8")
print ("Getting 5 samples from Arduino:")
ser.flushInput()

#Display 5 output from the device
test_count = 0

while(test_count<5):
    ser.flushInput()
    data = ser.readline()
    time.sleep(0.05)
    print(data)
    test_count+=1

############################## Part 2: Server Connection ##########################################
import http.client as httplib

print('The default server IP is 52.89.41.142 at port 8080')

# get the server IP and the port
IP_addr = str(raw_input('Please enter the server IP/port if different from the above: '))

#Connect to the server
# will use the default IP when no user input available
if IP_addr:
    conn = httplib.HTTPConnection(IP_addr)
else:
    # IP_addr = '52.89.41.142:8080'
    # conn = httplib.HTTPConnection("52.89.41.142:8080")
    IP_addr = '127.0.0.1:5000'
    conn = httplib.HTTPConnection(IP_addr)

#Test the connection
conn.request("POST","/login")
res = conn.getresponse()

if res.status==200:
    print('Server connected', res.reason,res.read())

############################# Part 3: Send the sensor data ############################################
# set the header
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

display_info = str(raw_input('Do you want to display the incoming data from Arduino?(Y/n) '))

if display_info == 'Y' or display_info == 'y':

    # display sensor readings
    a = "1"
    one = a.encode("utf-8")
    print ("Recieving message from arduino ...")
    ser.flushInput()
    data = ser.readline()
    params = urllib.urlencode({'Readings': data})
    conn = httplib.HTTPConnection(IP_addr)
    conn.request("POST", "/query/client", params, headers)
    res = conn.getresponse()
    reason = res.reason
    params = urllib.urlencode({'Hello world': count})
    read = res.read()

    while(res.status==200):
        ser.flushInput()
        data = ser.readline()
        params = urllib.urlencode({'Readings': data})
        print(data)
        conn = httplib.HTTPConnection(IP_addr)
        conn.request("POST","/query",params,headers)
        res = conn.getresponse()
        reason = res.reason
        read = res.read()
else:

    # hide the sensor readings
    a = "1"
    one = a.encode("utf-8")
    print ("Recieving message from arduino ...")
    ser.flushInput()
    data = ser.readline()
    params = urllib.urlencode({'Readings': data})
    conn = httplib.HTTPConnection(IP_addr)
    conn.request("POST","/query/client",params,headers)
    res = conn.getresponse()
    reason = res.reason
    read = res.read()

    while(res.status==200):
        ser.flushInput()
        data = ser.readline()
        params = urllib.urlencode({'Readings': data})
        conn = httplib.HTTPConnection(IP_addr)
        conn.request("POST","/query",params,headers)
        res = conn.getresponse()
        reason = res.reason
        read = res.read()
