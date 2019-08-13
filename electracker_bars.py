import httplib, urllib, paho.mqtt.client as mqtt
from gpiozero import Button
from time import sleep
from time import time

ldr = Button(4)

barTime = 120  #length of each record cycle

while True:
	flashes = 0
	startTime = time()
	endTime = startTime + barTime
	while time()<=endTime:
	
		ldr.wait_for_release()
		flashes += 1
		#print("flash" + str(flashes))
		sleep(0.07)			
		
	consumption = 1.125/(float(barTime)/float(flashes))
#	print (int(flashes*5)*" " + "* " +str(consumption))

#write to thingspeak:

	try:
		params = urllib.urlencode({'field1': consumption, 'field2': 18,'key':'4WCP4S3W6MJAF4X5'})
		headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
		conn = httplib.HTTPConnection("api.thingspeak.com:80")
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print("Couldn't write to TS")

#write to MQTT

	try: 
		client = mqtt.Client("electrackerpi")
		client.connect("broker.hivemq.com")
		client.publish("78lvdb/burnrate",consumption)
		print("published consumption to MQTT")
	except:
		print("Couldn't write to MQTT")

