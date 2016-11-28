#program to analyse electricity use over time by hour.

#open a file

#for each hour:
#read it line by line
#bucket into hour
#get total
#get average for each hour

import csv
import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

elecByHour=[]
#date = 21

for i in range (0,24):     #for each hour
			with open ('feeds.csv', 'rb') as csvfile:
				rawelecdata = csv.DictReader(csvfile)

				j=0
				hourelectot=0

				for row in rawelecdata:
					if int(row['created_at'][11:13])==i: #and int(row['created_at'][8:10])==date:
						hourelectot += float(row['field1'])
						j +=1
				
			print(i,hourelectot/j,j) #useful to for debugging

			elecByHour.append(hourelectot/j) #add average for the current hour to list


y = (elecByHour)
N = len(y)
x = range(N)
width = 1/1.5
plt.xlabel ('Time of Day / hr')
plt.ylabel ('kW')
plt.title('Average Consumption over 14 days 14-28 Nov')
plt.bar(x, y, width, color="blue")
plt.savefig('elecByHour.png')

os.system('xviewer elecByHour.png &')








