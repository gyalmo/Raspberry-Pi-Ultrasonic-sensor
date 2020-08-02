#Ultrasonic sensor -2

import RPi.GPIO as GPIO
import time as t
GPIO.setmode (GPIO.BCM)
trigger =18 
echo =16
GPIO.setwarnings (False)
GPIO.setup (trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
while True:
  GPIO.output(trigger,True)
   t.sleep(0.0001)
   GPIO.output (trigger,False)
   t.sleep(1)
   while(GPIO.input(echo)==0):
      starttime = t.time           #total time
   while(GPIO.input(echo)==1):
      totaltime=stoptime-starttime   #totaltime=stoptime-starttime 
   distance=(totaltime*34300)/2
   print (distance)
t.sleep(2)
