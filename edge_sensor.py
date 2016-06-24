#!/usr/bin/env python
     
# Example for edge sensing on pin 23 using a LDR and Resistor in series

#thanks to Alex Eames @ http://raspi.tv for the useful hints

#Outline:
#1)set pin low
#2)wait for falling edge
#3)start timer
#4)Wait for rising edge
#5)stop timer and log or print time since last event
#6)reset and restart timer
#7) repeat
     
import RPi.GPIO as GPIO, time, os

#procedure to wait for transit light-->dark
def wait_for_flash():
    try:
        GPIO.wait_for_edge(23,GPIO.RISING)
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit 

#initialise pins     
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#timing
tot_time=0
start_time=time.time()

for i in range (0,20):
    wait_for_flash()
    elapsed_time = time.time()-start_time
    start_time=time.time()
    kW=((1/elapsed_time)*4.5)
    print (elapsed_time,kW)
    tot_time = tot_time + elapsed_time
    time.sleep(0.3)
    
GPIO.cleanup()           # clean up GPIO on normal exit        

print("Ending PRogram. total time =",tot_time)

