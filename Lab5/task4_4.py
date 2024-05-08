import pygame as pg
import pygame.image
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import pi, sin, cos


def draw_3d(arr):
    h = 1.0
    n = 8
    r = h * 1.2
    glBindTexture(GL_TEXTURE_2D, arr[0])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
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

    # glNormal3f(0.0, 1.0, 0.0)
    # glTexCoord2d(1, 1)
    # glVertex3f(-h, h, -h)
    # glTexCoord2d(0, 1)
    # glVertex3f(h, h, -h)
    # glTexCoord2d(0, 0)
    # glVertex3f(h, h, h)
    # glTexCoord2d(1, 0)
    # glVertex3f(-h, h, h)

    # glNormal3f(0.0, -1.0, 0.0)
    # glTexCoord2d(1, 1)
    # glVertex3f(-h, -h, -h)
    # glTexCoord2d(0, 1)
    # glVertex3f(h, -h, -h)
    # glTexCoord2d(0, 0)
    # glVertex3f(h, -h, h)
    # glTexCoord2d(1, 0)
    # glVertex3f(-h, -h, h)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, arr[1])
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_BLEND)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0.0, 1, 0.0)
    glTexCoord2d(0.5, 0.5)
    glVertex3f(0.0, r, 0.0)

    for i in range(n + 1):
        glTexCoord2d(0.5 + 0.5 * cos(i * 2 * pi / n),
                     0.5 + 0.5 * sin(i * 2 * pi / n))
        glVertex3f(r * cos(2 * pi / n * i), h, r * sin(2 * pi / n * i))
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
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, width, height, GL_RGBA,
                      GL_UNSIGNED_BYTE, textureData)
    return texture


def gen_two_textures(arr, surface):
    glGenTextures(2, arr)
    arr[0] = load_bmp_texture("2x2.bmp")
    arr[1] = gen_rgba_texture(surface)


def gen_rgba_texture(textureSurface):
    textureData = pygame.image.tostring(textureSurface, "RGBA", True)

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, textureSurface.get_width(), textureSurface.get_height(),
                      GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def image_preprocess(img):
    textureSurface = pygame.image.load(img).convert_alpha()
    width = textureSurface.get_width()
    height = textureSurface.get_height()


    for x in range(width):
        for y in range(height):
            px = textureSurface.get_at((x, y))
            if px == (255, 255, 255, 255):
                textureSurface.set_at((x, y), (0, 0, 0, 0))
                continue
            textureSurface.set_at((x, y), (255 - px.r, 255 - px.g, 255 - px.b, px.a))
    return textureSurface


if __name__ == '__main__':
    tex_array = [0, 0]

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
    surface = image_preprocess("spider.bmp")

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
        gen_two_textures(tex_array, surface)
        # Texture modification
        glMatrixMode(GL_TEXTURE)
        glLoadIdentity()
        glScale(mult, mult, mult)
        glMatrixMode(GL_MODELVIEW)

        glRotate(abs(x or y), x, y, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_3d(tex_array)
        # ----------------
        pg.display.flip()
        pg.time.wait(10)
