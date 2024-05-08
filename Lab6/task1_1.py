import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from colors import Colors


def draw_3d():
    h = 1.0

    glBegin(GL_QUADS)

    glColor3f(1.0, 0.0, 0.0)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(h, h, h)
    glVertex3f(-h, h, h)
    glVertex3f(-h, -h, h)
    glVertex3f(h, -h, h)
    glColor3f(0.0, 0.0, 1.0)
    glNormal3f(1.0, 0.0, 0.0)
    glVertex3f(h, h, -h)
    glVertex3f(h, h, h)
    glVertex3f(h, -h, h)
    glVertex3f(h, -h, -h)
    glColor3f(0.0, 1.0, 0.0)
    glNormal3f(0.0, 0.0, -1.0)
    glVertex3f(-h, h, -h)
    glVertex3f(h, h, -h)
    glVertex3f(h, -h, -h)
    glVertex3f(-h, -h, -h)
    glColor3f(1.0, 1.0, 0.0)
    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(-h, h, h)
    glVertex3f(-h, h, -h)
    glVertex3f(-h, -h, -h)
    glVertex3f(-h, -h, h)
    # .......код з методчних вказівок

    glColor3f(0.0, 1.0, 1.0)
    glNormal3f(0.0, 1.0, 0.0)
    glVertex3f(-h, h, -h)
    glVertex3f(h, h, -h)
    glVertex3f(h, h, h)
    glVertex3f(-h, h, h)

    glColor3f(1.0, 1.0, 1.0)
    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(-h, -h, -h)
    glVertex3f(h, -h, -h)
    glVertex3f(h, -h, h)
    glVertex3f(-h, -h, h)

    glEnd()


def draw_axis():
    h = 1.0
    glDisable(GL_LIGHTING)
    glLineWidth(4)
    glBegin(GL_LINES)
    # OX
    glColor3fv(Colors.RED)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    # OY
    glColor3fv(Colors.BLUE)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    # OZ
    glColor3fv(Colors.GREEN)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()

    glEnable(GL_LIGHTING)


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def on_paint(width, height):

    # XOY
    glViewport(0, h//2+1, w//2+1, h //2+1)
    glScissor(0, h//2+1, w//2+1, h //2+1)
    glClearColor(0.9, 0.7, 0.8, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0)
    draw_axis()
    glPopMatrix()
    # XOZ
    glViewport(0, 0, w // 2 + 1, h // 2 + 1)
    glScissor(0,0, w // 2 + 1, h // 2 + 1)
    glClearColor(0.8, 0.9, 0.7, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1)
    draw_axis()
    glPopMatrix()
    # YOZ
    glViewport(w // 2 + 1, h // 2, w // 2, h // 2)
    glScissor(w // 2 + 1, h // 2, w // 2, h // 2)
    glClearColor(0.8, 0.8, 0.9, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    draw_axis()
    glPopMatrix()
    # XYZ
    glViewport(w // 2 + 1, 0, w // 2, h // 2)
    glScissor(w // 2 + 1, 0, w // 2, h // 2)
    glClearColor(0.9, 0.8, 0.8, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    gluLookAt(4.5, 4.5, 4.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    draw_axis()
    glPopMatrix()




if __name__ == '__main__':
    pg.init()
    display = (800, 600)
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
        print(w, h)
        on_paint(w, h)
        # -----------------
        pg.display.flip()
        pg.time.wait(10)
