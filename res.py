import pyglet


pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()


tank = pyglet.resource.image("Tank.png")
bullet = pyglet.resource.image("bullet.png")
brick = pyglet.resource.image("brick32.png")