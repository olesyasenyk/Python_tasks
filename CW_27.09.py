import pygame
pygame.init()

gameDisplay=pygame.display.set_mode((400,400))
pygame.display.set_caption('My first game')
done=False
clock=pygame.time.Clock()

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14

while not done:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            pygame.draw.arc(gameDisplay, WHITE, (10, 50, 280, 100), 0, PI) 
        if event.type==pygame.QUIT:
            done=True

    # pygame.draw.arc(gameDisplay, WHITE, (10, 50, 280, 100), 0, PI)
    # pygame.draw.arc(gameDisplay, PINK, (50, 30, 200, 150), PI, 2*PI, 3)

pygame.display.update()
clock.tick(60)





# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сatch the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r,ball
#     canv.delete(ball)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)

     
     
# def click(event):
#     global points, x, text
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
#         x = -1000
# #видалення круга при кліку
#         canv.delete(text)
#         canv.delete(ball)
#         text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 


        

# #щоб не можна було «накручувати» очки, 
# # клікаючи багато разів по кругу, 
# # поки він не зникне

# #Після кліку круг не зникає і це не ok.
# #Можна видалити все 
# # canv.delete(ALL), 
# # але тоді буде видалятись і рахунок

# #краще дати імена всім графічним примітивам
# # (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
# #щоб можна було видалити ball, треба перед викликом 
# #функції ball() намалювати цей ball
# ball = canv.create_oval(-100,0,0,0)
# text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)


# mainloop()





from tkinter import *
from random import randrange as rnd, choice
import time

# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Drag the BALL")
 
canv = Canvas(root,bg='black')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r,ball
    #canv.delete(ball)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    # root.after(1000,new_ball)

     
     
def motion(event):
    global x
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        True
     


    # without trace
        # screen.fill((0,0,0))          



        # points += 1
        # x = -1000
#видалення круга при кліку
        #canv.delete(text)
        # canv.delete(ball)
        #text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 


        

#щоб не можна було «накручувати» очки, 
# клікаючи багато разів по кругу, 
# поки він не зникне

#Після кліку круг не зникає і це не ok.
#Можна видалити все 
# canv.delete(ALL), 
# але тоді буде видалятись і рахунок

#краще дати імена всім графічним примітивам
# (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
#щоб можна було видалити ball, треба перед викликом 
#функції ball() намалювати цей ball
# ball = canv.create_oval(-100,0,0,0)
# text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
# points = 0
# new_ball()
canv.bind('<Button-1>', motion)


mainloop()