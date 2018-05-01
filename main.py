import pygame
from settings import *

from game_objects import *

game_state = GameState()

def main ():

    pygame.init()

    pygame.display.set_caption("Tick_Tack_Toe")

    screen = pygame.display.set_mode(SIZE)

    #game objects
    background = Background()

    game_state.objects.add(background)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen.fill(BACKGROUND_COLOR)

        icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(icon)


        game_state.update()

        game_state.draw_points()

        game_state.objects.draw(screen)

        pygame.display.flip()

        pygame.time.wait(25)


if __name__ == "__main__":
    main()