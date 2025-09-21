import pygame as pg



def backround_music(o):
    if o==1:
        pg.mixer.music.load("2023-09-07 14-34-42.mp3")
        pg.mixer.music.set_volume(.5)
        pg.mixer.music.play(-1)
    else:
        pg.mixer.music.stop()
    return(o)

def music_setup():
    hit_wall=pg.mixer.Sound("metal-pipe-falling-sound-effect-By-Tuna.mp3")
    key_press=pg.mixer.Sound("194796__jim-ph__vintage-keyboard-2.wav")
    backround_music(1)
    return(hit_wall,key_press)
