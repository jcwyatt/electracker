from gpiozero import Button
from time import sleep
from time import time

ldr = Button(4)


old_t = time()
new_t = time()
while True:
	ldr.wait_for_release()
	old_t = new_t
	new_t = time()
	interval = new_t - old_t
	print (int(interval*10)*" " + "*")
	sleep (0.07)
	

'''while True:
	def hello():
    		print("Hello")
		x = time()
		print (x)
		return x

	def bye():
    		print("Bye")
		y = time()
		print (y)
		return y
	
	ldr.when_pressed = hello = q
	ldr.when_released = bye
	print (q)
'''
