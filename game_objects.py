import pygame
import minimax as algorithm
from settings import *


class Dagger(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Dagger,self).__init__()

        self.image = pygame.image.load(DAGGER_PATH)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class Circle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Circle,self).__init__()

        self.image = pygame.image.load(CIRCLE_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load(BACKGROUND_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

class Win(pygame.sprite.Sprite):

    dx = 10
    dy = 10

    def __init__(self):
        super(Win, self).__init__()

        self.image = pygame.image.load(WIN_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIDTH:
            self.dx = - self.dx
        if self.rect.y <= 0 or self.rect.y >= HEIGHT:
            self.dy = - self.dy

        self.rect.x = self.rect.x + self.dx

        self.rect.sy = self.rect.y + self.dy




class Lose(pygame.sprite.Sprite):

    dx = 10
    dy = 10

    def __init__(self):
        super(Lose, self).__init__()

        self.image = pygame.image.load(LOSE_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIDTH:
            self.dx = - self.dx
        if self.rect.y <= 0 or self.rect.y >= HEIGHT:
            self.dy = - self.dy

        self.rect.x = self.rect.x + self.dx

        self.rect.y = self.rect.y + self.dy

class Tie(pygame.sprite.Sprite):

    dx = 10
    dy = 10

    def __init__(self):
        super(Tie, self).__init__()

        self.image = pygame.image.load(TIE_PATH)

        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIDTH:
            self.dx = - self.dx
        if self.rect.y <= 0 or self.rect.y >= HEIGHT:
            self.dy = - self.dy

        self.rect.centerx = self.rect.centerx + self.dx

        self.rect.centery = self.rect.centery + self.dy


class GameState():

    win = Win()

    lose = Lose()

    tie = Tie()

    drawed = [False, False, False, False, False, False, False, False, False]

    huPlayer = "X"

    aiPlayer = "O"

    objects = pygame.sprite.Group()

    indexes = [[scale//2, scale//2],[scale + scale // 2, scale // 2],[2*scale + scale // 2, scale // 2],
               [scale // 2,scale + scale // 2],[scale + scale // 2,scale + scale // 2],[2*scale + scale // 2,scale + scale // 2],
               [scale // 2,2*scale + scale // 2],[scale + scale // 2,2*scale + scale // 2],[2*scale + scale // 2,2*scale + scale // 2]]

    def __init__(self,dagger_turn = True):
        self.dagger_turn = dagger_turn

        self.places = [x for x in range(9)]

    def update(self):



        if algorithm.winning(self.places,self.huPlayer):
            temp = list(self.objects)
            if self.win in temp:
                self.win.update()
            else:
                self.objects.add(self.win)
            print("win hum")

        elif algorithm.winning(self.places,self.aiPlayer):
            temp = list(self.objects)
            if self.lose in temp:
                self.lose.update()
            else:
                self.objects.add(self.lose)
            print("win ai")

        elif len(algorithm.emptyIndexies(self.places)) == 0:
            temp = list(self.objects)
            if self.tie in temp:
                self.tie.update()
            else:
                self.objects.add(self.tie)
            print("tie")

        if self.lose in list(self.objects) or self.win in list(self.objects) or self.tie in list(self.objects):
            return


        if not self.dagger_turn:
            self.places[algorithm.minimax(self.places,self.aiPlayer)["index"]] = self.aiPlayer
            self.dagger_turn = True


        keys = pygame.mouse.get_pressed()

        if (keys[0]):
            #point = dict()
            if self.dagger_turn:
                mouse_pos = pygame.mouse.get_pos()

                print("left pos:", mouse_pos)


                if mouse_pos[0] <= scale and mouse_pos[1] <= scale:
                   if isinstance(self.places[0],int):
                       self.places[0] = self.huPlayer

                       self.dagger_turn = False

                if (scale < mouse_pos[0] < 2*scale and mouse_pos[1] <= scale):
                    if isinstance(self.places[1], int):
                        self.places[1] = self.huPlayer

                        self.dagger_turn = False

                if (2*scale < mouse_pos[0] < 3*scale  and mouse_pos[1] <= scale):
                        if isinstance(self.places[2], int):
                            self.places[2] = self.huPlayer

                            self.dagger_turn = False

                 #second row

                if (mouse_pos[0] < scale) and (scale < mouse_pos[1] < 2*scale):
                    if isinstance(self.places[3], int):
                        self.places[3] = self.huPlayer

                        self.dagger_turn = False

                if (scale < mouse_pos[0] < 2*scale) and (scale < mouse_pos[1] < 2*scale):
                    if isinstance(self.places[4], int):
                        self.places[4] = self.huPlayer

                        self.dagger_turn = False

                if (2*scale < mouse_pos[0] and scale < mouse_pos[1] < 2*scale):
                     if isinstance(self.places[5], int):
                         self.places[5] = self.huPlayer

                         self.dagger_turn = False

                # third row

                if (mouse_pos[0] < scale and 2*scale < mouse_pos[1]):
                    if isinstance(self.places[6], int):
                        self.places[6] = self.huPlayer

                        self.dagger_turn = False

                #
                if (scale < mouse_pos[0] < 2*scale) and ( 2*scale < mouse_pos[1]):
                    if isinstance(self.places[7], int):
                        self.places[7] = self.huPlayer

                        self.dagger_turn = False
                #
                if (2*scale < mouse_pos[0] and  2*scale < mouse_pos[1]):
                    if isinstance(self.places[8], int):
                        self.places[8] = self.huPlayer

                        self.dagger_turn = False




        if (keys[2]):

            if not self.dagger_turn:

                mouse_pos = pygame.mouse.get_pos()
                print("left pos:",mouse_pos)

                # first colum

                if mouse_pos[0] <= scale and mouse_pos[1] <= scale:
                    if isinstance(self.places[0], int):
                        self.places[0] = self.aiPlayer

                        self.dagger_turn = True

                if (scale < mouse_pos[0] < 2*scale and mouse_pos[1] <= scale):
                    if isinstance(self.places[1], int):
                        self.places[1] = self.aiPlayer

                        self.dagger_turn = True

                if (2*scale < mouse_pos[0] < 3*scale  and mouse_pos[1] <= scale):
                     if isinstance(self.places[2], int):
                         self.places[2] = self.aiPlayer

                         self.dagger_turn = True

                 #second row

                if (mouse_pos[0] < scale) and (scale < mouse_pos[1] < 2*scale):
                    if isinstance(self.places[3], int):
                        self.places[3] = self.aiPlayer

                        self.dagger_turn = True

                if (scale < mouse_pos[0] < 2*scale) and (scale < mouse_pos[1] < 2*scale):
                    if isinstance(self.places[4], int):
                        self.places[4] = self.aiPlayer

                        self.dagger_turn = True

                #
                if (2*scale < mouse_pos[0] and scale < mouse_pos[1] < 2*scale):
                    if isinstance(self.places[5], int):
                         self.places[5] = self.aiPlayer

                         self.dagger_turn = True

                # third row

                if (mouse_pos[0] < scale and 2*scale < mouse_pos[1]):
                    if isinstance(self.places[6], int):
                        self.places[6] = self.aiPlayer

                        self.dagger_turn = True

                if (scale < mouse_pos[0] < 2*scale) and ( 2*scale < mouse_pos[1]):
                    if isinstance(self.places[7], int):
                        self.places[7] = self.aiPlayer

                        self.dagger_turn = True


                if (2*scale < mouse_pos[0] and  2*scale < mouse_pos[1]):
                    if isinstance(self.places[8], int):
                        self.places[8] = self.aiPlayer

                        self.dagger_turn = True


    def draw_points(self):

        for i in range(len(self.places)):
            if self.places[i] == "X" and not self.drawed[i]:
                dagger = Dagger(self.indexes[i][0],self.indexes[i][1])
                self.objects.add(dagger)
                print("dagger")
                self.drawed[i] = True

            elif self.places[i] == "O" and not self.drawed[i]:
                circle = Circle(self.indexes[i][0], self.indexes[i][1])
                self.objects.add(circle)
                print("circle")
                self.drawed[i] = True

