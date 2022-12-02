from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 
from kecepatan import Speed

class Rectangle(Speed):
    
    def __init__(self,t1:tuple,panjang, lebar) :
        ''' 
        t1 = bottom-left
        t2 = bottom-right
        t3 = top-right
        t4 = top-left
        '''
        self.panjang = panjang
        self.lebar = lebar

        self.t1 = [*t1]
        self.t2 = [None,None]
        self.t3 = [None,None]
        self.t4 = [None,None]
        self.__get_all_point()

        self.__x_translate = 3
        self.__y_translate = 3
    
    def draw(self):
        glColor3ub(0,1,0)

        # glTranslatef(self.__x_translate, self.__y_translate,0)
        glBegin(GL_QUADS)
        glVertex2f(*self.t1)
        glVertex2f(*self.t2)
        glVertex2f(*self.t3)
        glVertex2f(*self.t4)
        glEnd()

    def __get_all_point(self):
        self.t2[0], self.t2[1] = self.t1[0]+self.lebar , self.t1[1]
        self.t3[0], self.t3[1] = self.t1[0]+self.lebar , self.t1[1]+self.panjang
        self.t4[0], self.t4[1] = self.t1[0]            , self.t1[1]+self.panjang
