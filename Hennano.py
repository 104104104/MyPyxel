import pyxel
import random
import time

width=160
height=120

class Enemy:
    def __init__(self):
        randp=random.randint(0,4)
        if randp==0:
            self.x=0
            self.y=0
        elif randp==1:
            self.x=width
            self.y=0
        elif randp==2:
            self.x=0
            self.y=height
        else:
            self.x=width
            self.y=height
    def draw_enemy(self):
        pyxel.rect(self.x, self.y, self.x + 7, self.y+7, 9)


class App:
    def __init__(self):
        pyxel.init(width, height)
        self.enemys=[]
        self.t=0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.enemys.append(Enemy())
        self.enemys.append(Enemy())
        for ene in self.enemys:
            if ene.x >= pyxel.mouse_x:
                ene.x-=1
            else:
                ene.x+=1
            if ene.y >= pyxel.mouse_y:
                ene.y-=1
            else:
                ene.y+=1

    def draw(self):
        pyxel.cls(0)
        for ene in self.enemys:
            ene.draw_enemy()
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, pyxel.mouse_x + 7, pyxel.mouse_y+7, 14)

App()
