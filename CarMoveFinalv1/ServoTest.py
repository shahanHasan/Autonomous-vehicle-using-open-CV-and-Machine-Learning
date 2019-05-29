#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time

class ServoTest:
    '''
    servo test
    '''
    # Initialise the PWM device using the default address
    # bmp = PWM(0x40, debug=True)
    pwm = PWM(0x6F)
    pwm2 = PWM(0x6f)
    servoMin = 05   # Min pulse length out of 4096
    servoMax = 350  # Max pulse length out of 4096

    def setServoPulse(channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print ("%d us per period" % pulseLength)
    pulseLength /= 4096                     # 12 bits of resolution
    print ("%d us per bit" % pulseLength)
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)
    pwm2.setPWM(channel , 0, pulse)

    pwm.setPWMFreq(60)
    pwm2.setPWMFreq(60)                        # Set frequency to 60 Hz

if __name__ : '__main__':
    while (True):
    # Change speed of continuous servo on channel O
    pwm.setPWM(0, 0, servoMin)
    #pwm2.setPWM(14, 0, servoMin)

    time.sleep(1)
    pwm.setPWM(0, 0, servoMax)
    #pwm2.setPWM(14, 0, servoMax)

    time.sleep(1)
