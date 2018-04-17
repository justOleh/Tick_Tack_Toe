import pygame
from settings import *
from game_objects import *

def main ():

    pygame.init()

    pygame.display.set_caption("Tick_Tack_Toe")

    screen = pygame.display.set_mode(SIZE)


    #game objects
    background = Background()


    #groups
    all_objects = pygame.sprite.Group()

    #adding objects to groups
    all_objects.add(background)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen.fill(BACKGROUND_COLOR)



        icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(icon)


        all_objects.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()