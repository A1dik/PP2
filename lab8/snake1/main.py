from os import scandir
from select import select
from random import choice
import time
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
SCORE = 0
BLOCK_SIZE = 20
collision = False


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []

        f = open(r"levels\lvl{}.txt".format(level), "r")

        # lines = content.split('\n')
        # print(len(lines[0]))

        for y in range(0, HEIGHT // BLOCK_SIZE + 1):
            for x in range(0, WIDTH // BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226, 135, 67), rect)


class Food:
    def __init__(self, wall):
        self.location = Point(choice([i for i in range(1, 19) if i != 10 and i not in wall.body]),
                              choice([i for i in range(1, 19) if i != 11 and i not in wall.body]))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0

        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE

        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)

    def check_collision(self, food):
        global SCORE
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                SCORE += 1
                food.location.x = choice([i for i in range(1, 19) if i not in self.body])
                food.location.y = choice([i for i in range(1, 19) if i not in self.body])

    def check_wall(self, wall):
        pass
        global collision
        for point in wall.body:
            if self.body[0].x == point.x:
                if self.body[0].y == point.y:
                    collision = True

        # if self.body[0].x == wall.body.x:
        #   if self.body[0].y == food.location.y:


def main():
    global SCREEN, CLOCK, collision
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    FPS = 5
    score_font = pygame.font.SysFont("Verdana", 20)
    snake = Snake()
    wall = Wall(snake.level)
    food = Food(wall)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1

        if len(snake.body) == 5:
            snake.level = 2
            wall = Wall(snake.level)
            FPS = 6
        elif len(snake.body) == 10:
            snake.level = 3
            wall = Wall(snake.level)
            FPS = 7
        '''
        for x in wall.body:
            if (snake.body[0].x, snake.body[0].y)== x:
                time.sleep(1)
                pygame.quit()
        '''
        snake.check_wall(wall)
        if collision:
            time.sleep(0.1)
            pygame.quit()
            break

        snake.move()
        snake.check_collision(food)

        SCREEN.fill(BLACK)

        food.draw()
        wall.draw()
        snake.draw()
        drawGrid()

        level_img = score_font.render(str(snake.level), True, WHITE)
        SCREEN.blit(level_img, (10, 35))
        score_img = score_font.render(str(SCORE), True, WHITE)
        SCREEN.blit(score_img, (10, 10))

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()