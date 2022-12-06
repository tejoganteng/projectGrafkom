from OpenGL.GL import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut
from OpenGL.GLU import *
from math import *    
from random import randint


#------------------------------text------------------------
def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()
       
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()
#-------------------------Asset-----------------------------------
anchor_burung1_x,anchor_burung1_y = randint(71,450),200
speed_burung1 = randint(30,80)/100
burung1_mati = False
def burung1():
    global anchor_burung1_y, anchor_burung1_x,speed_burung1
    glPushMatrix()
    glTranslate(anchor_burung1_x,anchor_burung1_y,0)
    anchor_burung1_x += speed_burung1

    if anchor_burung1_x > 480:
        speed_burung1 = -(speed_burung1)
    if anchor_burung1_x < 70:
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

anchor_burung2_x,anchor_burung2_y = randint(71,450),400
speed_burung2 = randint(30,80)/100
burung2_mati = False
def burung2():
    global anchor_burung2_y, anchor_burung2_x, speed_burung2
    glPushMatrix()
    glTranslate(anchor_burung2_x,anchor_burung2_y,0)
    anchor_burung2_x += speed_burung2

    if anchor_burung2_x > 470:
        speed_burung2 = -(speed_burung2)
    if anchor_burung2_x < 70:
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

anchor_burung3_x,anchor_burung3_y = randint(71,450),300
speed_burung3 = 0.8
burung3_mati = False
def burung3():
    global anchor_burung3_y, anchor_burung3_x, speed_burung3
    glPushMatrix()
    glTranslate(anchor_burung3_x,anchor_burung3_y,0)
    anchor_burung3_x += speed_burung3
    if anchor_burung3_x > 470:
        speed_burung3 = -(speed_burung3)
    if anchor_burung3_x < 70:
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

anchor_ketapel_x, anchor_ketapel_y = 100,0
speed_ketapel = 10
def ketapel():
    global anchor_ketapel_x, anchor_ketapel_y
    glPushMatrix()
    glTranslate(anchor_ketapel_x,anchor_ketapel_y,0)
    glBegin(GL_POLYGON)         #sisi kanan
    glColor3ub(100,100,100)
    x = 120
    glVertex2f(100-x,62)
    glVertex2f(67-x,70)
    glVertex2f(100-x,90)
    glEnd()
    
    glBegin(GL_POLYGON)         #sisi kiri
    glColor3ub(100,100,100)
    glVertex2f(135-x,61.62)
    glVertex2f(169-x,69)
    glVertex2f(140-x,90)
    glEnd()
    
    glBegin(GL_POLYGON)         #gagang
    glColor3ub(150-x,150,150)
    glVertex2f(100-x,0)
    glVertex2f(135.2-x,0)
    glVertex2f(135.2-x,62)
    glVertex2f(100-x,61.62)
    glEnd()
    glPopMatrix()

def tiang(x=0,y=0):
    glPushMatrix()
    glTranslated(x,y,0)

    glBegin(GL_POLYGON)
    glColor3ub(47, 50, 69)
    glVertex2f(0,0)
    glVertex2f(40,0)
    glVertex2f(40,450)
    glVertex2f(0,450)
    glEnd()

    glPopMatrix()

def papan(x,y):
    glPushMatrix()
    glTranslated(x,y,0)

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0,0)
    glVertex2f(480,0)
    glVertex2f(480,5)
    glVertex2f(0,5)
    glEnd()

    glPopMatrix()

def background():
    glPushMatrix()

    glBegin(GL_POLYGON)
    glColor3ub(159, 237, 193)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,500)
    glVertex2f(0,500)
    glEnd()

    glPopMatrix()


