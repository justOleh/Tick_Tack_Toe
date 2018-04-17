import pygame
from settings import *

def main ():

    pygame.init()

    pygame.display.set_caption("Tick_Tack_Toe")

    screen = pygame.display.set_mode(SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen.fill(BACKGROUND_COLOR)

        #background = pygame.sprite.Sprite()
        background_image = pygame.image.load(BACKGROUND_PATH)
        background_rect = background_image.get_rect()
        background_rect.centerx = WIDTH // 2


        icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(icon)


        screen.blit(background_image,background_rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()