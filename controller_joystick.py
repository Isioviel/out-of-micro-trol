from microbit import *
import radio


'''
RADIO CONFIGURATION
IMPORTANT: change the channel/address/group for each controller &
           ensure the channel/address/group match the robot
'''
radio.config(channel=12)
radio.config(address=0x12073120)
radio.config(group=31)

on = False

display.show(Image.NO)


'''
BUTTON INPUTS
joystick:bit
'''
buttons = {2: 'A',
           516: 'B',
           684: 'C',
           768: 'D',
           853: 'E',
           819: 'F'}

def button_press():
    press = pin2.read_analog()
    if press < 900:
        for number in range(press-5, press+5):
            if number in buttons:
                return buttons[number]


'''
JOYSTICK CONVERSION
joystick:bit
'''
def drive():
    x = (pin0.read_analog()) - 511
    y = (pin1.read_analog()) - 511
    left = y + x
    right = y - x
    return str(left) + " " + str(right)


'''
MAIN LOOP
'''
while True:
    button = button_press()
    if button == 'F':
        radio.on()
        display.show(Image.YES)
        on = True
    while on is True:
        button = button_press()
        if button == 'E':
            radio.send('stop')
            radio.off()
            display.show(Image.NO)
            on = False
        else:
            radio.send(drive())
            sleep(10)