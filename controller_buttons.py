from microbit import *
import radio

'''
Start conditions:
Turn radio on and to channel 12 (to stop interference)
The channel can be between 0 and 100, and will need to be unique to me!
'''
radio.on()

robot = "MicroTrol"
radio.config(channel=12)
radio.config(address=0x12073120)
radio.config(group=31)
display.show(Image.GIRAFFE)
'''
Main program:
Send message string based on which button or external switch pressed.
'''
while True:
    if pin14.read_digital() == 1:
        radio.send("left")
        sleep(1)
    elif pin1.read_digital() == 1:
        radio.send("right")
        sleep(1)
    elif pin16.read_digital() == 1:
        radio.send("forward")
        sleep(1)
    elif pin2.read_digital() == 1:
        radio.send("backward")
        sleep(1)
    elif pin0.read_digital() == 1:
        if robot == "MicroTrol":    #switch to Kitty
            radio.config(channel=12)
            radio.config(address=0x12073121)
            radio.config(group=07)
            display.show(Image.DUCK)
            robot = "Kitty"
        elif robot == "Kitty":      #switch to MicroTrol
            radio.config(channel=12)
            radio.config(address=0x12073120)
            radio.config(group=31)
            display.show(Image.GIRAFFE)
            robot = "MicroTrol"
    else:
        radio.send("stop")
        sleep(1)
