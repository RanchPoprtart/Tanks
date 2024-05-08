import pyglet
from pyglet.window import key
import res
import util
import math



class GameObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def check_for_collision(self, object):
        pass


class Tank(GameObject):

    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = {"left": False, "right": False, "UP": False, "DOWN": False}
        self.key_handler = key.KeyStateHandler()
        self.dir = ""
    def on_key_press(self, symbol, mod):
        direction = 0
        if symbol == key.LEFT:
            self.keys["left"] = True
            self.dir = "left"
        if symbol == key.RIGHT:
            self.keys["right"] = True
            self.dir = "right"
        if symbol == key.UP:
            self.keys["UP"] = True
            self.dir = "UP"
        if symbol == key.DOWN:
            self.keys["DOWN"] = True
            self.dir = "DOWN"

    def on_key_release(self, symbol, mod):
        if symbol == key.LEFT:
            self.keys["left"] = False
        if symbol == key.RIGHT:
            self.keys["right"] = False
        if symbol == key.UP:
            self.keys["UP"] = False
        if symbol == key.DOWN:
            self.keys["DOWN"] = False

    def update(self, dt):
        if self.keys["left"]:
            self.x -= 2
        if self.keys["right"]:
            self.x += 2
        if self.keys["UP"]:
            self.y += 2
        if self.keys["DOWN"]:
            self.y -= 2
        #super().update(dt)






class Blocks(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Bullet(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pyglet.clock.schedule_once(self.self_destruct, 0.5)
        self.base_speed = 15