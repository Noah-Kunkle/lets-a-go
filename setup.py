import pygame as pg
import numpy as np  # noqa: F401
import LVl
import draw
import player

def crutal_setup():
    pg.init()
    pg.mixer.init()
    clock=pg.time.Clock()
    return(clock)

def screen_setup(res_x, res_y):
    screen=pg.display.set_mode((res_x, res_y))
    return(screen)

def setup2(fov,speeeed,res_x,player_amount):
    fov=2*fov
    sped = 0.01 * speeeed
    is_music=True
    mode=True
    per_player_x=res_x/player_amount
    return(per_player_x,fov,is_music,sped,mode)

def class_setup(sped,turn,screen,Scale,fov,res_x,res_y,darkness,dencity,per_player_x):
    m1=LVl.Lvl(LVl.l1())
    m2=LVl.Lvl(LVl.l2())
    m1.color()
    m2.color()
    lvlA1=m1.lvl
    p1=player.Entity(1,lvlA1,sped,turn)
    p2=player.Entity(2,lvlA1,sped,turn)
    d1=draw.draw(screen,Scale,lvlA1,fov,per_player_x,res_y,darkness,dencity)
    return(p1,p2,d1,lvlA1)