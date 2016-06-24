#!/usr/bin/env python
     
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
     
import RPi.GPIO as GPIO, time, os
import sqlite3

#initiaise database tools
conn = sqlite3.connect('20150320_eclipse.db')
c =  conn.cursor()

#create database
c.execute("CREATE TABLE eclipse (date text, level integer)")



     
#read light level from GPIO
DEBUG = 1
GPIO.setmode(GPIO.BCM)
  
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
     
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
     
for i in range (0,10):
    lilev= (RCtime(23)) # Read RC timing using pin #23
    print (lilev) 
    print (time.asctime())
    c.execute("INSERT into eclipse VALUES(?,?)",(time.asctime(),lilev))
    conn.commit()
    time.sleep(2)

conn.close()
        


