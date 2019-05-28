import pyxel
import random
import time

width=255
height=255
myfps=10

class Enemy:
    def __init__(self):
        self.x=random.randint(0,width)
        self.y=0
        self.size=1
    def bigger(self, plus):
        self.size+=plus
    def draw_enemy(self):
        pyxel.rect(self.x-int(self.size/2), self.y-int(self.size/2), self.x+int(self.size/2), self.y+int(self.size/2), 9)

class Cannon:
    def __init__(self):
        self.x=0
        self.y=int(int(height*(2/3)))
        self.direction=[1,0]
        self.burrets=[]
    def fire(self):
        if pyxel.frame_count % int(myfps/0.5) ==0: #2秒に一回
            self.burrets.append(Burret(self.x, self.y, self.direction))
    def draw_cannon(self):
        pyxel.rect(self.x-1, self.y-4, self.x+1, self.y+4, 9)
        for i in self.burrets:
            i.draw_burret()

class Burret:
    def __init__(self,inx,iny,indir):
        self.x=inx
        self.y=iny
        self.direction=indir
    def draw_burret(self):
        pyxel.rect(self.x, self.y, self.x, self.y+1, 4)
        self.x+=self.direction[0]
        self.y+=self.direction[1]

        


class App:
    def __init__(self, fps=myfps):
        pyxel.init(width, height)
        self.enemys=[]
        self.cannons=[]
        self.cannons.append(Cannon())
        self.st=time.time()
        self.tf=1
        self.difft=0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tf==1:
            self.enemys.append(Enemy())
            self.tf=0
            self.difft= int(time.time()) - int(self.st)
        if int(time.time()) - int(self.st) != self.difft and self.tf==0:
            self.tf=1
        for i, ene in enumerate(self.enemys):
            if ene.x >= pyxel.mouse_x:
                ene.x-=1
            else:
                ene.x+=1
            if ene.y >= pyxel.mouse_y:
                ene.y-=1
            else:
                ene.y+=1
            if ene.x<= pyxel.mouse_x<=ene.x+7  and ene.y<=pyxel.mouse_y<=ene.y+7:
                print("GAMEOVER")
                print(time.time()-self.st)
            #ene同士の当たり判定
            for j, ene2 in enumerate(self.enemys):
                if i!=j:
                    if ene.x-3 < ene2.x < ene2.x+3 and ene.y-3 < ene2.y < ene2.y+3:
                        ene.bigger(ene.size)
                        #self.enemys.pop(j)
                        print(ene.size)
                        break

    def draw(self):
        pyxel.cls(0)
        for ene in self.enemys:
            ene.draw_enemy()
        for con in self.cannons:
            con.draw_cannon()
            con.fire()
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, pyxel.mouse_x + 7, pyxel.mouse_y+7, 14)

App()
