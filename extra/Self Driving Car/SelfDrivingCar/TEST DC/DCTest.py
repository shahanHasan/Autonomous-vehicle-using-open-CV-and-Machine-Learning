#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit
from Raspi_PWM_Servo_Driver import PWM

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)
pwm = PWM(0x6F)
pwm2 = PWM(0x6f)
servoMin = 05   # Min pulse length out of 4096
servoMax = 350  # Max pulse length out of 4096

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def setServoPulse(channel, pulse):
	pulseLength = 1000000               # 1,000,000 us per second
	pulseLength /= 60                   # 60 Hz
	print ("%d us per period" % pulseLength)
	pulseLength /= 4096                 # 12 bits of resolution
	print ("%d us per bit" % pulseLength)
	pulse *= 1000
	pulse /= pulseLength
	pwm.setPWM(channel, 0, pulse)
	pwm2.setPWM(channel , 0, pulse)

################################# DC motor test!
myMotor  = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)
# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.FORWARD);

myMotor2.setSpeed(150)
myMotor2.run(Raspi_MotorHAT.FORWARD);

myMotor3.setSpeed(150)
myMotor3.run(Raspi_MotorHAT.FORWARD);

myMotor4.setSpeed(150)
myMotor4.run(Raspi_MotorHAT.FORWARD);

# turn on motor
myMotor.run(Raspi_MotorHAT.RELEASE);
myMotor2.run(Raspi_MotorHAT.RELEASE);
myMotor3.run(Raspi_MotorHAT.RELEASE);
myMotor4.run(Raspi_MotorHAT.RELEASE);

# servo 

pwm.setPWMFreq(60)
pwm2.setPWMFreq(60)                        # Set frequency to 60 Hz


while (True):
	print ("Forward! ")
	myMotor.run(Raspi_MotorHAT.FORWARD)
	myMotor2.run(Raspi_MotorHAT.FORWARD)
	myMotor3.run(Raspi_MotorHAT.FORWARD)
	myMotor4.run(Raspi_MotorHAT.FORWARD)
	pwm.setPWM(0, 0, servoMin)
	#pwm2.setPWM(14, 0, servoMin)


	print ("\tSpeed up...")
	for i in range(255):
		myMotor.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
		myMotor4.setSpeed(i)
		time.sleep(0.01)

	print ("\tSlow down...")
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
		myMotor4.setSpeed(i)
		time.sleep(0.01)

	print ("Backward! ")
	myMotor.run(Raspi_MotorHAT.BACKWARD)
	myMotor2.run(Raspi_MotorHAT.BACKWARD)
	myMotor3.run(Raspi_MotorHAT.BACKWARD)
	myMotor4.run(Raspi_MotorHAT.BACKWARD)
	pwm.setPWM(0, 0, servoMax)
	#pwm2.setPWM(14, 0, servoMax)
	

	print ("\tSpeed up...")
	for i in range(255):
		myMotor.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
		myMotor4.setSpeed(i)
		time.sleep(0.01)

	print ("\tSlow down...")
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		myMotor2.setSpeed(i)
		myMotor3.setSpeed(i)
		myMotor4.setSpeed(i)
		time.sleep(0.01)

	print ("Release")
	myMotor.run(Raspi_MotorHAT.RELEASE)
	myMotor2.run(Raspi_MotorHAT.RELEASE)
	myMotor3.run(Raspi_MotorHAT.RELEASE)
	myMotor4.run(Raspi_MotorHAT.RELEASE)
	pwm.setPWM(0, 0, servoMin)
  	#pwm2.setPWM(14, 0, servoMin)

	time.sleep(1.0)
