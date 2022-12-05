from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut
from math import *    
from random import randint

anchor_burung1_x,anchor_burung1_y = randint(21,450),200
speed_burung1 = 0.3
burung1_mati = False
def burung1():
    global anchor_burung1_y, anchor_burung1_x,speed_burung1
    glPushMatrix()
    glTranslate(anchor_burung1_x,anchor_burung1_y,0)
    anchor_burung1_x += speed_burung1

    if anchor_burung1_x > 480:
        speed_burung1 = -(speed_burung1)
    if anchor_burung1_x < 20:
        speed_burung1 = -(speed_burung1)


    glBegin(GL_POLYGON)             #badan
    posx, posy = -20,25             
    sides = 32    
    radius = 20  
    glColor3ub(219, 103, 53)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glBegin(GL_POLYGON)              #mulut
    glColor3ub(230, 224, 115)
    glVertex2f(-20, 5)
    glVertex2f(-15, 15)
    glVertex2f(-20, 25)
    glVertex2f(-25, 15)
    glEnd()
    
    posx, posy = -29,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -29,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()


    posx, posy = -10,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -10,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glPopMatrix()

anchor_burung2_x,anchor_burung2_y = randint(21,450),400
speed_burung2 = 0.8
burung2_mati = False
def burung2():
    global anchor_burung2_y, anchor_burung2_x, speed_burung2
    glPushMatrix()
    glTranslate(anchor_burung2_x,anchor_burung2_y,0)
    anchor_burung2_x += speed_burung2

    if anchor_burung2_x > 470:
        speed_burung2 = -(speed_burung2)
    if anchor_burung2_x < 20:
        speed_burung2 = -(speed_burung2)


    glBegin(GL_POLYGON)             #badan
    posx, posy = -20,25             
    sides = 32    
    radius = 20  
    glColor3ub(219, 103, 53)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glBegin(GL_POLYGON)              #mulut
    glColor3ub(230, 224, 115)
    glVertex2f(-20, 5)
    glVertex2f(-15, 15)
    glVertex2f(-20, 25)
    glVertex2f(-25, 15)
    glEnd()
    
    posx, posy = -29,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -29,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()


    posx, posy = -10,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -10,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glPopMatrix()

anchor_burung3_x,anchor_burung3_y = randint(21,450),300
speed_burung3 = 0.8
burung3_mati = False
def burung3():
    global anchor_burung3_y, anchor_burung3_x, speed_burung3
    glPushMatrix()
    glTranslate(anchor_burung3_x,anchor_burung3_y,0)
    anchor_burung3_x += speed_burung3
    if anchor_burung3_x > 470:
        speed_burung3 = -(speed_burung3)
    if anchor_burung3_x < 20:
        speed_burung3 = -(speed_burung3)


    glBegin(GL_POLYGON)             #badan
    posx, posy = -20,25             
    sides = 32    
    radius = 20  
    glColor3ub(219, 103, 53)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glBegin(GL_POLYGON)              #mulut
    glColor3ub(230, 224, 115)
    glVertex2f(-20, 5)
    glVertex2f(-15, 15)
    glVertex2f(-20, 25)
    glVertex2f(-25, 15)
    glEnd()
    
    posx, posy = -29,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -29,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()


    posx, posy = -10,29             #mata
    sides = 32    
    radius = 6    
    glBegin(GL_POLYGON)    
    glColor3ub(255, 255, 255)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    posx, posy = -10,29             #pupil
    sides = 32    
    radius = 3    
    glBegin(GL_POLYGON)    
    glColor3ub(0,0,0)
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides) + posx    
        sine  = radius * sin(i*2*pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()

    glPopMatrix()