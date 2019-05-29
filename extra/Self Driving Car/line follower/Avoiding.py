

import RPi.GPIO as GPIO

import time



def	Avoiding():

	if GPIO.input(IR_M) == False:

		Motor_Stop()

	else:

		Motor_Forward()


def Motor_Forward():

	print 'motor forward'

	GPIO.output(ENA,True)

	GPIO.output(ENB,True)

	GPIO.output(IN1,True)

	GPIO.output(IN2,False)

	GPIO.output(IN3,True)

	GPIO.output(IN4,False)

def Motor_Backward():

	print 'motor_backward'

	GPIO.output(ENA,True)

	GPIO.output(ENB,True)

	GPIO.output(IN1,False)

	GPIO.output(IN2,True)

	GPIO.output(IN3,False)

	GPIO.output(IN4,True)

def Motor_TurnLeft():

	print 'motor_turnleft'

	GPIO.output(ENA,True)

	GPIO.output(ENB,True)

	GPIO.output(IN1,True)

	GPIO.output(IN2,False)

	GPIO.output(IN3,False)

	GPIO.output(IN4,True)

def Motor_TurnRight():

	print 'motor_turnright'

	GPIO.output(ENA,True)

	GPIO.output(ENB,True)

	GPIO.output(IN1,False)

	GPIO.output(IN2,True)

	GPIO.output(IN3,True)

	GPIO.output(IN4,False)

def Motor_Stop():

	print 'motor_stop'

	GPIO.output(ENA,False)

	GPIO.output(ENB,False)

	GPIO.output(IN1,False)

	GPIO.output(IN2,False)

	GPIO.output(IN3,False)

	GPIO.output(IN4,False)




GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)



ENA = 13

ENB = 20

IN1 = 19

IN2 = 16

IN3 = 21

IN4 = 26





IR_M = 22





GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)



GPIO.setup(IR_M,GPIO.IN,pull_up_down=GPIO.PUD_UP)





time.sleep(2)

try:

		while True:

			Motor_Forward()
			time.sleep(0.1)
			Motor_Backward()
			time.sleep(0.1)

except KeyboardInterrupt:

         GPIO.cleanup()
