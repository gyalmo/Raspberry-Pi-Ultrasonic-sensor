#Ultrasonic Sensor -3

import RPi.GPIO as GPIO
import time as time
def USR():
   GPIO.setup (16,GPIO.IN)
   GPIO.setup (20,GPIO.OUT)
   GPIO.setup (20,GPIO.HIGH)
   time.sleep(0.00001)
   GPIO.output(20,GPIO.LOW)
    time.sleep(0.0001) 
    while(GPIO.input(16)==0):
        it=time.time()
    while(GPIO.input(10)==1):
        ft=time.time()
    tt=ft-it
    print (“at the distance of”,tt*34200/2)
def IR():

    GPIO.setup(12,GPIO.IN)
    if(GPIO.input(12)==1):
        print (“Object Found”)
        USR()
    else:
        print (“Object not Found”)
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False):
while (1):
     IR()
