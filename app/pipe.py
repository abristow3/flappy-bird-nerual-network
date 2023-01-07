import pygame
import random
from functions import *


class Pipe:

    def __init__(self, game_display, x, y, pipe_type):
        self.game_display = game_display
        self.state = PIPE_MOVING
        self.pipe_type = pipe_type
        self.img = pygame.image.load(PIPE_FILENAME)
        self.rect = self.img.get_rect()
        self.set_position(x, y)
        print("PIPE_MOVING")

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def move_position(self, dx, dy):
        self.rect.centerx += dx
        self.rect.centery += dy

    def draw(self):
        self.game_display.blit(self.img, self.rect)

    def check_status(self):
        if self.rect.right < 0:
            self.state = PIPE_DONE
            print("PIPE_DONE")

    def update(self, dt):
        if self.state == PIPE_MOVING:
            self.move_position(-(PIPE_SPEED * dt), 0)
            self.draw()
