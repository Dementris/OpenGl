import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from colors import Colors

def draw_axis():
    h = 1.0
    glDisable(GL_LIGHTING)
    glLineWidth(4)
    glBegin(GL_LINES)
    # OX
    glColor3fv(Colors.RED)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(800.0, 0.0, 0.0)
    # OY
    glColor3fv(Colors.BLUE)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 800.0, 0.0)
    # OZ
    glColor3fv(Colors.GREEN)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 800.0)

    glEnd()

    glEnable(GL_LIGHTING)

def draw_3d(angle):
    glPushMatrix()
    draw_axis()
    glPopMatrix()
    glPushMatrix()
    glRotate(angle, 0, 1, 0)
    light = [1.0, 1.0, 1.0, 0]
    glLightfv(GL_LIGHT0, GL_POSITION, light)
    glColor3fv(Colors.LEMON)
    glutSolidTeapot(2)
    glPopMatrix()

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def on_paint(width, height, angle):
    # XOY
    glViewport(0, h // 2 + 1, w // 2 + 1, h // 2 + 1)
    glScissor(0, h // 2 + 1, w // 2 + 1, h // 2 + 1)
    glClearColor(0.9, 0.7, 0.8, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0)
    draw_3d(angle)
    glPopMatrix()
    # XOZ
    glViewport(0, 0, w // 2 + 1, h // 2 + 1)
    glScissor(0, 0, w // 2 + 1, h // 2 + 1)
    glClearColor(0.8, 0.9, 0.7, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1)
    draw_3d(angle)
    glPopMatrix()
    # YOZ
    glViewport(w // 2 + 1, h // 2, w // 2, h // 2)
    glScissor(w // 2 + 1, h // 2, w // 2, h // 2)
    glClearColor(0.8, 0.8, 0.9, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    draw_3d(angle)
    glPopMatrix()
    # XYZ
    glViewport(w // 2 + 1, 0, w // 2, h // 2)
    glScissor(w // 2 + 1, 0, w // 2, h // 2)
    glClearColor(0.9, 0.8, 0.8, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(4.5, 4.5, 4.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    draw_3d(angle)
    glPopMatrix()


if __name__ == '__main__':
    angle = 0.0

    pg.init()
    display = (800, 600)
    glutInit()
    # OnCreate
    screen = pg.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_SCISSOR_TEST)
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
                pg.display.set_mode((event.w, event.h), DOUBLEBUF | OPENGL | RESIZABLE)
        # OnPaint
        w, h = pg.display.Info().current_w, pg.display.Info().current_h

        on_paint(w, h, angle)

        angle += 0.5
        if angle > 360.0:
            angle = 0.0
        # -----------------
        pg.display.flip()
        pg.time.wait(10)
