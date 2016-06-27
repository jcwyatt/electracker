Electracker Project
===================

A) To monitor electricity consumption
B) To transmit data via MQTT
C) To output data to webpage / hardware display


The monotoring device is a Raspberry Pi hooked up to an LDR which is detecting
the flashes from an electrcity meter. 3200 flashes = 1kWh.  

Monitoring Algorithms - Pros - Cons

1) How many flashes in 10s
	Pros:
	Easy to program
	Fixed reporting interval
	

	Cons:
	Imprecise
	Can't detect small variations
	
2) How long for n flashes
	Pros:
	Easy to program
	Very accurate and precise

	Cons:
	low consumption gives very long reporting intervals

3) Start timing  on flash n, stop on flash n+1
   Do this every 10 s or every flash, whichever is the greater
   (1 flash every 10s = 0.1125kW which never happens!)

	Pros:
	Totally Accurate
	Fairly fixed reporting interval, easy to adjust
	
	Cons:
	Harder to program



