import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)
time.sleep(0.5)
print "LED ON"
GPIO.output(18,GPIO.HIGH)
time.sleep(0.5)
print "on-on-on"
GPIO.output(18,GPIO.LOW)
time.sleep(0.4)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(18,GPIO.LOW)
time.sleep(0.3)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(18,GPIO.LOW)
time.sleep(0.2)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.2)
GPIO.output(18,GPIO.LOW)
time.sleep(0.1)
GPIO.output(18,GPIO.HIGH)
time.sleep(0.1)
GPIO.output(18,GPIO.LOW)
