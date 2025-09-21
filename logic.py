import numpy as np
import pygame as pg
import LVl
import player
import draw


        
        
        
        
def game_loop(screen,d1,p1,p2,minilvl,clock,lvlA1,res_x,fx,fy,current_time,player_amount,entitys):        
        screen.fill([0,0,0])
        pg.display.set_caption("Raycasting - FPS: "+str(round(clock.get_fps())))
        if player_amount==2:
            d1.draw_lines(p1.get_posx(),p1.get_posy(),p1.get_rot(),lvlA1,0)
            d1.draw_lines(p2.get_posx(),p2.get_posy(),p2.get_rot(),lvlA1,res_x/2)
            p1.move_player()
            p2.move_player()
            if minilvl:
                d1.box_draw(p1.lvl,0)
                d1.box_draw(p2.lvl,res_x/2)
                d1.plaer_draw(p1.get_rot(),p1.get_posx(),p1.get_posy(),0)
                d1.plaer_draw(p2.get_rot(),p2.get_posx(),p2.get_posy(),res_x/2)
            pg.display.update()
            if(fx==int(p1.get_posx())and fy==int(p1.get_posy()))and(fx==int(p2.get_posx())and fy==int(p2.get_posy())):
                return(2)
            else:
                return(3)

        else:
            d1.draw_lines(p1.get_posx(),p1.get_posy(),p1.get_rot(),lvlA1,0)
            p1.move_player()
            if minilvl:
                d1.box_draw(p1.lvl,0)
                d1.plaer_draw(p1.get_rot(),p1.get_posx(),p1.get_posy(),0)
            d1.draw_entitys(entitys,p1,lvlA1,0)
            pg.display.update()
            if(fx==int(p1.get_posx())and fy==int(p1.get_posy())and player.coin_amount==3):
                return(2)
            else:
                return(3)
