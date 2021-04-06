# raspberrypiHomeTheatre

** I have changed the projector to a new model with a remote control so I no longer use the CD4066 to turn on the projector itself.  But I'm including that code in case you have a projector that doesn't include a remote control.
**this project involves some soldering and high voltages(110) BE CAREFULL

A personal project for using raspberry pi as a home theatre. Using a raspberry pi B+, and a projector to make a home entertainment system.  I added a few extra features using the GPIO pins to control the following:
-A relay for the speakers
-A relay for fans
-"pressing" the projector power button using a CD4066 IC Quad Bilateral switch. For turning the projector off, I had to press another button to confirm shutdown on the projector, I used another set of the pins on the CD4066 to do this. (take a look at Brainy Bits youtube video to understand how this IC works -> https://www.youtube.com/watch?v=re51EJibEmA)
-an lm298 motor driver- I used this to lower and raise the projector initially when I click the projector button, as well as to adjust the angle when I push the up or down buttons

## Short explanation of how the system functions

I use VNC to have access to the Raspberry Pi from my cellphone, this way I can see the desktop without lowering the projector.  
-From my phone I open the AV control (developed with Python)
-I can turn on the speakers independently to use the system for music, using Youtube on Chromium browser from the Raspberry Pi.(this is done by clicking the "speakers" button which runs the GPIO21button() function in the program)
-When the "projector" button is clicked the program runs the following sequence(GPIO20button() function in the program):
1.  GPIO pins 23, 24, and 25 connected to the lm298 activate the motor to lower the projector.(I use time--sorry!  I could have used a sensor to know when it had reached the desired angle but I didn't).
2.  When the motor stops lowering the projector, the fan is turn on by the relay switch which is connected to GPIO pin 20.
3.  The projector is switched on through the CD4066 IC connected to GPIO 22.(this mimic a button press, so GPIO 22 goes HIGH, waits(sleeps) for 15 milliseconds, and then goes LOW).

For shutting down the projector, the steps run more or less in reverse order, except that the CD4066 IC now "presses" the power button on the projector, which displays a message asking to confirm the shutdown, so I use another set of pins on the IC, to mimic the confirmation button being pressed.

## Materials

I used an InFocus projector that I bought at a thrift shop for $20 (that might explain why there was no remote)

![projector](/projector.png)

I removed these two buttons, scaped the "varnish" off on the circuit underneath them, and soldered wires from the CD4066 to them.

![4066 IC](/4066.png)

connect the IC to Gnd and VCC(5 or 3.3v on the Rpi), and use one "switch" per button to be "mimicked"

![relays](/relay.jpg)

This 2 channel relay module works.  I just bought the relays individually and soldered them onto a perforated board.  Make sure to used diodes if you do this to avoid any booboos!

![lm298](/lm298.jpg)

This lm298 module is the one I used for driving the motor.

![motor](/motor.jpg)

This is a geared motor, so it produces sufficient torque to raise and lower the projector.

*** Some of these connections might need a resistor.  Look up "pull up resistors", "pull down resistors", "voltage dividers" to understand when you need to use one.

VNC for remote access to the Raspberry pi.  Find it here https://www.raspberrypi.org/documentation/remote-access/vnc/ 