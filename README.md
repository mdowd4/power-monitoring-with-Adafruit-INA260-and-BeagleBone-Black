# Power Monitoring With Adafruit INA260 and BeagleBone Black

## Description
This is a python script for a BeagleBone Black (BBB) to periodically read power sensor data and store it for the duration of an experiment. The BBB fills lists with the data every other second and then takes the average after one minute. The average for the minute is written to a CSV file and the process repeats for the specified number of minutes of the test.

## INA260 Sensors
The power sensors communicate with the BBB over I2C. Because both devices are connected on the same I2C bus, they need unique addresses. To change the I2C address of one of the sensors from the default, a solder bridge must be added on either the A0 or A1 pads labeled on the board. The CircuitPython package for Adafruit INA260 was installed on the BBB to simplify the python code for initializing the I2C bus and reading the data from it.

## History
This power monitoring system was designed and built as part of my senior design project. The project focused on directional control for solar panels, where multiple control methods were tested against a stationary position. This power monitoring system collected data on current, voltage, and power for both the panel generation and control system consumption throughout each experiment. 

## YouTube Video
To see a video of my senior design project, click [here](https://youtu.be/9AI5urBoQ6E)
