from math import *
import pygame
#my Inspiration:
# https://www.youtube.com/watch?v=uWzPe_S-RVE&t=1595s

#screen width and height
width = 600
height = 600

#fixpoint for the Pendulum
zerox = width/2
zeroy = 150
clock = pygame.time.Clock()

#PI = pi... dont ask me
PI = pi

#length of the rods
r1 = 100
r2 = 100

#starting angle for the rods
a1 = PI/4
a2 = PI/2

#starting velocity and acceleration
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0

#mass (and size) of the Pendulum
m1 = 10
m2 = 15

x1 = zerox + sin(a1) * r1
y1 = zeroy + cos(a1) * r1

x2 = x1 + sin(a2) * r2
y2 = y1 + cos(a2) * r2

#gravity, let it be a small number, dont even think about something like 9.81 or so... or think about it, im a Comment, not a Cop
g = 0.2

run = True

#initialising Pygame
pygame.init()


#creating the Window (i think, this is not even necessary, but idc, it works)
window = pygame.display.set_mode((width, height))
window.fill((255, 255, 255))
pygame.display.set_caption('Double Pendulum')

'''
creating the Surface for the Pendulum and the drawn line with per-pixel Alpha values
I did this, so all the lines that have already been drawn, don't have to be drawn every frame (which ultimately slows your Programm down) and instead are drawn only once
'''
pensur = pygame.Surface((int(width),int(height)),pygame.SRCALPHA)
linesur = pygame.Surface((int(width),int(height)),pygame.SRCALPHA)
linesur.fill((255, 255, 255))

while run:
    window.fill((255, 255, 255))
    pensur.fill((255, 255, 255, 0))

    # limiting the iterations in a second (not necessary)
    #clock.tick(120)

    #previous x and y values for the line drawing
    px = x2
    py = y2

    #updating x and y values, angles and forces
    x1 = zerox + sin(a1) * r1
    y1 = zeroy + cos(a1) * r1
    x2 = x1 + sin(a2) * r2
    y2 = y1 + cos(a2) * r2
    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    #calculating the acceleration:
    term11 = -g*(2*m1 + m2)*sin(a1)
    term12 = -m2*g*sin(a1-2*a2)
    term13 = -2*sin(a1-a2)*m1*(((a2_v)**2)*r2 + ((a1_v)**2)*r1*cos(a1-a2))
    div1 = r1*(2+m1+m2-m2*cos(2*a1-2*a2))

    a1_a = (term11 + term12 + term13)/div1

    term21 = 2*sin(a1-a2)
    term22 = ((a1_v)**2)*r1*(m1+m2)
    term23 = g*(m1+m2)*cos(a1)
    term24 = ((a2_v)**2)*r2*m2*cos(a1-a2)
    div2 = r2*(2+m1+m2-m2*cos(2*a1-2*a2))

    a2_a = (term21 * (term22 + term23 + term24)) / div2


    #drawing the Double Pendulum:
    pygame.draw.line(pensur, (0, 0, 0,255), (int(zerox), int(zeroy)), (int(x1), int(y1)), 1)
    pygame.draw.circle(pensur, (0, 0, 0,255), (int(x1), int(y1)), m1)
    pygame.draw.line(pensur, (0, 0, 0,255), (int(x1), int(y1)), (int(x2), int(y2)), 1)
    pygame.draw.circle(pensur, (0, 0, 0,255), (int(x2), int(y2)), m2)

    pygame.draw.line(linesur, (0, 255, 0, 255), (int(px), int(py)),(int(x2), int(y2)), 1)

    window.blit(linesur,(0,0))
    window.blit(pensur,(0,0))

    #updating display
    pygame.display.update()

    #closing the Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()