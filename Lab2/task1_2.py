import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


def draw_3d():
    h = 1.0
    n = 16
    r = 0.5

    delta_fi = 2 * pi / n
    fi = 0
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)

    for i in range(n):
        glNormal3f(cos(fi + delta_fi / 2), sin(fi + delta_fi / 2), 0.0)
        glVertex3f(r * cos(fi), r * sin(fi), h / 2)
        glVertex3f(r * cos(fi), r * sin(fi), -h / 2)
        glVertex3f(r * cos(fi + delta_fi), r * sin(fi + delta_fi), -h / 2)
        glVertex3f(r * cos(fi + delta_fi), r * sin(fi + delta_fi), h / 2)
        fi += delta_fi
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0.0)
    glNormal3f(0, 0, 1)
    for i in range(n):
        glVertex3f(r * cos(fi), r * sin(fi), h / 2)
        fi += delta_fi
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glNormal3f(0, 0, -1)
    for i in range(n):
        glVertex3f(r * cos(fi), r * sin(fi), -h / 2)
        fi += delta_fi
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
        draw_3d()
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
