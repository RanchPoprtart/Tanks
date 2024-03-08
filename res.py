import pyglet


pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()


tankBase = pyglet.resource.image("tankBase.png")
tankTurret = pyglet.resource.image("tankTurret.png")
bullet = pyglet.resource.image("bullet.png")
brick = pyglet.resource.image("brick.png")