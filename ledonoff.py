import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
led1=27
led2=10
GPIO.setup(led1,GPIO.OUT)

while True:
	GPIO.output(led1,1)
	print('led on')
	time.sleep(1)
	GPIO.output(led1,0)
	print('led off')
	time.sleep(1)
GPIO.cleanup() 
