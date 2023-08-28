import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pyrr

# Inicializar pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (width / height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0, -5, -30)

# Variables para el control de la rotación
rotating = False
start_rotation = (0, 0)
rotation = [0, 0]

def draw_church():
    # Base de la iglesia
        glColor3f(0.5, 0.5, 0.5)
        glBegin(GL_QUADS)
        glVertex3f(-5, -5, 5)
        glVertex3f(5, -5, 5)
        glVertex3f(5, -5, -5)
        glVertex3f(-5, -5, -5)
        glEnd()

        # Pared frontal (color blanco)
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(-3, -5, 5)
        glVertex3f(3, -5, 5)
        glVertex3f(3, 5, 5)
        glVertex3f(-3, 5, 5)
        glEnd()

        # Torre (color gris claro)
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_QUADS)
        glVertex3f(-1, -5, 7)
        glVertex3f(1, -5, 7)
        glVertex3f(1, 5, 7)
        glVertex3f(-1, 5, 7)
        glEnd()

        # Techo (color beige)
        glColor3f(0.8, 0.8, 0.6)
        glBegin(GL_TRIANGLES)
        glVertex3f(-3, 5, 5)
        glVertex3f(3, 5, 5)
        glVertex3f(0, 10, 5)
        glEnd()
            
def handle_mouse_input(event):
    global rotating, start_rotation

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            rotating = True
            start_rotation = event.pos

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            rotating = False

    if event.type == pygame.MOUSEMOTION and rotating:
        rotation[0] += (event.pos[0] - start_rotation[0]) * 0.1
        rotation[1] += (event.pos[1] - start_rotation[1]) * 0.1
        start_rotation = event.pos
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            handle_mouse_input(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rotation[1], 1, 0, 0)
        glRotatef(rotation[0], 0, 1, 0)
        draw_church()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()