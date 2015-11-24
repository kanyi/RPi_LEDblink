#https://www.youtube.com/watch?v=41IO4Qe5Jzw
#explainingcomputers.com
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
for x in range(0,50):
    GPIO.output(12,True)
    time.sleep(0.2)
    GPIO.output(12,False)
    time.sleep(0.2)
GPIO.cleanup() 
