import pygame
import random
from functions import *


class Bird:

    def __init__(self, game_display):
        self.game_display = game_display
        self.state = BIRD_ALIVE
        self.img = pygame.image.load(BIRD_FILENAME)
        self.rect = self.img.get_rect()
        self.speed = 0
        self.time_lived = 0
        self.set_position(BIRD_START_X, BIRD_START_Y)

    def set_position(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def move(self, dt):

        distance = (self.speed * dt) + (0.5 * GRAVITY * dt * dt)
        new_speed = self.speed + (GRAVITY * dt)

        self.rect.centery += distance
        self.speed = new_speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0

    def jump(self):
        self.speed = BIRD_START_SPEED
        print("Jump!")

    def draw(self):
        self.game_display.blit(self.img, self.rect)

    def check_status(self):
        if self.rect.bottom > DISPLAY_H:
            self.state = BIRD_DEAD
            print("Dead Dimple")

    def update(self, dt):
        if self.state == BIRD_ALIVE:
            self.time_lived += dt
            self.move(dt)
            self.draw()
            self.check_status()
