import sys
sys.path.insert(0, "../lib")
import Leap
import sys, time, usb.core, usb.util
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

  finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
  bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
  state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']


  def on_connect(self, controller):
    print "Connected"
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
    controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
    controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
    controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);


  def on_frame(self, controller):
    frame = controller.frame()
    if len(frame.hands) == 0: print 'No Hands'

    def MoveArm(Duration, ArmCmd):
      RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)

      if RoboArm is None:
        raise ValueError("Arm not found")

      Duration=1

      RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
      time.sleep(Duration)
      ArmCmd=[0,0,0]
      RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

    for hand in frame.hands:
      xaxis = hand.palm_position[0]
      yaxis = hand.palm_position[1]
      zaxis = hand.palm_position[2]

      if xaxis > 100:
        print 'Moving Right'
        MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
      elif xaxis < -100:
        print 'Moving Left'
        MoveArm(1,[0,2,0]) #Rotate base clockwise
      elif yaxis > 300:
        print 'Moving Up'
        MoveArm(1,[64,0,0]) #Shoulder up
      elif yaxis < 200:
        print 'Moving Down'
        MoveArm(1,[128,0,0]) #Shoulder down
      elif zaxis > 80:
        print 'Moving Back'
        MoveArm(1,[1,0,0]) #Grip close
      elif zaxis < 0:
        print 'Moving Forward'
        MoveArm(1,[2,0,0]) #Grip open
      else:
        print 'Stopped Moving'

      
      


def main():
  listener = SampleListener()
  controller = Leap.Controller()

  controller.add_listener(listener)

  # Keep this process running until Enter is pressed
  print "Press Enter to quit..."
  try:
    sys.stdin.readline()
  except KeyboardInterrupt:
    pass
  finally:
    controller.remove_listener(listener)

if __name__ == "__main__":
  main()