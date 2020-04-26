import ssd1306
import machine
import time
i2c = machine.I2C(scl=machine.Pin(5),sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128,32,i2c)
character = '|'
void = " "
fill = "-"
range_max = 5
breaths = 6

for i in range(0,breaths):
  for i in range(0,range_max):
    oled.fill(0)
    text = (range_max-i)*void+character + i*fill + character + i*fill + character
    oled.text('Breathe in',22,3)
    oled.text(text,10,15)
    oled.show()
    time.sleep(1)
  for i in range(range_max-1,-1,-1):
    oled.fill(0)
    text = (range_max-i)*void+character + i*fill + character + i*fill + character
    oled.text('Breathe out',22,3)
    oled.text(text,10,15)
    oled.show()
    time.sleep(1)
    
oled.fill(0)
oled.text("Congrats!",5,0)
oled.text("You took "+str(breaths),5,10)
oled.text("deep breaths!",5,20)
oled.show()
