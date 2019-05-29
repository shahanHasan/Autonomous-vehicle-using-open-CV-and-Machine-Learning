#! /usr/bin/python
# -*- coding:utf-8 -*-
#black 1 white 0 

import RPi.GPIO as GPIO
#import lcddriver
import time 
from lfreadraw import Line_Follower

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ENA =  8	#//L298使能A
ENB =  6	#//L298使能B
IN1 = 11	#//电机接口1
IN2 =  7	#//电机接口2
IN3 = 12	#//电机接口3
IN4 =  5	#//电机接口4

# GPIO Setup
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

speed = 100
	#duty cycle
frequency = 500 #frequency of signal received by pi from motor driver 

#PWM soft
Parallel1 = GPIO.PWM(ENA,frequency)
Parallel1.start(speed)
Parallel2 = GPIO.PWM(ENB,frequency)
Parallel2.start(speed)

#follow black line
#mid 	=[0,0,1,0,0]	# Middle Position.
#mid1	=[0,1,1,1,0]	# Middle Position.
#small_l	=[0,1,1,0,0]	# Slightly to the left.
#small_l1=[0,1,0,0,0]	# Slightly to the left.
#small_r	=[0,0,1,1,0]	# Slightly to the right.
#small_r1=[0,0,0,1,0]	# Slightly to the right.
#left	=[1,1,0,0,0]	# Slightly to the left.
#left1	=[1,0,0,0,0]	# Slightly to the left.
#right	=[0,0,0,1,1]	# Sensor reads strongly to the right.
#right1	=[0,0,0,0,1]	# Sensor reads strongly to the right.
#stop	=[1,1,1,1,1]	# Sensor reads stop.
#stop1	=[0,0,0,0,0]	# Sensor reads stop.
#follow white line
mid 	=[1,1,0,1,1]	# Middle Position.
mid1	=[1,0,0,0,1]	# Middle Position.
small_l	=[1,0,0,1,1]	# Slightly to the left.
small_l1=[1,0,1,1,1]	# Slightly to the left.
small_r	=[1,1,0,0,1]	# Slightly to the right.
small_r1=[1,1,1,0,1]	# Slightly to the right.
left	=[0,0,1,1,1]	# Slightly to the left.
left1	=[0,1,1,1,1]	# Slightly to the left.
right	=[1,1,1,0,0]	# Sensor reads strongly to the right.
right1	=[1,1,1,1,0]	# Sensor reads strongly to the right.
stop	=[1,1,1,1,1]	# Sensor reads stop.
stop1	=[0,0,0,0,0]	# Sensor reads stop.





array1 = [0,0,0,0,0]
#lcd = lcddriver.lcd()
#lcd.lcd_clear()	
linef = Line_Follower()

def FollowLine():
	#linef = Line_Follower()
	a = linef.read_digital()
	if (a == stop1 ) | (a == small_l ) | (a == small_r) | (a == mid) | (a == mid1):
		Motor_Forward()
		print a[2]
		#lcd.lcd_display_string(print(a), 1 )

		return
	elif (a == small_l1) | (a == left) | (a == left1):
		Motor_TurnLeft()
		print a[1]
		#lcd.lcd_display_string(print(a), 1 )
		return
	elif (a == small_r1) | (a == right) | (a == right1):
		Motor_TurnRight()
		print a[3]
		#lcd.lcd_display_string(print(a), 2 )
		return
	elif (a == stop):#两侧都碰到黑线
		Motor_Backward()
		print linef.read_digital()
		#lcd.lcd_display_string(print(a), 2 )
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

try:
		while True:
			Motor_Forward()
			time.sleep(1)
			Motor_TurnLeft()
			time.sleep(1)
			Motor_Backward()
			time.sleep(1)
			Motor_TurnRight()	
			#FollowLine()
except KeyboardInterrupt:
        GPIO.cleanup()
	Parallel1.stop()
	Parallel2.stop()
