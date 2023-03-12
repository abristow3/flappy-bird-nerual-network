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

        if pipe_type == PIPE_UPPER:
            y = y - self.rect.height

        self.set_position(x, y)

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

    def update(self, dt):
        if self.state == PIPE_MOVING:
            self.move_position(-(PIPE_SPEED * dt), 0)
            self.draw()


class PipeCollection:
    def __init__(self, game_display):
        self.game_display = game_display
        self.pipes = []

    def add_new_pipe_pair(self, x):
        top_y = random.randint(PIPE_MIN, PIPE_MAX - PIPE_GAP_SIZE)
        bottom_y = top_y + PIPE_GAP_SIZE

        p1 = Pipe(self.game_display, x, top_y, PIPE_UPPER)
        p2 = Pipe(self.game_display, x, bottom_y, PIPE_LOWER)

        self.pipes.append(p1)
        self.pipes.append(p2)

    def create_new_set(self):
        self.pipes = []
        placed = PIPE_FIRST

        while placed < DISPLAY_W:
            self.add_new_pipe_pair(placed)
            placed += PIPE_ADD_GAP

    def update(self, dt):
        rightmost = 0

        for pipe in self.pipes:
            pipe.update(dt)

            if pipe.pipe_type == PIPE_UPPER:
                if pipe.rect.left > rightmost:
                    rightmost = pipe.rect.left

        if rightmost < (DISPLAY_W - PIPE_ADD_GAP):
            self.add_new_pipe_pair(DISPLAY_W)

        self.pipes = [pipe for pipe in self.pipes if pipe.state == PIPE_MOVING]
