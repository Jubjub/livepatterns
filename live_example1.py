import random
from math import *
from vmath import *
from cairo import *
from PIL import ImageDraw

# rename to live.py to see this example in action

random.seed(2)

re = random.uniform(0.1, 0.3)
ge = random.uniform(0, 0.2)
be = random.uniform(0, 0.1)


def rectangle(cr, x, y, width, height, angle=0):
    cr.save()
    center = v2(x - width / 2.0, y - height / 2.0)
    cr.translate(x, y)
    cr.rotate(angle)
    cr.translate(-x, -y)
    cr.rectangle(center.x, center.y, width, height)
    cr.restore()

def draw(cr, time, dt):
    time *= 2
    beat = time % 2
    if beat > 1:
        beat = 2 - beat
    radius = 0.4
    minimum = radius * beat + 0.06
    width = 0.03
    decrease = 0.04
    r = 0.0
    g = 0.0
    b = 0.0
    # squares
    size = 0.5 * (1 - beat)
    i = 0
    while size > 0:
        cr.set_source_rgb(r, g, b)
        wave = sin
        if not i % 2:
            wave = cos
        else:
            cr.set_source_rgb(b, g, r)
        rectangle(cr, 0.5, 0.5, size, size, wave(time * 1))
        cr.fill()
        i += 1
        size -= 0.05
        r += re * 1.4
        g += ge * 1.3
        b += be * 1.3
    r = 0.0
    g = 0.0
    b = 0.0
    while radius > minimum:
        r += re
        g += ge
        b += be
        # background
        width -= 0.01
        #cr.set_source_rgb(1 - r, 1 - g, 1 - b)
        cr.set_source_rgb(b, g, r)
        cr.arc(0.5, 0.5, radius, 0, 2 * pi)
        cr.stroke()
        width += 0.01
        # arcs
        cr.set_line_width(width)
        cr.set_source_rgb(r, g, b)
        extra = random.uniform(0, pi / 2)
        extra *= beat / 2
        cr.arc(0.5, 0.5, radius, time + pi + extra , 2 * pi + time + extra)
        cr.stroke()
        radius -= decrease

