from math import *
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_3d(n, pos, mode='default'):
    h = 1.0
    r = 0.5

    delta_fi = 2 * pi / n
    teta = atan(h / r)
    fi = 0

    if mode == 'line':
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(4)
        glEnable(GL_LINE_SMOOTH)
    elif mode == 'dots':
        glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
        glPointSize(15)
        glEnable(GL_POINT_SMOOTH)
    else: glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glPushMatrix()
    glTranslatef(pos[0], pos[1], pos[2])
    glBegin(GL_TRIANGLES)
    for i in range(n):
        glColor3f(i % 2, (i % 3) / 2, (i % 5) / 4)
        glNormal3f(cos(fi + delta_fi / 2) * sin(teta),
                   sin(fi + delta_fi / 2) * sin(teta),
                   cos(teta))
        glVertex3f(0, 0, h)
        glVertex3f(r * cos(fi), r * sin(fi), 0)
        glVertex3f(r * cos(fi + delta_fi),
                   r * sin(fi + delta_fi), 0)

        glColor3f(1, 1, 1)
        glNormal3f(cos(fi + delta_fi / 2) * sin(teta),
                   sin(fi + delta_fi / 2) * sin(teta),
                   -cos(teta))
        glVertex3f(0, 0, 0)
        glVertex3f(r * cos(fi), r * sin(fi), 0)
        glVertex3f(r * cos(fi + delta_fi),
                   r * sin(fi + delta_fi), 0)
        fi += delta_fi
    glEnd()
    glPopMatrix()


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


if __name__ == '__main__':

    obj_pos1 = (-1, 0, 0)
    obj_pos2 = (1, 0, 0)

    pg.init()
    display = (800, 600)
    # OnCreate
    pg.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.1, 0.0, 0.2, 0.0)
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
        glRotate(abs(x or y), x, y, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_3d(16, obj_pos1, mode='dots')
        draw_3d(4, obj_pos2)
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
