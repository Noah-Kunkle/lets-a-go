import pygame as pg
import numpy as np
from settings import*
import screens
import music
import setup
import logic
import time
import enimey

def game():
    
    clock=setup.crutal_setup()
    screen=setup.screen_setup(res_x,res_y)
    per_player_x,fov,is_music,sped,mode=setup.setup2(FOV,speeeed,res_x,player_amount)
    pipe,key=music.music_setup()
    run=True
    p1,p2,d1,lvlA1=setup.class_setup(sped,dpi,screen,Scale,fov,res_x,res_y,darkness,dencity,per_player_x)
    enimies=pg.sprite.Group()
    enimey.make_objeckts(enimies,screen)
    for o in enimies:
        pass

    while run:
        current_time=time.time_ns()    
        clock.tick(FPS)
        for e in pg.event.get():
            if e.type==pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                run=False
            if e.type==pg.KEYDOWN and e.key == pg.K_m:
                is_music=not is_music
                is_music=music.backround_music(is_music)
            if e.type == pg.KEYDOWN:
                key.play()
            if e.type==pg.KEYDOWN and e.key==pg.K_SPACE:
                if mode==1 or 2:
                    mode=3
                
            if e.type==pg.KEYDOWN and e.key==pg.K_HOME:
                if mode==3:
                    mode=2
            
        if mode == 1:
            screens.start_test(screen,res_x,res_y)
        elif mode == 2:
            screens.end_text(screen,res_x,res_y,pipe)
        elif mode == 3:
            mode=logic.game_loop(screen,d1,p1,p2,minilvl,clock,lvlA1,res_x,fx,fy,current_time,player_amount,enimies)
        elif mode == 4:
            pass
    pg.quit()
    
game()
        
