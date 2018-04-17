"""
An entire file for you to expand. Add methods here, and the client should be
able to call them with json-rpc without any editing to the pipeline.
"""
from gpiozero import Button,LED
from subprocess import call

red = LED(17)
button = Button(2)


# def toggle_led(isOn):
#     if(isOn):
#         red.on()
#     else:
#         red.off()

def toggle_led(isOn):
    if(isOn):
        red.on()
        call(['mpg321','../doorbellA.mp3'])
        red.off()

