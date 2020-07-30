Ultrasonic sensor -1

import RPi.GPIO as GPIO
import time as t
GPIO.setmode (GPIO.BCM)
trigger=18
echo=23
GPIO.setwarnings(False)
GPIO.setup (trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
while True:
   GPIO.output(trigger,True)
   time.sleep(.0001)
   GPIO.output(trigger,False)
   time.sleep(1)
   while(GPIO.input (echo)==0 ):
      it=time.time()
   while(GPIO.input (echo)== 1):
      ft= time.time()
   tt=ft-it
   distance=(tt*34300)/2
   print (distance)
   time.sleep(2)
