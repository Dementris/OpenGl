import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, sin, cos
from random import choice

def draw_3d(angle, red, green):
    h = 1.0
    glDisable(GL_LIGHTING)
    glBegin(GL_QUADS)

    glNormal3f(0.0, 0.0, 1.0)
    glColor3f(red, 0, 0)
    glVertex3f(h, h, h)
    glColor3f(red/5, green, 0)
    glVertex3f(-h, h, h)
    glColor3f(red, green, 1)
    glVertex3f(-h, -h, h)
    glColor3f(red, green/5, 0)
    glVertex3f(h, -h, h)

    glNormal3f(1.0, 0.0, 0.0)
    glColor3f(red, 0, 0)
    glVertex3f(h, h, -h)
    glColor3f(red, 0, 0)
    glVertex3f(h, h, h)
    glColor3f(red, 1, 0)
    glVertex3f(h, -h, h)
    glColor3f(0, green, 1)
    glVertex3f(h, -h, -h)

    glNormal3f(0.0, 0.0, -1.0)
    glColor3f(0, red, 0)
    glVertex3f(-h, h, -h)
    glColor3f(red/4, green/5, 1)
    glVertex3f(h, h, -h)
    glColor3f(0, green, red)
    glVertex3f(h, -h, -h)
    glColor3f(red, green, red)
    glVertex3f(-h, -h, -h)

    glNormal3f(-1.0, 0.0, 0.0)
    glColor3f(red, 0, 0)
    glVertex3f(-h, h, h)
    glColor3f(red/4, green/3, 1)
    glVertex3f(-h, h, -h)
    glColor3f(red/3, 0, 0)
    glVertex3f(-h, -h, -h)
    glColor3f(0, green, 0)
    glVertex3f(-h, -h, h)

    glColor3f(red, 0.0, 0.0)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(-h, h, -h)
    glColor3f(red, 0, 0)
    glVertex3f(h, h, -h)
    glColor3f(0, green, 0)
    glVertex3f(h, h, h)
    glColor3f(red, green/4, 0)
    glVertex3f(-h, h, h)
    glColor3f(red/5, green, 0)
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(-h, -h, -h)
    glColor3f(red/6, 0, 1)
    glVertex3f(h, -h, -h)
    glColor3f(0, green/2, 0)
    glVertex3f(h, -h, h)
    glColor3f(red, green, 0)
    glVertex3f(-h, -h, h)
    glEnd()


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


if __name__ == '__main__':
    pg.init()
    display = (800, 600)
    # OnCreate
    pg.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.1, 0.0, 0.2, 0.0)
    angle = 1
    variable_color1= 0
    variable_color2 = 1
    # -------------------
    while True:
        for event in pg.event.get():
            # OnDestroy
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            #     ------------------
            elif event.type == VIDEORESIZE:
                resize(event.w, event.h)

        keys = pg.key.get_pressed()
        x, y = 0, 0
        x += keys[pg.K_RIGHT] - keys[pg.K_LEFT]
        y += keys[pg.K_DOWN] - keys[pg.K_UP]
        # OnPaint

        glRotate(angle, 1, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        variable_color1 += angle / 1000
        variable_color2 -= angle / 1000
        if variable_color1 >= 1 and variable_color2 <= 0 or variable_color1 <= 0 and variable_color2 >= 1:
            angle *= -1

        draw_3d(angle, variable_color1, variable_color2)
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
