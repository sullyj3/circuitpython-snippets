import time
from adafruit_circuitplayground import cp
from math import log
from buttons import Buttons

def clamp(a, b, x):
  return max(min(x,b), a)

def ab_log10(a, b, x):
  return a * log(b * x, 10)

'''
def transfer(x, a, b):
  return clamp(0,10, round())
 
'''

''' given two points, calculate a new log10 transfer function '''
def calculate_transfer_function(pt_min, pt_max):
  (x_min, y_min) = pt_min
  (x_max, y_max) = pt_max
  # hack to make sure we don't divide by 0
  x_max = max(x_max, 0.001)
  x_min = max(x_min, 0.001)

  a = (y_max - y_min)/log(x_max/x_min, 10)
  b = 10 ** ((y_min * log(x_max, 10) - y_max * log(x_min, 10)) / (y_max - y_min))
  print("new transfer parameters: a =", a, "b =", b)

  return lambda x: ab_log10(a, b, x)

BLACK = (0,0,0)
BLUE = (0,0,20)
GREEN = (0,20,0)

# modes. (no enums in circuitpython unfortunately)
MIC = "MIC"
CALIBRATING = "CALIBRATING"

def main():
  buttons = Buttons()

  transfer = calculate_transfer_function((10, 1), (16000, 9))

  mode = MIC

  calibrate_min = None
  calibrate_max = None

  while True:
    buttons.update()

    if mode == MIC:
      num_pixels = clamp(0, 10, round(transfer(cp.sound_level)))
      for i in range(num_pixels):
        cp.pixels[i] = BLUE
      for i in range(9, num_pixels-1, -1):
        cp.pixels[i] = BLACK

      if buttons.pressed['BTN_A']:
        mode = CALIBRATING
        cp.pixels.fill(GREEN)
        print("Calibrating")
        calibrate_min = cp.sound_level
        calibrate_max = cp.sound_level

    elif mode == CALIBRATING:
      calibrate_min = min(cp.sound_level, calibrate_min)
      calibrate_max = max(cp.sound_level, calibrate_max)

      if buttons.released['BTN_A']:
        print("Done calibrating.")
        print("minimum detected audio level was", calibrate_min)
        print("maximum detected audio level was", calibrate_max)
        transfer = calculate_transfer_function((calibrate_min, 1), (calibrate_max, 9))
        mode = MIC

    time.sleep(0.01)

if __name__ == '__main__':
  print("Starting mic")
  main()

