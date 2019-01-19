#!/usr/bin/env python3

import anki_vector
import time

"""
Check the current state of the robot and cube batteries.

Vector is considered fully-charged above 4.1 volts. At 3.6V, the robot is approaching low charge.

Battery_level values are as follows:
Low = 1: 3.6V or less. If on charger, 4V or less.
Nominal = 2
Full = 3: only be achieved when Vector is on the charger.
"""
with anki_vector.Robot() as robot:
    battery_state = robot.get_battery_state()
    if battery_state:
        #print("Robot battery voltage: {0}".format(battery_state.battery_volts))
        #print("Robot battery Level: {0}".format(battery_state.battery_level))
        #print("Robot battery is charging: {0}".format(battery_state.is_charging))
        #print("Robot is on charger platform: {0}".format(battery_state.is_on_charger_platform))
        #print("Robot's suggested charger time: {0}".format(battery_state.suggested_charger_sec))
        
        print(" ")
        print (time.strftime("%Y-%m-%d %H:%M:%S"))
        print(" ")
        print("Battery voltage  | Battery Level | Charging | Platform |Charging Time |")
        print("{0}".format(battery_state.battery_volts), end = '      ')
        print("{0}".format(battery_state.battery_level), end = '             ')
        print("{0}".format(battery_state.is_charging), end = '      ')
        print("{0}".format(battery_state.is_on_charger_platform), end = '     ')
        print("{0}".format(battery_state.suggested_charger_sec))

        print(" ")

