import sys
import live
import cairo
import pyglet
import random
import inspect
from vmath import *
from PIL import Image
from pyglet.gl import *
from pyglet.window import *
from pyglet.window import key
from pyglet.text import Label
from cStringIO import StringIO
from pyglet import clock, image

# this will replace pyglet's default idle loop
def idle(loop):
    clock.tick(poll=True)
    return clock.get_sleep_time(sleep_idle=True) / 2.0
 
def set_topmost(window):
    from pyglet.window.win32 import _user32
    SWP_NOMOVE = 2
    HWND_TOPMOST = -1
    SWP_NOSIZE = 1
    _user32.SetWindowPos(
        window._hwnd, HWND_TOPMOST, 0, 0, 0, 0,
        SWP_NOMOVE | SWP_NOSIZE)

class Tool():
    def __init__(self):
        size = v2(600, 600)
        self.mode = 'cairo'
        self.size = size
        self.time = 0.0
        self.error = False
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *size)
        self.context = cairo.Context(self.surface)
        self.pil = Image.new('RGBA', size.to_tuple())
        self.context.scale(*size)
        config = Config(buffer_size=32,
                        alpha_size=8,
                        double_buffer=True,
                        depth_size=24,
                        stencil_size=8,
                        aux_buffers=0,
                        sample_buffers=0,
                        samples=0,)
        caption = 'livepatterns'
        self.window = Window(*size, config=config, caption=caption)
        self.message = Label('', 'Courier', 11, x=0, y=size.y)
        self.message.anchor_y = 'top'
        pyglet.app.EventLoop.idle = idle
        self.update_mode()
        self.init_opengl()

    def update_mode(self):
        self.mode = 'cairo'
        if 'im' in inspect.getargspec(live.draw)[0]:
            self.mode = 'pil'

    def init_opengl(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) 

    def update(self, dt):
        self.message.text = ''
        if not dt:
            return
        self.error = False
        try:
            reload(live)
        except Exception, error:
            self.error = True
            self.message.text = str(error)
            print error
            print '<- load error'
        self.time += dt
        self.window.clear()
        self.render(self.time, dt)
        self.window.flip()

    def render(self, time, dt):
        # clear surfaces
        self.context.set_operator(cairo.OPERATOR_SOURCE)
        self.context.set_source_rgba(0, 0, 0, 0)
        self.context.paint()
        self.pil = Image.new('RGBA', self.size.to_tuple())
        self.update_mode()
        manipulator = self.context
        if self.mode == 'pil':
            manipulator = self.pil
        # get the new pattern frame from the live module
        try:
            live.draw(manipulator, time, dt)
        except Exception, error:
            self.error = True
            self.message.text = str(error)
            print error
            print '<- execution error'
        # draw the final image
        if not self.error:
            if self.mode == 'cairo':
                data = StringIO()
                self.surface.write_to_png(data)
                pattern = image.load('pattern.png', file=data)
            elif self.mode == 'pil':
                raw = self.pil.tostring()
                size = self.size
                pattern = pyglet.image.ImageData(size.x, size.y, 'RGBA',
                        raw, pitch=size.x * 4)
            pattern.blit(0, 0)
        self.message.draw()

    def run(self):
        clock.schedule(self.update)
        set_topmost(self.window)
        pyglet.app.run()


def main(argv):
    print 'started'
    tool = Tool()
    tool.run()
    print 'done'

if __name__ == '__main__':
    main(sys.argv)

