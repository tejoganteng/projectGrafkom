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
