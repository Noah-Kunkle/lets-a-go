import numpy as np
import pygame as pg


class Entity:
    
    def __init__(self, number, lvl,  speed, dpi):
        self.x = 1.5
        self.y = 1.5
        self.lvl = lvl
        self.rotation = 0
        self.speed = speed
        self.is_alive = True
        self.dpi = dpi #distent per unit
        self.number = number
        self.coin_amount=0
        
    def colision(self):
        wallu, color = self.lvl[int(self.y + .1)][int(self.x)]
        walll, color = self.lvl[int(self.y)][int(self.x - .1)]
        wallr, color = self.lvl[int(self.y)][int(self.x + .1)]
        walld, color = self.lvl[int(self.y - .1)][int(self.x)]
        return(walld, walll, wallu, wallr)
    
    def move_player(self):
        
        if self.number == 1:
            
            w, a, s, d = get_keys(self.dpi)#get keys
            
        else:
            
            w, a, s, d = get_keys2(self.dpi)#get keys
            
        x, y = self.x + np.cos(self.rotation) * self.speed * (w - s),  self.y + np.sin(self.rotation) * self.speed * (w - s)
        self.rotation = (self.rotation - a + d)
        up,  left,  down,  right = self.colision()
        
        if up:
            y = int(y) + .1
        if down:
            y = int(y) + .9
        if left:
            x = int(x) + .1
        if right:
            x = int(x) + .9
        self.x, self.y = x, y
        
    def get_posy(self):
        
        return(self.y)
    
    def get_posx(self):
        
        return(self.x)
    
    def get_rot(self):
        
        return(self.rotation)
    
    
def get_keys(dpi):#get the input
    
    pressed_keys = pg.key.get_pressed()#get all keys
    
    if pressed_keys[ord('w')]:
        w = 1
    else:
        w = 0
    if pressed_keys[ord('a')]:
        a = np.pi / (dpi * 64)
    else:
        a = 0
    if pressed_keys[ord('s')]:
        s = 1
    else:
        s = 0
    if pressed_keys[ord('d')]:
        d = np.pi / (dpi * 64)
    else:
        d = 0
    return(w, a, s, d)#retuen a bool value for keys
        
def get_keys2(dpi):#get the input
    
    pressed_keys = pg.key.get_pressed()#get all keys
    
    if pressed_keys[pg.K_UP]:
        w = 1
    else:
        w = 0
    if pressed_keys[pg.K_LEFT]:
        a = np.pi / (dpi * 64)
    else:
        a = 0
    if pressed_keys[pg.K_DOWN]:
        s = 1
    else:
        s = 0
    if pressed_keys[pg.K_RIGHT]:
        d = np.pi / (dpi * 64)
    else:
        d = 0
    return(w, a, s, d)#retuen a bool value for keys