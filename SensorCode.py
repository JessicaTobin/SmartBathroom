#basic read input gpio4

import RPi.GPIO as GPIO  
from time import sleep    # For pausing
GPIO.setmode(GPIO.BCM)    # BCM numbering, not BOARD
GPIO.setup(4, GPIO.IN)    # Sets pin4 to an input 


try:                      # Doesn't kill the program on an error, goes to finally instead
    while True:           # MASH CTRL+C to stop the program
        
        if GPIO.input(4): # Checks what's up with Pin 4, if it's TRUE or FALSE
            print("I'm reading TRUE on GPIO 4")
            
        else:  
            print("I'm reading FALSE on GPIO 4") 

        sleep(1)          # Wait 1 second before the next reading  
  
finally:                  # When you CTL+C out of the try block, you end up here
    
    print("Cleaning up...")
    GPIO.cleanup()        # Turns off all pins that are still on so the next program runs cleanly
    
    



"""

#inputs changing outputs
import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input (button)  
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(25): # if port 25 == 1  
            print("Port 25 is 1/HIGH/True - LED ON")  
            GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True  
        else:  
            print("Port 25 is 0/LOW/False - LED OFF")  
            GPIO.output(24, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()  
"""
