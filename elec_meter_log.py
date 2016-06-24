
#!/usr/bin/env python
     
#First go with the LDR picking up the flashes from the electrcity meter.
     
import RPi.GPIO as GPIO, time, os
import sqlite3


#initiaise database tools
conn = sqlite3.connect('elecmeter03.db')
c =  conn.cursor()

#create database
#what to send to db: unixtime, 
#c.execute("CREATE TABLE e_meterlog02 (time float, power float, meter_reading integer)")

#initialise pins     
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



#procedure to wait for LED flash front edge
def wait_for_flash():
    try:
        GPIO.wait_for_edge(23,GPIO.RISING)
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit 
        conn.commit()
        conn.close()

meter_rdg = 0
impulse_count=0

#timing and kW calcs based on 800 imp / kWh
start_time=time.time()

for i in range (0,40):
    wait_for_flash()
    elapsed_time = time.time()-start_time
    start_time=time.time()
    if impulse_count < 800:
        impulse_count += 1
    else:
        meter_rdg +=1
        impulse_count=0
        conn.commit()
    kW=((1/elapsed_time)*4.5)
#    print (elapsed_time,kW,meter_rdg,impulse_count)
    c.execute("INSERT into e_meterlog02 VALUES(?,?,?)",(time.asctime(),kW,meter_rdg))
    time.sleep(0.3) #to allow for LED to turn off
    
GPIO.cleanup()           # clean up GPIO on normal exit        
conn.commit()
conn.close()

print("Ending PRogram")

