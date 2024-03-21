import pygame as pygame
import pyglet
from pyglet.window import key
from pyglet import window, shapes
import object
import res
import random
#import util




#constants
scale = 1.8
ScreenW = 758
CellCount = 13
CellW = ScreenW / 13
Block = 0
BlockW = CellW



#game Screen
class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.square = shapes.Rectangle(160, 0, 910, 910, color=(128, 128, 128), batch=self.batch)
        self.blocks = []


        #Playable grid
        for i in range(CellCount):
            row = []
            for j in range(CellCount):
                RandomTile = random.randint(1,10)
                if RandomTile <= 1:
                    row.append(object.Blocks(res.brick, BlockW * i + 200, BlockW * j + 45, batch=self.batch))
                    row[len(row) - 1].scale = scale
                else:
                    row.append(shapes.Rectangle(BlockW * i + 200, BlockW * j + 45, 32 * scale, 32 * scale, color=(0,0,0), batch=self.batch))
            self.blocks.append(row)


        #Tank Draw
        i = random.randint(3,12)
        j = random.randint(3,12)
        while type(self.blocks[i][j]) == object.Blocks:
            i = random.randint(3,12)
            j = random.randint(3,12)
        self.tank = object.Tank(res.tank, (i * BlockW) , (j * BlockW), batch=self.batch)
        print(self.tank.x, self.tank.y)


    '''def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.tank.x_speed = True
        elif symbol == key.RIGHT:
            self.tank.x_speed = True
        elif symbol == key.UP:
            self.tank.y_speed = True
        elif symbol == key.DOWN:
            self.tank.y_speed = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.tank.x_speed = False
        elif symbol == key.RIGHT:
            self.tank.x_speed = False
        elif symbol == key.UP:
            self.tank.y_speed = False
        elif symbol == key.DOWN:
            self.tank.y_speed = False'''


    def on_draw(self):
        self.square.draw()
        self.batch.draw()


        '''for i in range (len(self.blocks)):
            for j in range(len(self.blocks[i])):
                #print(self.blocks[i], self.blocks[j])
                self.blocks[i][j].draw()
                print(type(self.blocks[i][j]))'''

    def update(self, dt):
        self.square.x += 0






win = GameWindow(width=1200, height=800,)
pyglet.clock.schedule_interval(win.update , 1.0 / 60)

#start game
if __name__ ==  "__main__":
    pyglet.app.run()

