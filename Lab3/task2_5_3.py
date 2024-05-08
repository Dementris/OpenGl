import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, sin, cos


def draw_3d(angle):
    n = 90
    h = 1.0
    r1 = 1.0
    r2 = 0.5

    delta_fi = 2 * pi / n
    glDisable(GL_LIGHTING)

    for k in range(2):
        fi = 0
        glBegin(GL_QUAD_STRIP)
        for i in range(n + 1):
            red = abs(sin(2 * angle * pi / 180 + fi))
            blue = abs(sin(3 * angle * pi / 180 + fi))
            green = abs(sin(angle * pi / 180 + fi))
            glColor3f(red, blue, green)
            glVertex3f(r1 * cos(fi), r1 * sin(fi), -h + 2 * h * k)
            red = abs(sin(5 * angle * pi / 180 + fi))
            blue = abs(sin(7 * angle * pi / 180 + fi))
            green = abs(sin(3 * angle * pi / 180 + fi))
            glColor3f(red, green, blue)
            glVertex3f(r2 * cos(fi), r2 * sin(fi), 0)
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
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.1, 0.0, 0.2, 0.0)
    # -------------------
    angle = 0
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
        draw_3d(angle)
        angle = angle + 1 if angle <= 360 else 0
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