#----------------------------rock-----------------------------
ammunition = 4
rock1_speed = 0
anchor_rock_x, anchor_rock_y = anchor_ketapel_x, 70
on_animation = False
last_pos_x = 0
def rock1():
    global on_animation,ammunition, rock1_speed, anchor_rock_x, anchor_rock_y
    glPushMatrix()
    if not on_animation:
        glTranslate(anchor_rock_x,anchor_rock_y,0)  #fungsi translate sebelum nembak
        anchor_rock_y += rock1_speed
    else:
        glTranslated(last_pos_x,anchor_rock_y,0)    #fungsi translate setelah nembak
        anchor_rock_y += rock1_speed



    if anchor_rock_y > 510: #jika sudah melewati window
        # if ammunition
        rock1_speed = 0
        anchor_rock_y = 70
        on_animation = False


    glBegin(GL_POLYGON)
    glColor3ub(100,0,100)
    x = 10
    y = 10
    glVertex2f(-15.1845398351986,23.207060810307)
    glVertex2f(14.4762602738399-x,22.5759799569231)
    glVertex2f(18.8149411408535-x,0.8825756218549+y)
    glVertex2f(-1-x,-10.0753563664078+3+y)
    glVertex2f(-20.5,0+y)
    glEnd()

    glPopMatrix()



#--------------------------game state------------------------------
on_menu = True
on_game = False
on_pause = False
def menu():
    glBegin(GL_POLYGON)
    glColor3ub(177, 217, 176)
    glVertex2f(0,0)
    glVertex2f(500,0)
    glVertex2f(500,500)
    glVertex2f(0,500)
    glEnd()
    drawTextBold("P L A Y",230,250)
    drawText("Tekan T untuk mulai",200,230,0,0,0)

temp={
    'speed_burung1' : speed_burung1,
    'speed_burung2' : speed_burung2,
    'speed_burung3' : speed_burung3,
    'speed_ketapel' : speed_ketapel,
    'rock1_speed'   : rock1_speed
}
def pause():
    global speed_burung1,speed_burung2,speed_burung3,speed_ketapel,on_pause,rock1_speed
    
    if on_pause:
        speed_burung1 = 0
        speed_burung2 = 0
        speed_burung3 = 0 
        speed_ketapel = 0
    else:
        speed_burung1 = -temp['speed_burung1']
        speed_burung2 = -temp['speed_burung2']
        speed_burung3 = -temp['speed_burung3']
        speed_ketapel = temp['speed_ketapel']
        rock1_speed = temp['rock1_speed']

def gameover():
    global ammunition, burung1_mati,burung2_mati,burung3_mati,on_animation,on_gameover

    if (burung1_mati and burung2_mati and burung3_mati and not on_animation):
        glBegin(GL_POLYGON)
        glColor3ub(177, 217, 176)
        glVertex2f(0,0)
        glVertex2f(500,0)
        glVertex2f(500,500)
        glVertex2f(0,500)
        glEnd()
        drawText("Kamu Menang!",200,250,0,0,0)
    elif (ammunition == 0 and not on_animation) :         
        glBegin(GL_POLYGON)
        glColor3ub(177, 217, 176)
        glVertex2f(0,0)
        glVertex2f(500,0)
        glVertex2f(500,500)
        glVertex2f(0,500)
        glEnd()
        drawText("Kamu Kalah!",200,250,0,0,0)
    on_gameover = True
