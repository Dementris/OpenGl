import pygame as pg
import pygame.image
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_3d():
    h = 1.0
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)

    glNormal3f(0.0, 0.0, 1.0)
    glTexCoord2d(1, 1)
    glVertex3f(h, h, h)
    glTexCoord2d(0, 1)
    glVertex3f(-h, h, h)
    glTexCoord2d(0, 0)
    glVertex3f(-h, -h, h)
    glTexCoord2d(1, 0)
    glVertex3f(h, -h, h)

    glNormal3f(1.0, 0.0, 0.0)
    glTexCoord2d(1, 1)
    glVertex3f(h, h, -h)
    glTexCoord2d(0, 1)
    glVertex3f(h, h, h)
    glTexCoord2d(0, 0)
    glVertex3f(h, -h, h)
    glTexCoord2d(1, 0)
    glVertex3f(h, -h, -h)

    glNormal3f(0.0, 0.0, -1.0)
    glTexCoord2d(1, 1)
    glVertex3f(-h, h, -h)
    glTexCoord2d(0, 1)
    glVertex3f(h, h, -h)
    glTexCoord2d(0, 0)
    glVertex3f(h, -h, -h)
    glTexCoord2d(1, 0)
    glVertex3f(-h, -h, -h)

    glNormal3f(-1.0, 0.0, 0.0)
    glTexCoord2d(1, 1)
    glVertex3f(-h, h, h)
    glTexCoord2d(0, 1)
    glVertex3f(-h, h, -h)
    glTexCoord2d(0, 0)
    glVertex3f(-h, -h, -h)
    glTexCoord2d(1, 0)
    glVertex3f(-h, -h, h)
    # .......код з методчних вказівок

    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2d(1, 1)
    glVertex3f(-h, h, -h)
    glTexCoord2d(0, 1)
    glVertex3f(h, h, -h)
    glTexCoord2d(0, 0)
    glVertex3f(h, h, h)
    glTexCoord2d(1, 0)
    glVertex3f(-h, h, h)

    glNormal3f(0.0, -1.0, 0.0)
    glTexCoord2d(1, 1)
    glVertex3f(-h, -h, -h)
    glTexCoord2d(0, 1)
    glVertex3f(h, -h, -h)
    glTexCoord2d(0, 0)
    glVertex3f(h, -h, h)
    glTexCoord2d(1, 0)
    glVertex3f(-h, -h, h)

    glEnd()

def load_bmp_texture(img):
    textureSurface = pygame.image.load(img)

    textureData = pygame.image.tostring(textureSurface, "RGBA", True)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, textureData)
    return texture, width, height

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

    mult = 1
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
        load_bmp_texture('texture.bmp')
        # Texture modification
        glMatrixMode(GL_TEXTURE)
        glLoadIdentity()
        glScale(mult, mult, mult)
        glMatrixMode(GL_MODELVIEW)

        glRotate(abs(x or y), x, y, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_3d()
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
