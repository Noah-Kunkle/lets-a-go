import pygame as pg
import numpy as np
from settings import*
import LVl
# 1 = item 2 = mob 3 = idk
#
#
coin=pg.image.load('coin.png')

class entity(pg.sprite.Sprite):
    def __init__(self,pos,type,screen,number):
        super().__init__()
        self.type=type
        self.number=number
     #   self.image=image
      #  self.rect = self.image.get_rect()
       # self.rect.center=(0,res_y/2)
        self.screen=screen
        self.pos=pos

    def player_dis(self,player):
        a,b=self.pos
        c=player.x
        d=player.y
        dx=a-c
        dy=b-d
        #print(dx)
        angle=np.arctan2((dy),(dx))#-np.pi/2
        if angle<0:
            angle=angle+2*np.pi
        dis=np.sqrt(dy*dy+dx*dx)
        print(angle,dis)
        return((angle,dis))
    
    def suerside(self):
        self.kill()

        
        
def make_objeckts(enimies,screen):
    number=1
    objeckt_map=LVl.coin_map()
    for i in(range(len(objeckt_map[0]))):
        for j in(range(len(objeckt_map[1]))):
            if objeckt_map[i][j]==1:
                objeckt=entity((j+.5,i+.5),1,number,screen)
                number=number+1
                enimies.add(objeckt)
                #print ('added objeckt')
                #print (i,j)
    #print(enimies)