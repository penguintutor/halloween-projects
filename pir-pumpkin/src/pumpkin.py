from gpiozero import MotionSensor
from neopixel import *
import time

delay = 10
PIRPIN = 26

LEDCOUNT = 150
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True
BRIGHTNESS = 255


pir =  MotionSensor(PIRPIN)
strip = Adafruit_NeoPixel(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)
strip.begin()

while True:

    pir.wait_for_motion()
    print ("you can't hide")
    for i in range (0,LEDCOUNT,2):
        strip.setPixelColor(i, Color(255,0,0))
        strip.setPixelColor(i+1, Color(0,0,255))
    strip.show()
    time.sleep(delay)
    for i in range (LEDCOUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