#----------------------------game logic---------------------------------------
def game():
    global ammunition
    global last_pos_x, anchor_rock_y
    global anchor_burung1_x,anchor_burung1_y
    global anchor_burung2_x,anchor_burung2_y
    global anchor_burung3_x,anchor_burung3_y
    global burung3_mati,burung2_mati,burung1_mati

    x_burung_offset = -10
    y_burung_offset = 40                #geser garis collision agar sesuai lebar objek
    burung1_line_collision = [
        [anchor_burung1_x-17+x_burung_offset,anchor_burung1_y+y_burung_offset],[anchor_burung1_x+17+x_burung_offset,anchor_burung1_y+y_burung_offset]]
    burung2_line_collision = [
        [anchor_burung2_x-17+x_burung_offset,anchor_burung2_y+y_burung_offset],[anchor_burung2_x+17+x_burung_offset,anchor_burung2_y+y_burung_offset]]
    burung3_line_collision = [
        [anchor_burung3_x-17+x_burung_offset,anchor_burung3_y+y_burung_offset],[anchor_burung3_x+17+x_burung_offset,anchor_rock_y+y_burung_offset]]
    
    rock_t1_kiri = [last_pos_x-17,anchor_rock_y+70]
    rock_t2_kanan = [last_pos_x+17,anchor_rock_y+70]
    x,y = 0,1

    #-------------------------------collision-----------------------------------
    if burung1_line_collision[0][y]<rock_t1_kiri[y]<burung1_line_collision[0][y]+20:   
        if burung1_line_collision[0][x]< rock_t1_kiri[x] < burung1_line_collision[1][x]\
        or burung1_line_collision[0][x]< rock_t2_kanan[x] < burung1_line_collision[1][x]:
            burung1_mati = True   
    
    if burung2_line_collision[0][y]<rock_t1_kiri[y]<burung2_line_collision[0][y]+20:   #cek y
        if burung2_line_collision[0][x]< rock_t1_kiri[x] < burung2_line_collision[1][x] or\
        burung2_line_collision[0][x]< rock_t2_kanan[x] < burung2_line_collision[1][x]:
            burung2_mati = True     
    
    if burung3_line_collision[0][y]<rock_t1_kiri[y]<burung3_line_collision[0][y]+20:   #cek y
        if burung3_line_collision[0][x]< rock_t1_kiri[x] < burung3_line_collision[1][x] or\
        burung3_line_collision[0][x]< rock_t2_kanan[x] < burung3_line_collision[1][x]:
            burung3_mati = True    
    #----------------------------draw asset---------------------------------------
    #---background---
    background()
    tiang()
    papan(0,200)
    papan(0,300)
    papan(0,400)
    tiang(470)
    #----------------
    if not burung1_mati:
        burung1()
    if not burung2_mati:
        burung2()
    if not burung3_mati:
        burung3()
    ketapel()

    if ammunition >= 0:
        rock1()
    
    drawText(f'Rock Ammunition : {ammunition}',10,10,0,0,0)
    drawText(f'P = Pause',400,10,0,0,0)

    if on_pause:
        drawTextBold(f'Game Paused!',200,250)


        
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global on_menu,on_game,on_pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()

    if on_menu:
        menu()
    if on_game:
        game()
        gameover()
    
    glutSwapBuffers()


#--------------------------Control------------------------------------
def spesial_key(key,a,b):
    global speed_ketapel,anchor_ketapel_x, anchor_rock_x
    if key == GLUT_KEY_LEFT:
        x_after_translated_ketapel = anchor_ketapel_x  - speed_ketapel  
        print(x_after_translated_ketapel, '--', anchor_rock_x)

        if x_after_translated_ketapel > 20:
            anchor_ketapel_x -= speed_ketapel
            anchor_rock_x -= speed_ketapel

    if key == GLUT_KEY_RIGHT: 
        x_after_translated_ketapel = anchor_ketapel_x + speed_ketapel 
        print(x_after_translated_ketapel, '--', anchor_rock_x)
        if x_after_translated_ketapel < 480:
            anchor_ketapel_x += speed_ketapel 
            anchor_rock_x += speed_ketapel

def normal_key(key,a,b):
    global rock1_speed,on_animation,last_pos_x, anchor_ketapel_x, ammunition
    if key == b' ' and not on_animation:
        
        if ammunition > 0 :
            rock1_speed =1
            on_animation = True
            last_pos_x = anchor_ketapel_x
            ammunition -= 1
            print(ammunition)
            return True
    #------------ State Controller -------------------------------------------
    global on_game,on_menu,on_pause,on_gameover
    if key == b't':
        on_game = True
        on_menu = False
    
    if key == b'p' and on_game:
        on_pause = not on_pause
        print(on_pause)
        pause()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(450, 100)
wind = glutCreateWindow("Precision Bullet")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(normal_key)
glutSpecialFunc(spesial_key)
glutMainLoop()

            
    
