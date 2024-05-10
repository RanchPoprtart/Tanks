import pyglet


pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()


tank = pyglet.resource.image("Tank.png")
bullet = pyglet.resource.image("bullet.png")
brick = pyglet.resource.image("brick32.png")
breakableBrick =  pyglet.resource.image("bbrick.png")

def center_img(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

center_img(tank)
center_img(bullet)

