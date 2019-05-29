#! /usr/bin/python
# -*- coding:utf-8 -*-
#black 1 white 0 

import RPi.GPIO as GPIO
import time 
from lfreadraw import Line_Follower

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ENA = 13	#//L298使能A
ENB = 20	#//L298使能B
IN1 = 19	#//电机接口1
IN2 = 16	#//电机接口2
IN3 = 21	#//电机接口3
IN4 = 26	#//电机接口4

# GPIO Setup
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

right_speed = 100
left_speed = 100#duty cycle
frequency = 500 #signal received by pi from motor driver 
#PWM soft
Parallel1 = GPIO.PWM(ENA,frequency)#ENA right 
Parallel1.start(right_speed)
Parallel2 = GPIO.PWM(ENB,frequency)#ENB left
Parallel2.start(left_speed)


#follow black line
#just 1 sensor on black
midfwd	 =[0,0,1,0,0] # move forward
rightfwd =[0,0,0,1,0] #turn slight right
leftfwd	 =[0,1,0,0,0] #turn slight left
leftmost =[1,0,0,0,0] #turn left
rightmost=[0,0,0,0,1] #turn right

#just 2 sensors on black
midfwd1  =[0,0,1,1,0] #move forward
midfwd2  =[0,1,1,0,0] #move forward
rightfwd2=[0,0,0,1,1] #turn right
leftfwd2 =[1,1,0,0,0] #turn left

#just 3 sensors on black
midfwd3   =[0,1,1,1,0] #move forward
leftfwd3  =[1,1,1,0,0] #turn left
rightfwd3 =[0,0,1,1,1] #turn right

#just 4 sensors on black
rightfwd4=[0,1,1,1,1] #turn right
leftfwd4 =[1,1,1,1,0] #turn left

#just 5 sensors on black or white
stop1=[1,1,1,1,1] #stop
stop =[0,0,0,0,0] #move backward


linef = Line_Follower()

def FollowLine():
	#linef = Line_Follower()
	a = linef.read_digital()
	if (a == midfwd) | (a == midfwd1)|(a == midfwd2)|(a==midfwd3):
		Motor_Forward()
		print a
		return
	elif (a==rightfwd)|(a==rightmost)|(a==rightfwd2):
		Motor_TurnRight()
		print a
		return
	elif (a == rightfwd3)|(a == rightfwd4):
		while (a==midfwd1):		
		 Motor_TurnRight()
		 print a
		return
	elif (a == leftfwd3)|(a == leftfwd4):
		Motor_TurnLeft()
		print a
		return
	elif (a==leftfwd)|(a==leftmost)|(a==leftfwd2):
		Motor_TurnLeft()
		print a
		return
	
	elif (a == stop1):#on black completely
		Motor_Stop()
		print linef.read_digital()
		return
	elif (a == stop): #line lost  
		Motor_Backward()
		print a
		return


def Motor_Forward():
	print 'motor forward'
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
	

def Motor_Backward():
	print 'motor_backward'
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)

def Motor_TurnLeft():
	print 'motor_turnleft'
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)

def Motor_TurnRight():
	print 'motor_turnright'
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)

def Motor_Stop():
	print 'motor_stop'
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
def Motor_turnleft():
	print 'motor turning left'
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
def Motor_turnright():
	print 'motor turning right'
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
	

try:
		while True:
			#Motor_Forward()
			#time.sleep(1)
			#Motor_TurnLeft()
			#time.sleep(1)
			#Motor_Backward()
			#time.sleep(1)
			#Motor_turnright()	
			FollowLine()
except KeyboardInterrupt:
        GPIO.cleanup()
	Parallel1.stop()
	Parallel2.stop()
