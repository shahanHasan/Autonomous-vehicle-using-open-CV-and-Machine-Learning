from Motor_Test import Motor_Test

import time

# create a default object, no changes to I2C address or frequency
mt = Motor_Test(addr=0x6f)

while (True):
                mt.Motor_Forward()
                time.sleep(1)
                mt.Motor_Backward()
                time.sleep(1)
                mt.Motor_Forward()
                time.sleep(1)
