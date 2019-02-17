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
    x = (pin0.read_analog()) - 519          # stick centre returns zero
    y = (pin1.read_analog()) - 524          # stick centre returns zero
    left = int((y + x) * 1.2)               # adjusts so that highest reading is +/- 1023
    right = int((y - x) * 1.2)
    return str(left) + " " + str(right)


'''
MAIN LOOP
'''
on = False
display.show(Image.NO)

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
        elif button == 'A':
            radio.send('angry')
            sleep(100)
        elif button == 'B':
            radio.send('frown')
            sleep(100)
        elif button == 'C':
            radio.send('smile')
            sleep(100)
        elif button == 'D':
            radio.send('line')
            sleep(100)
        else:
            radio.send(drive())
            sleep(10)
