import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()
while(True):
	lcd.lcd_display_string("my name is -" , 1 )
	lcd.lcd_display_string("Godmode" , 2 )
	lcd.lcd_display_string("ok -" , 3 )
	lcd.lcd_display_string("my name is -" , 4 )

