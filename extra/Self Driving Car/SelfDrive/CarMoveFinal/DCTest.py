#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import lcddriver
import time
import atexit
from Raspi_PWM_Servo_Driver import PWM
import RPI.GPIO as gpio

class test:
	'''
	create default objects
	'''
	# create a default object, no changes to I2C address or frequency
	mh = Raspi_MotorHAT(addr=0x6f)
	pwm = PWM(0x6F)
	pwm2 = PWM(0x6f)
	servoMin = 05   # Min pulse length out of 4096
	servoMax = 350  # Max pulse length out of 4096
	lcd = lcddriver.lcd()
	# recommended for auto-disabling motors on shutdown!
	def turnOffMotors():
                mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
                mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
                mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
                mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

                #atexit.register(turnOffMotors)

	# to set the pulse/ not necessary
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
	'''
	creating 4 motors
	'''
	myMotor  = mh.getMotor(1)
	myMotor2 = mh.getMotor(2)
	myMotor3 = mh.getMotor(3)
	myMotor4 = mh.getMotor(4)

	def extraTest():

                # set the speed to start, from 0 (off) to 255 (max speed)
                myMotor.setSpeed(150)
                myMotor.run(Raspi_MotorHAT.FORWARD);
                # turn on motor
                myMotor.run(Raspi_MotorHAT.RELEASE);

	pwm.setPWMFreq(60)
	pwm2.setPWMFreq(60)# Set frequency to 60 Hz

	def main():
		try:

			while (True):
                                print ("Forward! ")
                                myMotor.run(Raspi_MotorHAT.FORWARD)
                                myMotor2.run(Raspi_MotorHAT.FORWARD)
                                myMotor3.run(Raspi_MotorHAT.FORWARD)
                                myMotor4.run(Raspi_MotorHAT.FORWARD)
                                pwm.setPWM(0, 0, servoMin)
                                pwm2.setPWM(14, 0, servoMin)
                                lcd.lcd_clear()
                                lcd.lcd_display_string("FORWARD" , 1 )


                                print ("\tSpeed up...")
                                for i in range(255):
                                        myMotor.setSpeed(i)
                                        myMotor2.setSpeed(i)
                                        myMotor3.setSpeed(i)
                                        myMotor4.setSpeed(i)
                                        time.sleep(5.0)

                                print ("\tSlow down...")
                                for i in reversed(range(255)):
                                        myMotor.setSpeed(i)
                                        myMotor2.setSpeed(i)
                                        myMotor3.setSpeed(i)
                                        myMotor4.setSpeed(i)
                                        time.sleep(5.0)

                                print ("Backward! ")
                                myMotor.run(Raspi_MotorHAT.BACKWARD)
                                myMotor2.run(Raspi_MotorHAT.BACKWARD)
                                myMotor3.run(Raspi_MotorHAT.BACKWARD)
                                myMotor4.run(Raspi_MotorHAT.BACKWARD)
                                pwm.setPWM(0, 0, servoMax)
                                pwm2.setPWM(14, 0, servoMax)
                                lcd.lcd_clear()
                                lcd.lcd_display_string("BACKWARD" , 1 )


                                print ("\tSpeed up...")
                                for i in range(255):
                                        myMotor.setSpeed(i)
                                        myMotor2.setSpeed(i)
                                        myMotor3.setSpeed(i)
                                        myMotor4.setSpeed(i)
                                        time.sleep(5.0)

                                print ("\tSlow down...")
                                for i in reversed(range(255)):
                                        myMotor.setSpeed(i)
                                        myMotor2.setSpeed(i)
                                        myMotor3.setSpeed(i)
                                        myMotor4.setSpeed(i)
                                        time.sleep(5.0)

                                print ("Release")
                                myMotor.run(Raspi_MotorHAT.RELEASE)
                                myMotor2.run(Raspi_MotorHAT.RELEASE)
                                myMotor3.run(Raspi_MotorHAT.RELEASE)
                                myMotor4.run(Raspi_MotorHAT.RELEASE)
                                lcd.lcd_clear()
                                lcd.lcd_display_string("RELEASE" , 1 )
                                #ideal servo location 350
                                pwm.setPWM(0, 0, servoMin)
                                pwm2.setPWM(14, 0, servoMin)
                                time.sleep(5.0)
                                
		except KeyboardInterrupt:
			lcd.lcd_clear()
			myMotor.run(Raspi_MotorHAT.RELEASE)
                        myMotor2.run(Raspi_MotorHAT.RELEASE)
                        myMotor3.run(Raspi_MotorHAT.RELEASE)
                        myMotor4.run(Raspi_MotorHAT.RELEASE)

if __name__ == "__main__":
	test().main()
