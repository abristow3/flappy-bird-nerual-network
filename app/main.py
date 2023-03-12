from functions import *
import pygame
from pipe import PipeCollection
from bird import BirdCollection


def update_label(data, title, font, x, y, game_display):
    label = font.render(f"{title} {data}", 1, DATA_FONT_COLOR)
    game_display.blit(label, (x, y))
    return y


def update_data_labels(game_display, dt, game_time, num_iterations, num_alive, most_generations, least_generations,
                       font):
    y_pos = 10
    gap = 20
    x_pos = 10
    y_pos = update_label(round(1000 / dt, 2), "FPS", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(round(game_time / 1000, 2), "Game Time", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(num_iterations, "Iteration", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(num_alive, "Alive", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(most_generations, "Most Gens", font, x_pos, y_pos + gap, game_display)
    y_pos = update_label(least_generations, "Least Gens", font, x_pos, y_pos + gap, game_display)


def run_game():
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption("AI Learn To Fly")

    running = True

    # Set background image
    background_image = pygame.image.load(BG_FILENAME)
    pipes = PipeCollection(game_display)
    pipes.create_new_set()

    birds = BirdCollection(game_display)

    # Set font style
    label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)

    clock = pygame.time.Clock()
    dt = 0
    game_time = 0
    num_iterations = 1
    most_generations = 0
    least_generations = 0

    while running:
        # Setup 30 frames per second
        dt = clock.tick(FPS)
        game_time += dt

        # load image and specify where to draw it, (0,0) is top left
        game_display.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

        pipes.update(dt)
        num_alive = birds.update(dt, pipes.pipes)

        if num_alive == 0:
            pipes.create_new_set()
            game_time = 0
            birds.evolve_population()
            num_iterations += 1

        if game_time > 150000:
            if most_generations == 0 and least_generations == 0:
                most_generations = num_iterations
                least_generations = num_iterations
            elif num_iterations > most_generations:
                most_generations = num_iterations
            elif num_iterations < least_generations:
                least_generations = num_iterations

            pipes.create_new_set()
            game_time = 0
            num_iterations = 0
            birds.create_new_generation()

        update_data_labels(game_display, dt, game_time, num_iterations, num_alive, most_generations, least_generations,
                           label_font)
        pygame.display.update()


if __name__ == "__main__":
    run_game()
