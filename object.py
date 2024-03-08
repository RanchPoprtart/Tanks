import pyglet
from pyglet.window import key
import res
#import util
#import math



class GameObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Player(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Bullet(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)


class Blocks(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



