#! /usr/bin/python
# -*- coding:utf-8 -*-
#black 1 white 0 

import RPi.GPIO as GPIO
import time 
import sys
sys.path.append("./lib")
import i2c_lib

class Motor_Test(object):
        

        def __init__(self, addr=0x60):
               
		self.deviceaddress = i2c_lib.i2c_device(addr)
                pwm1 = 8	
		in11 = 10
		in12 = 9
		pwm2 = 13
		in21 = 11
		in22 = 12
		pwm3 = 2
		in31 = 4 
		in32 = 3
		pwm4 = 7	
		in41 = 5	
		in42 = 6
		self.pwm1 = pwm1
		self.pwm2 = pwm2
		self.pwm3 = pwm3
		self.pwm4 = pwm4
		self.in11=in11
		self.in12=in12
		self.in21=in21
		self.in22=in22
		self.in31=in31
		self.in32=in32
		self.in41=in41
		self.in42=in42
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
                	

        def gpiosetup(self):        
                # GPIO Setup
                GPIO.setup(self.pwm1,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in11,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in12,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.pwm2,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in21,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in22,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.pwm3,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in31,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in32,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.pwm4,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in41,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(self.in42,GPIO.OUT,initial=GPIO.LOW)

        def pwmsetup(self):
                speed = 100
                left_speed = 100#duty cycle
                frequency = 500 #signal received by pi from motordriver 
                #PWM soft
                Parallel1 = GPIO.PWM(self.pwm1,frequency)#ENA right 
                Parallel1.start(speed)
                Parallel2 = GPIO.PWM(self.pwm2,frequency)#ENB left
                Parallel2.start(speed)
                Parallel3 = GPIO.PWM(self.pwm3,frequency)#ENA right 
                Parallel3.start(speed)
                Parallel4 = GPIO.PWM(self.pwm4,frequency)#ENB left
                Parallel4.start(speed)

        def Motor_Forward(self):
                print 'motor forward'
		
                GPIO.output(self.pwm1,True)
                GPIO.output(self.pwm2,True)
		GPIO.output(self.pwm3,True)
                GPIO.output(self.pwm4,True)		
                GPIO.output(self.in11,False)
                GPIO.output(self.in12,True)
                GPIO.output(self.in21,False)
                GPIO.output(self.in22,True)
                GPIO.output(self.in31,False)
                GPIO.output(self.in31,True)
                GPIO.output(self.in41,False)
                GPIO.output(self.in42,True)

        def Motor_Backward(self):
                print 'motor_backward'
		GPIO.output(self.pwm1,True)
                GPIO.output(self.pwm2,True)
		GPIO.output(self.pwm3,True)
                GPIO.output(self.pwm4,True)
                GPIO.output(self.in11,True)
                GPIO.output(self.in12,False)
                GPIO.output(self.in21,True)
                GPIO.output(self.in22,False)
                GPIO.output(self.in31,True)
                GPIO.output(self.in31,False)
                GPIO.output(self.in41,True)
                GPIO.output(self.in42,False)

        def Motor_TurnLeft(self):
                print 'motor_turnleft'
		GPIO.output(self.pwm1,True)
                GPIO.output(self.pwm2,True)
		GPIO.output(self.pwm3,True)
                GPIO.output(self.pwm4,True)
                GPIO.output(self.in11,True)
                GPIO.output(self.in12,False)
                GPIO.output(self.in21,True)
                GPIO.output(self.in22,False)
                GPIO.output(self.in31,False)
                GPIO.output(self.in31,True)
                GPIO.output(self.in41,False)
                GPIO.output(self.in42,True)

        def Motor_TurnRight(self):
                print 'motor_turnright'
		GPIO.output(self.pwm1,True)
                GPIO.output(self.pwm2,True)
		GPIO.output(self.pwm3,True)
                GPIO.output(self.pwm4,True)
                GPIO.output(self.in11,False)
                GPIO.output(self.in12,True)
                GPIO.output(self.in21,False)
                GPIO.output(self.in22,True)
                GPIO.output(self.in31,True)
                GPIO.output(self.in31,False)
                GPIO.output(self.in41,True)
                GPIO.output(self.in42,False)

        def Motor_Stop(self):
                print 'motor_stop'
                GPIO.output(self.in11,False)
                GPIO.output(self.in12,False)
                GPIO.output(self.in21,False)
                GPIO.output(self.in22,False)
                GPIO.output(self.in31,False)
                GPIO.output(self.in31,False)
                GPIO.output(self.in41,False)
                GPIO.output(self.in42,False)

if __name__ == '__main__':
	lf = Motor_Test(addr = 0x6f)
	lf.gpiosetup()
        while True:
		  lf.Motor_Forward()
		  time.sleep(1)
		  lf.Motor_Backward()
		  time.sleep(1)
		  lf.Motor_Forward()	
          
