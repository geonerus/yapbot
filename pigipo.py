import RPi.GPIO as GPIO
import time
from func import GetState
UPDATE_TIME=600
GPIO.setmode(GPIO.BOARD) 
chan_list = [7,11]    
GPIO.setup(chan_list, GPIO.OUT)
def y():
    GPIO.output(11,True)
    GPIO.output(7,True)
    print('y sets!')
def g():
    GPIO.output(11,True)
    GPIO.output(7,False)
    print('g sets!')
def r():
    GPIO.output(11,False)
    GPIO.output(7,True)
    print('r sets!')    
while 5:
    a=GetState()
    print('update '+a[1])
    if a[0]<4:
        g()
    if 3<a[0]<7:
        y()
    if 6<a[0]:
        r()
    print('sleep start!')
    time.sleep(UPDATE_TIME)
