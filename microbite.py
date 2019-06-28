from microbit import *
import radio

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
MOTOR CONTROL
@ScienceOxford code for microbit with L9110s motor driver
http://www.multiwingspan.co.uk/micro.php?page=botline
'''
RF = pin2
RB = pin8
LF = pin1
LB = pin0

# 1023 turns the motors off; 0 turns them on at full speed
def stop():
    LF.write_analog(0)
    LB.write_analog(0)
    RF.write_analog(0)
    RB.write_analog(0)
    display.clear()

# Inputs between 0-1023 to control both motors
def drive(L, R):
    # Below is an adjustment to correct for motor speed discrepancy
    L = L
    R = int(R*0.9)
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        LF.write_analog(abs(L))  # go forwards at speed given
        LB.write_analog(0)         # don't go backwards
    elif L < 0 and L >= -1023:
        LF.write_analog(0)         # don't go forwards
        LB.write_analog(abs(L))  # go backwards at speed given
    else:
        LF.write_analog(0)         # stop the left wheel
        LB.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        RF.write_analog(abs(R))  # go forwards at speed given
        RB.write_analog(0)         # don't go backwards
    elif R < 0 and R >= -1023:
        RF.write_analog(0)         # don't go forwards
        RB.write_analog(abs(R))  # go backwards at speed given
    else:
        RF.write_analog(0)         # stop the right wheel
        RB.write_analog(0)


'''
MAIN LOOP
Receiving messages from controller_joystick.py
'''
stop()
pin15.write_analog(0)
display.show(Image.GIRAFFE)

while True:
    message = radio.receive()
    if message is not None:
        if message == 'stop':
            stop()
        elif message == 'angry':
            display.show(Image.ANGRY)
            pin15.write_analog(100)
        elif message == 'frown':
            display.show(Image.SAD)
        elif message == 'smile':
            display.show(Image.HAPPY)
            pin15.write_analog(65)
        elif message == 'line':
            display.show(Image.DUCK)
            pin15.write_analog(0)
        else:
            message = message.split()
            drive(int(message[0]), int(message[1]))
