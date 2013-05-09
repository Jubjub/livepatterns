import random
from math import *
from vmath import *
from cairo import *
from PIL import ImageDraw

random.seed(2)

re = random.uniform(0.1, 0.3)
ge = random.uniform(0, 0.2)
be = random.uniform(0, 0.1)

def draw(im, time, dt):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=(128 * sin(time), 100, 3, 100))
    draw.line((0, im.size[1] * sin(time), im.size[0], 0), fill=(12, 255, 30, 255))

