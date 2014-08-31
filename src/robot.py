# ROBOT ARM CONTROL PROGRAM
# Based on http://www.wikihow.com/Use-a-USB-Robotic-Arm-with-a-Raspberry-Pi-(Maplin)
# Remember to install the PyUSB library before use.
# This script allows you to send a series of commands to your robot arm.
# Example of use: sudo python arm.py ab bc su sd eu ed wu wd go gc lo lf
# 4th January 2014
# Sean Clark (www.seanclark.me.uk)

# Import libraries
import sys, time, usb.core, usb.util

# Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)

# Check if the arm is detected and warn if not
if RoboArm is None:
  raise ValueError("Arm not found")

#Create a variable for duration
Duration = 1

#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
  #Start the movement
  RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
  #Stop the movement after waiting a specified duration
  time.sleep(Duration)
  ArmCmd=[0,0,0]
  RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

# Parse the command line
Commands = sys.argv[1:]
for i in range(1,len(sys.argv)):
  Command = str(sys.argv[i])
  print Command;

  # Execute the command
  if (Command == 'ba'):
    MoveArm(Duration,[0,1,0])    # Rotate base anti-clockwise
  elif (Command == 'bc'):
    MoveArm(Duration,[0,2,0])    # Rotate base clockwise
  elif (Command == 'su'):
    MoveArm(Duration,[64,0,0])   # Shoulder up
  elif (Command == 'sd'):
    MoveArm(Duration,[128,0,0])  # Shoulder down
  elif (Command == 'eu'):
    MoveArm(Duration,[16,0,0])   # Elbow up
  elif (Command == 'ed'):
    MoveArm(Duration,[32,0,0])   # Elbow down
  elif (Command == 'wu'):
    MoveArm(Duration,[4,0,0])    # Wrist up
  elif (Command == 'wd'):
    MoveArm(Duration,[8,0,0])    # Wrist down
  elif (Command == 'go'):
    MoveArm(Duration,[2,0,0])    # Grip open
  elif (Command == 'gc'):
    MoveArm(Duration,[1,0,0])    # Grip close
  elif (Command == 'lo'):
    MoveArm(Duration,[0,0,1])    # Light on
  elif (Command == 'lf'):
    MoveArm(Duration,[0,0,0])    # Light off