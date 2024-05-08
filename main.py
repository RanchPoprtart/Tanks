import pygame as pygame
import pyglet
from pyglet.window import key
from pyglet import window, shapes
import object
import res
import random
import util

'''
each block has 4 cells
there is 20 blocks by 20
but there is 26 x 26 grid


'''
#constants
scale= 2
ScreenW = 600
CellCount = 24
BlockW= 32
CellW = 16





#game Screen
class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.square = shapes.Rectangle(170, 0, 900, 900, color=(128, 128, 128), batch=self.batch)
        self.blocks = []



        #Playable grid
        for i in range(CellCount):
            row = []
            for j in range(CellCount):
                RandomTile = random.randint(1,20)
                if RandomTile <= 1:
                    row.append(object.Blocks(res.brick, BlockW * i + 200, BlockW * j + 16, batch=self.batch))
                    row[len(row) - 1].scale = scale
                else:
                    row.append(shapes.Rectangle(BlockW * i + 200, BlockW * j + 16,  CellW * scale,  CellW * scale, color=(0,0,0), batch=self.batch))
            self.blocks.append(row)


        #Tank Draw
        i = random.randint(2,23)
        j = random.randint(2,23)
        if type(self.blocks[i][j]) == object.Blocks:
            i = random.randint(2,23)
            j = random.randint(2,23)
        self.tank = object.Tank(res.tank, i * BlockW + 200 , j * BlockW + 16 , batch=self.batch)
        print(self.tank.x, self.tank.y)
        self.push_handlers(self.tank)
        self.push_handlers(self.tank.key_handler)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.is_blocked = False


    def on_draw(self):
        self.square.draw()
        self.batch.draw()



    def update(self, dt):
        self.tank.update(dt)
        self.check_for_Obj(self.tank.dir)
        '''if self.is_blocked:
            self.x = 0
            self.y = 0
            return'''



    def check_for_Obj(self, dir):
        tank_x = self.tank.x
        tank_y = self.tank.y
        if self.tank.dir == "left":
            self.tank.rotation = 270
            for i in range (CellCount):
                for j in range (CellCount):
                    if tank_x == self.blocks[i][j].x + BlockW and (tank_y >= self.blocks[i][j].y - 18 and tank_y < self.blocks[i][j].y + BlockW ) and self.tank.keys["left"] and type(self.blocks[i][j]) == object.Blocks:
                        self.tank.keys["left"] = False
                        self.tank.x += 2
        if self.tank.dir == "right":
            self.tank.rotation = 90
            for i in range (CellCount):
                for j in range (CellCount):
                    if tank_x == self.blocks[i][j].x - 12 and ( tank_y >= self.blocks[i][j].y - 12 and tank_y < self.blocks[i][j].y + BlockW ) and self.tank.keys["right"] and type(self.blocks[i][j]) == object.Blocks:

                        self.tank.keys["right"] = False
                        self.tank.x -= 2
        if self.tank.dir == "DOWN":
            self.tank.rotation = 180
            for i in range (CellCount):
                for j in range (CellCount):
                    if tank_y == self.blocks[i][j].y + BlockW and ( tank_x >= self.blocks[i][j].x - 12 and tank_x < self.blocks[i][j].x + BlockW ) and self.tank.keys["DOWN"] and type(self.blocks[i][j]) == object.Blocks:
                        self.tank.keys["Down"] = False
                        self.tank.y += 2
        if self.tank.dir == "UP":
            self.tank.rotation = 0
            for i in range(CellCount):
                for j in range(CellCount):
                    if tank_y == self.blocks[i][j].y - 12 and ( tank_x >= self.blocks[i][j].x - 12 and tank_x < self.blocks[i][j].x + BlockW ) and self.tank.keys["UP"] and type(self.blocks[i][j]) == object.Blocks:
                        print("stop")
                        self.tank.keys["UP"] = False
                        self.tank.y -= 2







win = GameWindow(width=1200, height=800,)
pyglet.clock.schedule_interval(win.update , 1.0 / 60)

#start game
if __name__ ==  "__main__":
    pyglet.app.run()

