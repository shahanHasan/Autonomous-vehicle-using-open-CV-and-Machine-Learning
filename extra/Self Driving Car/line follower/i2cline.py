#! /usr/bin/python
# -*- coding:utf-8 -*-
#black 1 white 0 

import RPi.GPIO as GPIO
import time 
from lfreadraw import Line_Follower

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
linef = Line_Follower()

def FollowLine():
	#linef = Line_Follower()
	a = linef.read_digital()
	if (a == small_l ) | (a == small_r) | (a == mid) | (a == mid1):
		Motor_Forward()
		print a[2]
		return
	elif (a == small_l1) | (a == left) | (a == left1):
		Motor_TurnRight()
		print a[1]
		return
	elif (a == small_r1) | (a == right) | (a == right1):
		Motor_TurnLeft()
		print a[3]
		return
	elif (a == stop):#两侧都碰到黑线
		Motor_Stop()
		print linef.read_digital()
		return

	
def Motor_Forward():
	print 'motor forward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)

#def Motor_Forward():
#	print 'motor Backward '
#	GPIO.output(ENA,True)
#	GPIO.output(ENB,True)
#	GPIO.output(IN1,True)
#	GPIO.output(IN2,False)
#	GPIO.output(IN3,True)
#	GPIO.output(IN4,False)

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

#管脚类型设置
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
########电机驱动接口定义#################
ENA = 13	#//L298使能A
ENB = 20	#//L298使能B
IN1 = 19	#//电机接口1
IN2 = 16	#//电机接口2
IN3 = 21	#//电机接口3
IN4 = 26	#//电机接口4
########红外传感器接口定义#################

IR_R = 18	#小车右侧巡线红外
IR_L = 27	#小车左侧巡线红外


#########电机初始化为LOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
#########红外初始化为输入，并内部拉高#########

GPIO.setup(IR_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)


time.sleep(2)
try:
		while True:
			#Motor_Forward()
			#time.sleep(1)
			#Motor_TurnLeft()
			#time.sleep(1)
			#Motor_Backward()
			#time.sleep(1)
			#Motor_TurnRight()	
			FollowLine()
except KeyboardInterrupt:
         GPIO.cleanup()
