from gpiozero import Button

ldr = Button(4)

i = 0

while True:
	ldr.wait_for_press()
	print("It got dark")
	i +=1
	print (i)



