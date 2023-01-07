from functions import *
import pygame
from pipe import Pipe


def update_label(data, title, font, x, y, game_display):
    label = font.render(f"{title} {data}", 1, DATA_FONT_COLOR)
    game_display.blit(label, (x, y))
    return y


def update_data_labels(game_display, dt, game_time, font):
    y_pos = 10
    gap = 20
    x_pos = 10
    y_pos = update_label(round(1000 / dt, 2), "FPS", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(round(game_time / 1000, 2), "Game Time", font, x_pos, y_pos + gap, game_display)


def run_game():
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption("AI Learn To Fly")

    running = True

    # Set background image
    background_image = pygame.image.load(BG_FILENAME)

    # Set font style
    label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)

    clock = pygame.time.Clock()
    dt = 0
    game_time = 0

    pipe = Pipe(game_display, DISPLAY_W, 300, PIPE_LOWER)

    while running:
        # Setup 30 frames per second
        dt = clock.tick(FPS)
        game_time += dt

        # load image and specify where to draw it, (0,0) is top left
        game_display.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

        update_data_labels(game_display, dt, game_time, label_font)
        pipe.update(dt)
        pygame.display.update()


if __name__ == "__main__":
    run_game()
