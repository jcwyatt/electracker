import httplib, urllib
from gpiozero import Button
from time import sleep
from time import time

ldr = Button(4)


old_t = time()
new_t = time()
logOfData=[]
dataPoints=0
while True:
	ldr.wait_for_release()
	old_t = new_t
	new_t = time()
	interval = new_t - old_t
	consumption = 1.125/interval
#	print (int(interval*10)*" " + "* " +str(consumption))

#	print(time())
#write to thingspeak
	params = urllib.urlencode({'field1': consumption, 'field2': 18,'key':'4WCP4S3W6MJAF4X5'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()
	
	

