from gpiozero import Button,LED
from signal import pause
from subprocess import call
import sys

red = LED(17)
button = Button(2)

def say_hello():
    print("Hello!")
    call(['mpg321','doorbellA.mp3'])
    red.on()

def say_goodbye():
    red.off()

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()
