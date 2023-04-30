import os
import psycopg2
import pygame
import random
import sys

from config import config

params = config()
pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
font1 = pygame.font.Font(None, 32)
text1 = font1.render("Score", True, (0, 0, 255))
text2 = font1.render("Level", True, (0, 0, 255))
score = 0
head1 = 0
head2 = 0
chfps = 5
FPS = 4
Over = False
Victory = False


def Save(highscore, level, name):
    cur.execute("UPDATE Snake SET score = %s, level = %s WHERE name = %s", (highscore, level, name))
    conn.commit()


class Scene:
    def __init__(self):
        self.done = False

    def draw(self, screen, scenetext1, scenetext2, clock):
        self.done = False
        global highscore, level, name
        Save(highscore, level, name)
        while not self.done:
            screen.fill((0, 0, 0))
            screen.blit(scenetext1, (250 - scenetext1.get_width() // 2, 150 - scenetext1.get_height() // 2))
            screen.blit(scenetext2, (250 - scenetext2.get_width() // 2, 250 - scenetext2.get_height() // 2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cur.close()
                    conn.close()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.done = True
            pygame.display.update()
            clock.tick(10)


class Snake:
    def __init__(self):
        self.body = []
        self.dx = 0
        self.dy = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global highscore, level, name
                Save(highscore, level, name)
                cur.close()
                conn.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.body[1][1] != self.body[0][1] - 1:
                    self.dy = -1
                    self.dx = 0
                if event.key == pygame.K_DOWN and self.body[1][1] != self.body[0][1] + 1:
                    self.dy = 1
                    self.dx = 0
                if event.key == pygame.K_RIGHT and self.body[1][0] != self.body[0][0] + 1:
                    self.dx = 1
                    self.dy = 0
                if event.key == pygame.K_LEFT and self.body[1][0] != self.body[0][0] - 1:
                    self.dx = -1
                    self.dy = 0
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        if self.body[0][0] == -1:
            self.body[0][0] = 19
        if self.body[0][0] == 20:
            self.body[0][0] = 0
        if self.body[0][1] == -1:
            self.body[0][1] = 19
        if self.body[0][1] == 20:
            self.body[0][1] = 0

    def draw(self, screen):
        i, u = self.body[0]
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(i * 20, u * 20, 20, 20))
        for q in self.body[1:]:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(q[0] * 20, q[1] * 20, 20, 20))

    def new(self, x, y):
        self.body = [[x, y], [x + 1, y], [x + 2, y]]
        self.dx = -1
        self.dy = 0


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x * 20, self.y * 20, 20, 20))

    def new(self, S, W):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        q = [self.x, self.y]
        while q in S.body or q in W.body:
            self.x = random.randint(0, 19)
            self.y = random.randint(0, 19)
            q = [self.x, self.y]


class Wall:
    def __init__(self):
        self.body = []

    def draw(self, screen):
        for x in range(len(self.body)):
            pygame.draw.rect(screen, (165, 42, 42), pygame.Rect(self.body[x][0] * 20, self.body[x][1] * 20, 20, 20))

    def new(self, level):
        self.body = []
        text = r"levels\{}.txt".format(level)
        if os.path.exists(text):
            f = open(text, "r")
            i = 0
            u = 0
            line = f.readline()
            while line != None and i < 20:
                for x in line:
                    if x == "#":
                        self.body.append([u, i])
                    elif x == "$":
                        global head1, head2
                        head1 = u
                        head2 = i
                    u += 1
                    if u == 20:
                        break
                i += 1
                u = 0
                line = f.readline()
        else:
            global Victory
            Victory = True


def Grid(screen):
    for x in range(0, 400, 20):
        for y in range(0, 400, 20):
            pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(x, y, 20, 20), 1)


conn = psycopg2.connect(**params)
cur = conn.cursor()
name = input("Enter your name\n")
cur.execute("SELECT count(*) FROM Snake WHERE name = %s", (name,))
if cur.fetchone()[0] == 0:
    cur.execute("INSERT INTO Snake(name, score, level) VALUES(%s,%s,%s)", (name, 0, 1))
    conn.commit()
    highscore = 0
    level = 1
else:
    cur.execute("SELECT score FROM Snake WHERE name = %s", (name,))
    highscore = cur.fetchone()[0]
    cur.execute("SELECT level FROM Snake WHERE name = %s", (name,))
    level = cur.fetchone()[0]
totalscore = (highscore // 15) * 15
scenetext1 = font.render("Welcome, " + name, True, (147, 250, 165))
scenetext2 = font.render("Highscore - " + str(highscore) + "; Level - " + str(level), True, (147, 250, 165))
W = Wall()
W.new(level)
S = Snake()
S.new(head1, head2)
F = Food()
F.new(S, W)
Sc = Scene()
Sc.draw(screen, scenetext1, scenetext2, clock)
while True:
    screen.fill((0, 0, 0))
    Grid(screen)
    S.move()
    S.draw(screen)
    if S.body[0][0] == F.x and S.body[0][1] == F.y:
        score += 1
        totalscore += 1
        if totalscore > highscore:
            highscore = totalscore
        F.new(S, W)
        S.body.append([F.x, F.y])
    for i in range(1, len(S.body)):
        if S.body[0][0] == S.body[i][0] and S.body[0][1] == S.body[i][1]:
            Over = True
    for i in range(len(W.body)):
        if S.body[0][0] == W.body[i][0] and S.body[0][1] == W.body[i][1]:
            Over = True
    if Over:
        scenetext1 = font.render("Game Over, " + name, True, (136, 8, 8))
        scenetext2 = font.render("Highscore - " + str(highscore) + "; Level - " + str(level), True, (136, 8, 8))
        Sc.draw(screen, scenetext1, scenetext2, clock)
        cur.close()
        conn.close()
        pygame.quit()
        sys.exit()
    F.draw(screen)
    W.draw(screen)
    if score == chfps:
        FPS += 2
        chfps += 5
    Score = font.render(str(score), True, (0, 0, 255))
    Level = font.render(str(level), True, (0, 0, 255))
    screen.blit(Score, (450 - Score.get_width() // 2, 130 - Score.get_height() // 2))
    screen.blit(Level, (450 - Level.get_width() // 2, 330 - Level.get_height() // 2))
    screen.blit(text1, (450 - text1.get_width() // 2, 50 - text1.get_height() // 2))
    screen.blit(text2, (450 - text2.get_width() // 2, 250 - text2.get_height() // 2))
    pygame.display.update()
    if score == 15:
        score = 0
        FPS = 4
        chfps = 5
        level += 1
        W.new(level)
        if Victory:
            level = 1
            scenetext1 = font.render("Congratulations, " + name, True, (255, 215, 0))
            scenetext2 = font.render("Victory", True, (255, 215, 0))
            Sc.draw(screen, scenetext1, scenetext2, clock)
            cur.close()
            conn.close()
            pygame.quit()
            sys.exit()
        S.new(head1, head2)
        F.new(S, W)
        scenetext1 = font.render("Good job, " + name, True, (207, 181, 59))
        scenetext2 = font.render("Highscore - " + str(highscore) + "; Level - " + str(level), True, (207, 181, 59))
        Sc.draw(screen, scenetext1, scenetext2, clock)
    clock.tick(FPS)
