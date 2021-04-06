# tkinter for creating graphical interface(GUI)
# Rpi.GPIO for using the general purpose input/output pins of the Rpi
# sleep for creating delays (or times) to keep motor on, buttons pressed, delays, etc.
import Tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

#declaring the pins we're using for this project
# 20,21 are for relays for fan, and speakers
GPIO21 = 21
GPIO20 = 20
#22,27 for CD4066 IC to mimic pressing the buttons on the projector
GPIO22Power = 22
GPIO27Confirm = 27
#23,24,25, to the lm298 h-bridger to control speed and direction of the motor 
in1 = 24
in2 = 23
en = 25
# sets modes of the Rpi pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
GPIO.setup(GPIO22Power, GPIO.OUT)
GPIO.setup(GPIO27Confirm, GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
# initializes the pins LOW (OFF) for the motor
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
# Sets the PWM signal for the motor
p=GPIO.PWM(en,1000)
p.start(60)
# creates the visual interface of the AV system
master = tk.Tk()
master.title("ROBINSON'S AVControl")
master.geometry("350x175")
# initializes the state(on or off) of the speaker and fan
GPIO21_state = True
GPIO20_State = True
# function for turning the speakers on or off. If GPIO_state is'true' it turns on the speakers, changes the state to 'false' and changes the message to asking if you want to turn the speakers off.
def GPIO21button():
  global GPIO21_state
  if GPIO21_state == True:
    GPIO.output(GPIO21, GPIO21_state)
    GPIO21_state = False
    ONlabel = tk.Label(master, text="Turn OFF?", fg="red")
    ONlabel.grid(row=0, column=1)
  else:
    GPIO.output(GPIO21, GPIO21_state)
    GPIO21_state = True
    ONlabel = tk.Label(master, text="Turn ON?", fg="blue")
    ONlabel.grid(row=0, column=1)
#function for the projector to turn on.  This lowers the projector, turns on the projector through the use of the CD4066 to mimic button presses and turns on the fan.
def GPIO20button():
  global GPIO20_State
  if GPIO20_State == True:
                #turn on motor
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                sleep(.25)
                #turns off motor
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                sleep(.25)
                GPIO.output(GPIO20, GPIO20_State)
                GPIO20_State = False
                # mimics button press for 15 milliseconds
                GPIO.output(GPIO22Power,GPIO.HIGH)
                sleep(0.15)
                # 'releases' the button
                GPIO.output(GPIO22Power,GPIO.LOW)
                # changes the message next to the button 
                OFFlabel = tk.Label(master, text="Turn OFF?", fg="red")
                OFFlabel.grid(row=4, column=1)
  else:
                # turns off the projector, turns off the fan, etc.
                GPIO.output(GPIO20, GPIO20_State)
                GPIO20_State = True
                GPIO.output(GPIO22Power,GPIO.HIGH)
                sleep(0.15)
                GPIO.output(GPIO22Power,GPIO.LOW)
                sleep(0.15)
                GPIO.output(GPIO27Confirm,GPIO.HIGH)
                sleep(0.15)
                GPIO.output(GPIO27Confirm,GPIO.LOW)
                OFFlabel = tk.Label(master, text="Turn ON?", fg="blue")
                OFFlabel.grid(row=4, column=1)
                sleep(0.15)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                sleep(.25)
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
# up and down buttons for adjusting the vertical angle of the projector by moving the motor.  motor stays on for 1 millisecond at a time
def upButton():
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                sleep(0.1)
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
def downButton():
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                sleep(0.1)
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)

# creates the interface (GUI)
ONbutton = tk.Button(master, text="Speakers", bg="blue",fg="white", command=GPIO21button)
ONbutton.grid(row=0, column=0)
ONbutton.config( height = 2, width = 7)
Blanklabel1 = tk.Label(master, text="                         ")
Blanklabel1.grid(row=0, column=1)
OFFbutton = tk.Button(master, text="Projector",bg="blue" ,fg="white", command=GPIO20button)
OFFbutton.grid(row=4, column=0)
OFFbutton.config( height = 2, width = 7)
Blanklabel2 = tk.Label(master, text="                         ")
Blanklabel2.grid(row=2, column=1)
Upbutton = tk.Button(master, text="UP",bg="grey", command=upButton)
Upbutton.grid(row=0, column=20)
Upbutton.config( height = 3, width = 3)
Blanklabel4 = tk.Label(master, text="                         ")
Blanklabel4.grid(row=1, column=1)
Blanklabel3 = tk.Label(master, text="Adjust Projector Angle")
Blanklabel3.grid(row=2, column=20)
Blanklabel5 = tk.Label(master, text="                         ")
Blanklabel5.grid(row=3, column=1)
Downbutton = tk.Button(master, text="DOWN",bg="grey", command=downButton)
Downbutton.grid(row=4, column=20)
Downbutton.config( height = 3, width = 3)
master.mainloop()