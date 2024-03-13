import pyglet
from pyglet import window, shapes
import object
import res
#import util
#import random

scale = 1.8
ScreenW = 923
CellCount = 13
CellW = ScreenW / 13
Block = 0
BlockW = CellW * .8





class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.square = shapes.Rectangle(160, 0, 923, 923, color=(128, 128, 128), batch=self.batch)
        self.blocks = []

        for i in range(CellCount):
            row = []
            for j in range(CellCount):
                row.append(object.Blocks(res.brick, BlockW * i + 200, BlockW * j + 40))
                row[len(row) - 1].scale = scale


                #pyglet.sprite.Sprite()
            self.blocks.append(row)




    def on_draw(self):
        self.square.draw()
        for i in range (len(self.blocks)):
            for j in range(len(self.blocks[i])):
                print(self.blocks[i], self.blocks[j])
                self.blocks[i][j].draw()

    def update(self, dt):
        self.square.x += 0









win = GameWindow(width=1200, height=800,)


pyglet.clock.schedule_interval(win.update , 1.0 / 60)


if __name__ ==  "__main__":
    pyglet.app.run()