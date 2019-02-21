from microbit import *
import radio
import neopixel
import random

'''
RADIO CONFIGURATION
IMPORTANT: change the channel/address/group for each robot &
           ensure the channel/address/group match the controller
'''
radio.config(channel=12)
radio.config(address=0x12073120)
radio.config(group=31)
radio.config(queue=1)

radio.on()


'''
MCROBOFACE NEOPIXELS
https://4tronix.co.uk/blog/?p=1383
'''      
mrf = neopixel.NeoPixel(pin0, 17)
smile = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
frown = [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
line = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
angry = [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

def exp(expression):
    red_nose = random.randint(0, 255)
    green_nose = random.randint(0, 255)
    blue_nose = random.randint(0, 255)
    red_eyes = random.randint(0, 255)
    green_eyes = random.randint(0, 255)
    blue_eyes = random.randint(0, 255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    mrf[14] = (red_nose, green_nose, blue_nose)
    for id in range(15, 17):
        mrf[id] = (red_eyes, green_eyes, blue_eyes)
    for id in range(0, 14):
        if (expression[id] != 0):
            mrf[id] = (red, green, blue)
        else:
            mrf[id] = (0, 0, 0)

    mrf.show()


'''
MOTOR CONTROL
@ScienceOxford code for microbit with L9110s motor driver
http://www.multiwingspan.co.uk/micro.php?page=botline
'''
LF = pin14
LB = pin13
RF = pin12
RB = pin15

# 1023 turns the motors off; 0 turns them on at full speed
def stop():
    LF.write_analog(1023)
    LB.write_analog(1023)
    RF.write_analog(1023)
    RB.write_analog(1023)

# Inputs between 0-1023 to control both motors
def drive(L, R):
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        LF.write_analog(abs(L-1023))  # go forwards at speed given
        LB.write_analog(1023)         # don't go backwards
    elif L < 0 and L >= -1023:
        LF.write_analog(1023)         # don't go forwards
        LB.write_analog(abs(L+1023))  # go backwards at speed given
    else:
        LF.write_analog(1023)         # stop the left wheel
        LB.write_analog(1023)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        RF.write_analog(abs(R-1023))  # go forwards at speed given
        RB.write_analog(1023)         # don't go backwards
    elif R < 0 and R >= -1023:
        RF.write_analog(1023)         # don't go forwards
        RB.write_analog(abs(R+1023))  # go backwards at speed given
    else:
        RF.write_analog(1023)         # stop the right wheel
        RB.write_analog(1023)


'''
MAIN LOOP
Receiving messages from controller_joystick.py
'''
stop()
display.show(Image.HAPPY)
exp(smile)

while True:
    message = radio.receive()
    if message is not None:
        if message == 'stop':
            stop()
        elif message == 'angry':
            exp(angry)
            display.show(Image.ANGRY)
        elif message == 'frown':
            exp(frown)
            display.show(Image.SAD)
        elif message == 'smile':
            exp(smile)
            display.show(Image.HAPPY)
        elif message == 'line':
            exp(line)
            display.show(Image.SURPRISED)
        else:
            message = message.split()
            drive(-int(message[0]), -int(message[1]))
