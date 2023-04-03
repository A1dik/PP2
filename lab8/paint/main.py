from turtle import position
import math
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()
    R = (255, 0, 0)
    G = (0, 255, 0)
    B = (0, 0, 255)
    key_R = True
    key_G = False
    key_B = False

    prevX = 0
    prevY = 0

    currentX = -1
    currentY = -1

    screen.fill((0, 0, 0))

    isMouseDown = False
    rectan = True
    circle = False
    eraser = False
    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    rectan = True
                    circle = False
                    eraser = False
                if event.key == pygame.K_2:
                    rectan = False
                    circle = True
                    eraser = False
                if event.key == pygame.K_3:
                    rectan = False
                    circle = False
                    eraser = True
                if event.key == pygame.K_r:
                    key_R = True
                    key_G = False
                    key_B = False
                if event.key == pygame.K_g:
                    key_R = False
                    key_G = True
                    key_B = False
                if event.key == pygame.K_b:
                    key_R = False
                    key_G = False
                    key_B = True

        if eraser:
            if isMouseDown:  # eraser
                pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 10)

            prevX = currentX
            prevY = currentY
        elif isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
            screen.blit(baseLayer, (0, 0))

            if circle:  # circle
                radius = math.sqrt((abs(prevX - currentX)) ** 2 + (abs(prevY - currentY)) ** 2)
                if key_R:
                    pygame.draw.circle(screen, R, (min(prevX, currentX), min(prevY, currentY)), radius, 1)
                elif key_G:
                    pygame.draw.circle(screen, G, (min(prevX, currentX), min(prevY, currentY)), radius, 1)
                elif key_B:
                    pygame.draw.circle(screen, B, (min(prevX, currentX), min(prevY, currentY)), radius, 1)
            elif rectan:  # rectangle
                r = calculateRect(prevX, prevY, currentX, currentY)
                if key_R:
                    pygame.draw.rect(screen, R, pygame.Rect(r), 1)
                elif key_G:
                    pygame.draw.rect(screen, G, pygame.Rect(r), 1)
                elif key_B:
                    pygame.draw.rect(screen, B, pygame.Rect(r), 1)
        pygame.display.flip()
        clock.tick(60)


def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


main()
