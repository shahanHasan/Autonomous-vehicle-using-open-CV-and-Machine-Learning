#! /usr/bin/python
# -*- coding:utf-8 -*-
#black 1 white 0 

import smbus
import RPi.GPIO as GPIO
import time 

bus = smbus.SMBus(1)
bus.write_byte_data (0x6f,0x00,0x00)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
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

# GPIO Setup
GPIO.setup(pwm1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in11,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in12,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pwm2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in21,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in22,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pwm3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in31,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in32,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pwm4,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in41,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(in42,GPIO.OUT,initial=GPIO.LOW)

speed = 100
left_speed = 100#duty cycle
frequency = 500 #signal received by pi from motor driver 
#PWM soft
Parallel1 = GPIO.PWM(pwm1,frequency)#ENA right 
Parallel1.start(speed)
Parallel2 = GPIO.PWM(pwm2,frequency)#ENB left
Parallel2.start(speed)
Parallel3 = GPIO.PWM(pwm3,frequency)#ENA right 
Parallel3.start(speed)
Parallel4 = GPIO.PWM(pwm4,frequency)#ENB left
Parallel4.start(speed)

def Motor_Forward():
	print 'motor forward'
	GPIO.output(in11,False)
	GPIO.output(in12,True)
	GPIO.output(in21,False)
	GPIO.output(in22,True)
	GPIO.output(in31,False)
	GPIO.output(in31,True)
	GPIO.output(in41,False)
	GPIO.output(in42,True)

def Motor_Backward():
	print 'motor_backward'
	GPIO.output(in11,True)
	GPIO.output(in12,False)
	GPIO.output(in21,True)
	GPIO.output(in22,False)
	GPIO.output(in31,True)
	GPIO.output(in31,False)
	GPIO.output(in41,True)
	GPIO.output(in42,False)

def Motor_TurnLeft():
	print 'motor_turnleft'
	GPIO.output(in11,True)
	GPIO.output(in12,False)
	GPIO.output(in21,True)
	GPIO.output(in22,False)
	GPIO.output(in31,False)
	GPIO.output(in31,True)
	GPIO.output(in41,False)
	GPIO.output(in42,True)

def Motor_TurnRight():
	print 'motor_turnright'
	GPIO.output(in11,False)
	GPIO.output(in12,True)
	GPIO.output(in21,False)
	GPIO.output(in22,True)
	GPIO.output(in31,True)
	GPIO.output(in31,False)
	GPIO.output(in41,True)
	GPIO.output(in42,False)

def Motor_Stop():
	print 'motor_stop'
	GPIO.output(in11,False)
	GPIO.output(in12,False)
	GPIO.output(in21,False)
	GPIO.output(in22,False)
	GPIO.output(in31,False)
	GPIO.output(in31,False)
	GPIO.output(in41,False)
	GPIO.output(in42,False)


try:
		while True:
			Motor_Forward()
			time.sleep(1)
			Motor_Backward()
			time.sleep(1)
			Motor_Forward()	
		    
except KeyboardInterrupt:
        GPIO.cleanup()
	Parallel1.stop()
	Parallel2.stop()
        Parallel3.stop()
	Parallel4.stop()
