import pygame as pg
import numpy as np
import music

def end_text(screen,x,y,pipe):
    music.backround_music(0)
    pipe.play()
    screen.fill([50,50,50])
    font=pg.font.SysFont("Arial",200)
    text2=font.render("You Win",True,(50,50,255))
    screen.blit(text2,(x/2-300,y/2-50))
    pg.display.flip()
    pg.display.update
    
def start_test(screen,x,y):
    music.backround_music(1)
    screen.fill([50,50,50])
    font=pg.font.SysFont("Arial",200)
    text2=font.render("Hello",True,(50,50,255))
    screen.blit(text2,(x/2-300,y/2-50))
    pg.display.flip()
    pg.display.update
