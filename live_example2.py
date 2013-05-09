import random
from math import *
from vmath import *
from cairo import *
from PIL import ImageDraw

# rename to live.py to see this example in action

def draw(im, time, dt):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=(128 * sin(time), 100, 3, 100))
    draw.line((0, im.size[1] * sin(time), im.size[0], 0), fill=(12, 255, 30, 255))

