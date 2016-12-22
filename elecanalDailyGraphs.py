#program to analyse electricity use over time by hour.

#open a file

#for each hour:
#read it line by line
#bucket into hour
#get total
#get average for each hour

#enhancements to follow: daily charts, date range charts, movie!

import csv
import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt



startDay = 20
startMonth = 12

while True:
	elecByHour=[]
	dailyTotal=0
	dailyReadings=0

	for i in range (0,24):     #for each hour
				with open ('feeds.csv', 'rb') as csvfile:
					rawelecdata = csv.DictReader(csvfile)
					
					j=0
					hourelectot=0

					for row in rawelecdata:
						if int(row['created_at'][11:13])==i and int(row['created_at'][8:10])==startDay and int(row['created_at'][5:7])==startMonth:
							hourelectot += float(row['field1'])
							j +=1
					
				print(i,hourelectot/j,j) #useful to for debugging

				elecByHour.append(hourelectot/j) #add average for the current hour to list

				#calculate average for day:
				dailyTotal = dailyTotal + hourelectot
				dailyReadings = dailyReadings + j


	dailyAverage = dailyTotal/dailyReadings

	y = (elecByHour)
	N = len(y)
	x = range(N)
	width = 1/1.5
	plt.xlabel ('Time of Day / hr')
	plt.ylabel ('kW')
	plt.ylim((0,6))
	plt.title('Consumption for '+ str(startDay) + '/' + str(startMonth) + ' Average = ' + str(dailyAverage)+'kW')
	plt.bar(x, y, width, color="blue")
	plt.savefig('elecByHour' + str(startMonth) + str(startDay) + '.png')
	plt.close()
	#os.system('xviewer elecByHour.png &')
	startDay += 1










