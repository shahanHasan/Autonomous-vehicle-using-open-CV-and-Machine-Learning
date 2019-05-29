#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import lcddriver
import time
import atexit
from Raspi_PWM_Servo_Driver import PWM
import RPi.GPIO as gpio

class Drive:

    '''
    move FORWARD,BACKWARD,LEFT,RIGHT,HARDLeft,HARDRight,Stop
    '''
    def __init__(self):
        # an object of class motor
        self.mh = Raspi_MotorHAT(0x6f)
        # creating object servo
        self.pwm= PWM(0x6f)
        self.PWM2 = PWM(0x6f)
        # creating object lcd
        self.lcd = lcddriver.lcd()
        # creating 4 motors
        self.myMotor1= self.mh.getMotor(1)
        self.myMotor2= self.mh.getMotor(2)
        self.myMotor3= self.mh.getMotor(3)
        self.myMotor4= self.mh.getMotor(4)
        # servo min and max turn
        self.servoMin = 5
        self.servoMax = 250

    def Forward(self):
        # move forward
        print ("Forward! ")
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
        self.myMotor3.run(Raspi_MotorHAT.FORWARD)
        self.myMotor4.run(Raspi_MotorHAT.FORWARD)

        self.myMotor1.setSpeed(100)
        self.myMotor2.setSpeed(100)
        self.myMotor3.setSpeed(100)
        self.myMotor4.setSpeed(100)

        self.lcd.lcd_display_string("FORWARD", 1)

    def Backward(self):
        # move BACKWARD
        print ("Backward! ")
        self.myMotor1.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor2.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor3.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor4.run(Raspi_MotorHAT.BACKWARD)

        self.myMotor1.setSpeed(100)
        self.myMotor2.setSpeed(100)
        self.myMotor3.setSpeed(100)
        self.myMotor4.setSpeed(100)

        self.lcd.lcd_display_string("BACKWARD", 1)

    def Stop(self):
        # stop
        print('Stop')
    	self.myMotor1.run(Raspi_MotorHAT.RELEASE)
    	self.myMotor2.run(Raspi_MotorHAT.RELEASE)
    	self.myMotor3.run(Raspi_MotorHAT.RELEASE)
    	self.myMotor4.run(Raspi_MotorHAT.RELEASE)

    	#atexit.register(turnOffMotors)

        self.lcd.lcd_display_string("STOP", 1)

    def SpinLeft(self):
        # spin left
        print('Spin left')
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
        self.myMotor3.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor4.run(Raspi_MotorHAT.BACKWARD)

        self.myMotor1.setSpeed(100)
        self.myMotor2.setSpeed(100)
        self.myMotor3.setSpeed(100)
        self.myMotor4.setSpeed(100)

        self.lcd.lcd_display_string("Spin left", 1)

    def SpinRight(self):
        # spin right
        print('Spin right')
        self.myMotor1.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor2.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor3.run(Raspi_MotorHAT.FORWARD)
        self.myMotor4.run(Raspi_MotorHAT.FORWARD)

        self.myMotor1.setSpeed(100)
        self.myMotor2.setSpeed(100)
        self.myMotor3.setSpeed(100)
        self.myMotor4.setSpeed(100)

        self.lcd.lcd_display_string("Spin right", 1)

    def MoveHardLeft(self):
        # forward hard left
        print('Mover Hard left')
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
        self.myMotor3.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor4.run(Raspi_MotorHAT.BACKWARD)

        self.myMotor1.setSpeed(150)
        self.myMotor2.setSpeed(150)
        self.myMotor3.setSpeed(50)
        self.myMotor4.setSpeed(50)

        self.lcd.lcd_display_string("Move Hard Left", 1)

    def MoveHardRight(self):
        # forward hard right
        print('Move Hard Right')
        self.myMotor1.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor2.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor3.run(Raspi_MotorHAT.FORWARD)
        self.myMotor4.run(Raspi_MotorHAT.FORWARD)

        self.myMotor1.setSpeed(50)
        self.myMotor2.setSpeed(50)
        self.myMotor3.setSpeed(150)
        self.myMotor4.setSpeed(150)

        self.lcd.lcd_display_string("Spin Hard Right", 1)

    def MoveLightLeft(self):
        # forward slight left
        print('Move slight left')
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
        self.myMotor3.run(Raspi_MotorHAT.FORWARD)
        self.myMotor4.run(Raspi_MotorHAT.FORWARD)

        self.myMotor1.setSpeed(120)
        self.myMotor2.setSpeed(120)
        self.myMotor3.setSpeed(40)
        self.myMotor4.setSpeed(40)

        self.lcd.lcd_display_string("Move Light Left", 1)

    def MoveLightRight(self):
        # forward slight right
        print('Move slight right')
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        self.myMotor2.run(Raspi_MotorHAT.FORWARD)
        self.myMotor3.run(Raspi_MotorHAT.FORWARD)
        self.myMotor4.run(Raspi_MotorHAT.FORWARD)

        self.myMotor1.setSpeed(40)
        self.myMotor2.setSpeed(40)
        self.myMotor3.setSpeed(120)
        self.myMotor4.setSpeed(120)

        self.lcd.lcd_display_string("Spin Light Right", 1)

    def main(self):
        try:
            while(True):
                self.Forward()
                time.sleep(1)
		self.lcd.lcd_clear()

                self.Backward()
                time.sleep(1)
		self.lcd.lcd_clear()

                self.Stop()
                time.sleep(5)
		self.lcd.lcd_clear()

                self.SpinLeft()
                time.sleep(5)
		self.lcd.lcd_clear()

                self.SpinRight()
                time.sleep(5)
		self.lcd.lcd_clear()

                self.MoveHardLeft()
                time.sleep(5)
		self.lcd.lcd_clear()
		
                self.MoveHardRight()
                time.sleep(5)
		self.lcd.lcd_clear()

                self.MoveLightLeft()
                time.sleep(5)
		self.lcd.lcd_clear()
		
                self.MoveLightRight()
                time.sleep(5)
		self.lcd.lcd_clear()

        except KeyboardInterrupt:
            #self.Stop()
            self.lcd.lcd_clear()
	    self.myMotor1.run(Raspi_MotorHAT.RELEASE)
    	    self.myMotor2.run(Raspi_MotorHAT.RELEASE)
    	    self.myMotor3.run(Raspi_MotorHAT.RELEASE)
    	    self.myMotor4.run(Raspi_MotorHAT.RELEASE)		
	

if __name__ == "__main__":

    Drive().main()
