# Vector-Battery-Status
Python script that reports on Anki Vector's battery status.   Much of this code is in the SDK  - - I reformated output to improve readability and to ultimately create a log file.

Anki provides the following "abbreviated" info about Vector's battery status in the SDK:

"Vector is considered fully-charged above 4.1 volts. At 3.6V, the robot is approaching low charge.

Battery_level values are as follows:
Low = 1: 3.6V or less. If on charger, 4V or less.
Nominal = 2
Full = 3: only be achieved when Vector is on the charger."


NOTE:  You will need to have the Anki Vector SDK installed on your PC in order to run this script.  The SDK can be found at:
https://developer.anki.com/vector/docs/initial.html

Also note, as of Anki Vector SDK Ver 0.5.1, Python programs should not be run while the smart phone app is connected to Vector.  On rare occasions, the Python code will run (or portions will execute) but it is highly recommended that you close the Vector smart phone app before executing any Python code that connects to Vector.  [Vector probably gets confused if two apps are trying to talk to him at the same time - - it kinda makes sense.  Even humans don't like two people talking to them at the same time :-) ]
