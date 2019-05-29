import time 
import serial



uart = serial.Serial("/dev/ttyS0",baudrate =31250000)

for i in range(0,5):			
	raw_result = uart.readline()
	print (raw_result)


