from microbit import *
import radio
import neopixel
import random

radio.on()
radio.config(channel=12)
radio.config(address=0x12073120)
radio.config(group=31)

AIA = pin14
AIB = pin13
BIA = pin16
BIB = pin15
on = 0
off = 1

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


def stop():
    AIA.write_digital(off)
    AIB.write_digital(off)
    BIA.write_digital(off)
    BIB.write_digital(off)
    display.show(Image.HAPPY)
    exp(smile)


def forward():
    AIA.write_digital(on)
    AIB.write_digital(off)
    BIA.write_digital(on)
    BIB.write_digital(off)
    display.show(Image.ANGRY)
    exp(angry)


def backward():
    AIA.write_digital(off)
    AIB.write_digital(on)
    BIA.write_digital(off)
    BIB.write_digital(on)
    display.show(Image.ARROW_S)
    exp(line)


def left_turn():
    AIA.write_digital(off)
    AIB.write_digital(on)
    BIA.write_digital(on)
    BIB.write_digital(off)
    display.show(Image.ARROW_W)
    exp(smile)


def right_turn():
    AIA.write_digital(on)
    AIB.write_digital(off)
    BIA.write_digital(off)
    BIB.write_digital(on)
    display.show(Image.ARROW_E)
    exp(smile)


stop()

while True:
    sleep(2)
    message = radio.receive()
    if message is not None:
        if message == "forward":
            forward()
        elif message == "backward":
            backward()
        elif message == "left":
            left_turn()
        elif message == "right":
            right_turn()
        elif message == "stop":
            stop()
    else:
        stop()

'''
Next step:
    write_analog() for finer control
Issues to solve:
    error at random times (not related to neopixels as also happens with Kitty)
    expression changes so frequently, colours look white
'''
