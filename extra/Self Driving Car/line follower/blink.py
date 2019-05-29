import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setwarnings(False)

gpio.setup(10, gpio.OUT,initial=gpio.LOW)

try :
	while True :
		gpio.output(10,True)
		time.sleep(1.0)
		gpio.output(10,False)
		time.sleep(1.0)
except KeyboardInterrupt:

	gpio.cleanup()
