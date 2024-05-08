import math

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


def calculate_rgb(width, height):
    # Create a grayscale image with a radial gradient.
    grayscale_image = np.zeros((height, width), dtype=np.float32)
    center_x = width // 2
    center_y = height // 2
    radius = min(center_x, center_y)

    for y in range(height):
        for x in range(width):
            dist = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            angle = np.arctan2(y - center_y, x - center_x)
            spiral_value = (1 - dist / radius) * np.cos(angle * 15 + dist / radius * 5) * 0.5 + 0.5
            grayscale_image[y, x] = spiral_value

    # Convert the grayscale image to RGB.
    rgb_image = np.stack([grayscale_image, grayscale_image, grayscale_image-0.5], axis=-1)

    # Rescaling before conversion
    rgb_image *= 255
    return rgb_image.astype(np.uint8)


def calculate_texture():
    texture = calculate_rgb(100, 100)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, 100, 100, GL_RGB, GL_UNSIGNED_BYTE, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


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
        calculate_texture()
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
