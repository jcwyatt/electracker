import httplib, urllib
from gpiozero import Button
from time import sleep
from time import time

ldr = Button(4)

barTime = 60 #length of each record cycle

while True:
	flashes = 0
	startTime = time()
	endTime = startTime + barTime
	while time()<=endTime:
	
		ldr.wait_for_release()
		flashes += 1
		sleep(0.7)			
	
	consumption = 1.125/(barTime/flashes)
#	print (int(flashes*5)*" " + "* " +str(consumption))

#write to thingspeak:

	params = urllib.urlencode({'field1': consumption, 'field2': 18,'key':'4WCP4S3W6MJAF4X5'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()

