import pyxel
import random

width=255
height=255
myfps=10

minsize=1
gravitysize=2


gravveclen=1

class Enemys:
    def __init__(self):
        self.enes=[]
    def appendene(self):
        self.enes.append(Enemy())
    def grav(self, nowene):
        for ene in self.enes:
            ene.gravvecx=nowene.x-ene.x
            ene.gravvecy=nowene.y-ene.y
            if ene.gravvecx!=0 and ene.gravvecy!=0:
                if ene.gravvecx > ene.gravvecy:
                    ene.gravvecx=int(ene.gravvecx/abs(ene.gravvecy))
                    ene.gravvecy=int(ene.gravvecy/abs(ene.gravvecy))
                else:
                    ene.gravvecy=int(ene.gravvecy/abs(ene.gravvecx))
                    ene.gravvecx=int(ene.gravvecx/abs(ene.gravvecx))
           
            if ene.gravvecx>gravveclen:
                ene.gravvecx=gravveclen
            if ene.gravvecy>gravveclen:
                ene.gravvecy=gravveclen
            if ene.gravvecx<-gravveclen:
                ene.gravvecx=-gravveclen
            if ene.gravvecy<-gravveclen:
                ene.gravvecy=-gravveclen

            ene.x+=ene.gravvecx
            ene.y+=ene.gravvecy



class Enemy:
    def __init__(self):
        self.x=random.randint(0,width)
        self.y=0
        self.size=minsize
        self.vecx=pyxel.mouse_x-self.x
        self.vecy=pyxel.mouse_y-self.y
        self.gravvecx=0
        self.gravvecy=0
    def bigger(self, plus):
        self.size+=plus

    def calvec(self):
        self.vecx=pyxel.mouse_x-self.x
        self.vecy=pyxel.mouse_y-self.y
        if self.vecx!=0 and self.vecy!=0:
            if self.vecx > self.vecy:
                self.vecx=int(self.vecx/abs(self.vecy))
                self.vecy=int(self.vecy/abs(self.vecy))
            else:
                self.vecy=int(self.vecy/abs(self.vecx))
                self.vecx=int(self.vecx/abs(self.vecx))
        if self.vecx>5:
            self.vecx=5
        if self.vecy>5:
            self.vecy=5
        if self.vecx<-5:
            self.vecx=-5
        if self.vecy<-5:
            self.vecy=-5



        self.x+=self.vecx
        self.y+=self.vecy
    def draw_enemy(self):
        pyxel.circ(self.x, self.y, self.size, 9)



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
        self.enemys=Enemys()
        self.cannons=[]
        self.cannons.append(Cannon())
        self.maxene=0
        self.gameover_flug=0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % (myfps*2)==0:
            self.enemys.appendene()
        for i, ene in enumerate(self.enemys.enes):
            ene.calvec()
            if ene.x<= pyxel.mouse_x<=ene.x+7  and ene.y<=pyxel.mouse_y<=ene.y+7:
                self.gameover_flug=1
            #ene同士の当たり判定
            for j, ene2 in enumerate(self.enemys.enes):
                if i!=j:
                    if ene.x-3 < ene2.x < ene.x+3 and ene.y-3 < ene2.y < ene.y+3:
                        ene.bigger(ene2.size)
                        self.enemys.enes.pop(j)
                        break
            if ene.size>=gravitysize:
                self.enemys.grav(ene)

    def draw(self):
        pyxel.cls(0)
        for ene in self.enemys.enes:
            ene.draw_enemy()
            if self.maxene<ene.size:
                self.maxene=ene.size
        pyxel.text(height-20, width-60, str(int(self.maxene/minsize)), 7)
        for con in self.cannons:
            con.draw_cannon()
            con.fire()
        if self.gameover_flug: 
            pyxel.text(int(height/2),int(width/2), "GAMEOVER  "+str(int(self.maxene/minsize)), 14)
 
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, pyxel.mouse_x + 7, pyxel.mouse_y+7, 14)

App()
