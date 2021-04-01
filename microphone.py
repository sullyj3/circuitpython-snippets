import time
from adafruit_circuitplayground import cp
from math import log

def clamp(a, b, x):
  return max(min(x,b), a)

def transfer(x):
  return clamp(0,10, round(3 * log(x, 10)))
 
BLACK = (0,0,0)
BLUE = (0,0,20)

while True:
  num_pixels = transfer(cp.sound_level)
  for i in range(num_pixels):
    cp.pixels[i] = BLUE
  for i in range(9, num_pixels-1, -1):
    cp.pixels[i] = BLACK
  #print(num_pixels)
  time.sleep(0.01)

