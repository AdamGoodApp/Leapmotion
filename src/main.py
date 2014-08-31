import sys
sys.path.insert(0, "../lib")
import Leap
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
    
    for hand in frame.hands:
      if hand.palm_position[0] > 0:
        print 'Moving Right'
      else:
        print 'Moving Left'
      


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