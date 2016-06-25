from gpiozero import Button

ldr = Button(4)

i = 0

while True:
	ldr.wait_for_press()
	print("It got dark")
	i +=1
	print (i)

'''def hello():
    print("Hello")

def bye():
    print("Bye")

button.when_pressed = hello
button.when_released = bye
'''

