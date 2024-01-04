import pygame
from random import randint
from time import time
import webbrowser
pygame.init()
pygame.display.set_caption('TrueProger and FalseProger')

#zastavka=input('хотите посмотреть заставку?(да/нет)')
#if zastavka=='да':
#    webbrowser.open('https://www.youtube.com/watch?v=AqM-N4h3ViI')

class Chvk():
    def __init__(self,png,x,y,width,heigth):
        self.rect=pygame.Rect(x, y, width, heigth)
        self.png=pygame.image.load(png)
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
    def fill(self):
        pygame.draw.rect(linox,self.fire)

class Bullet():
    def __init__(self,bul,damage,x_b, y_b, width_b, heigth_b):
        self.self.bal=pygame.image.load(bul)
        self.self.damage=damage
        self.fire=pygame.Rect(x_b, y_b+10, width_b, heigth_b)
        self.coor_x=x_b
        self.coor_y=y_b
    def draw_fir(self):
        linox.blit(self.bal,(self.coor_x,self.coor_y))
    def drawfire2(self):
        linox.blit(self.bal,(self.fire.x+5,self.fire.y))
        

f_x=250
f_y=250

bg=pygame.image.load('5.png')
pl=Chvk('pl.png',250,250,50,100)
en=Chvk('en.png',50,250,50,100)

bullett='l'

bull=0

temp=0

move_left=False
move_right=False

linox=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()#создание и сохранение времени в переменную
run=True
#linox.fill((41, 227, 184))
#font=pygame.font.Font(None,30).render('TrueProger_and_FalseProger',True,(227, 68, 248 ))
while run:
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button ==1:
            bullett=('bullet.png',50,pl.rect.x,pl.rect.x,25,10)
            #bullett.draw_fir()
            bull=180
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                move_left=True
            elif event.key==pygame.K_d:
                move_right=True
            
            elif event.key==pygame.K_w:
                pl.rect.y-=30
                temp=160
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                move_left=False
            elif event.key==pygame.K_d:
                move_right=False
                
    if move_left==True:
        pl.rect.x-=1
    if move_right==True:
        pl.rect.x+=1

    if bull<=180 and bull>0:
        bullett.drawfire2()
        bull-=1
    
    linox.blit(bg,(0,0))
    pl.drawd()
    en.drawd()
    
    f_x=pl.rect.x
    f_y=pl.rect.y
    
    
    if pl.rect.y<=220 and temp<=0:
        pl.rect.y=250
    if temp<=160:
        temp-=1
