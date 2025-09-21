import pygame as pg
import numpy as np
import enimey
from settings import*


class draw:
    def __init__(self,screen,scale,lvl,fov,x_res,y_res,darkness,clarity):
        self.screen=screen
        self.scale=scale
        self.lvl=lvl
        self.fov=fov
        self.x_res=x_res
        self.y_res=y_res
        self.darkness=darkness
        self.clarity=clarity
        self.dis_factor=3
        self.item_scale=100
        self.area=1
        self.coin=pg.image.load('coin.png').convert_alpha()

    def plaer_draw(self,rot,x,y,offset):
        carictor=pg.image.load('player_stand.png')
        carictor=pg.transform.scale(carictor,(self.scale,self.scale))
        carictor=pg.transform.rotate(carictor,-(rot)*(180/np.pi)-90)
        thick=pg.Surface.get_width(carictor)
        self.screen.blit(carictor,(x*self.scale+offset-thick/2-.5,y*self.scale-thick/2-.5))
    def draw_lines(self,xpos,ypos,rot,lvl,offset):
        h_res=self.y_res/2
        j=0.02
        mod=(self.x_res)/(self.fov*self.clarity)
        for i in range(self.fov*self.clarity):
            rot_b=(np.deg2rad(i-((self.fov/(2/self.clarity))))/(self.clarity*2))
            rot_i=rot+rot_b
            x,y=(xpos,ypos)
            sin,cos,cos2=(j*np.sin(rot_i),j*np.cos(rot_i),j*np.cos(rot_b))
            n=0
            while(True):
                x,y=(x+cos,y+sin)
                n=n+1
                wall,color=lvl[int(y)][int(x)]
                if wall!=0 or n==int(255/self.darkness):
                    h=(((h_res)/n)/cos2)
                    break
            r,g,b=color
            r,g,b=r-n*self.darkness,g-n*self.darkness,b-n*self.darkness
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0
            color=r,g,b
            imod=i*mod+offset
            pg.draw.line(self.screen,color,[imod,h+h_res],[imod,-h+h_res],int(mod)+1)
            
    def box_draw(self,lvl,offset):
        for i in range(len(lvl[0])): # x position
            for j in range(len(lvl[1])): # y postiotion
                wall, color = lvl[i][j] # Access the current element
                pg.draw.rect(self.screen,color,[(j*self.scale)+offset,(i*self.scale),self.scale+1,self.scale+1])
                         
    def draw_entitys(self,entitys,player,lvl,offset):
        pixles_per_degree=self.x_res/self.fov*2
        pixles_per_rad=(pixles_per_degree*180)/np.pi
        coin_gain=0
        for i in entitys:
            angle,dis=enimey.entity.player_dis(i,player)
            player_rot=player.rotation
            while (player_rot>2*np.pi):
                player_rot-=2*np.pi
            while (player_rot<0):
                player_rot+=2*np.pi
            angle_b=angle-2*np.pi
            angle_c=angle+2*np.pi

            if dis<self.dis_factor:
                billy=(player_rot-angle)*pixles_per_rad
                billy_b=(player_rot-angle_b)*pixles_per_rad
                billy_c=(player_rot-angle_c)*pixles_per_rad
                half_width=self.x_res/2
                half_hight=self.y_res/2
                scale=(self.item_scale-dis*33)*3
                coin_new = pg.transform.scale(self.coin,(scale,scale))
                size=pg.Surface.get_width(coin_new)
                self.screen.blit(coin_new,(-billy+half_width-size/2,half_hight-size/2))
                self.screen.blit(coin_new,(-billy_b+half_width-size/2,half_hight-size/2))
                self.screen.blit(coin_new,(-billy_c+half_width-size/2,half_hight-size/2))

                if dis<.35:
                    i.suerside()
                    player.coin_amount+=1
                    
        font=pg.font.SysFont("Arial",40)
        text=font.render((f"Coin {player.coin_amount}"),True,(50,50,255))
        self.screen.blit(text,(20,res_y-50))
            
            
            
    
