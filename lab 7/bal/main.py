import pygame

# initialize Pygame
pygame.init()

# define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# set screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# set ball properties
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_radius = 25
ball_color = RED

# set screen properties
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Game")

# set clock
clock = pygame.time.Clock()


# define function to keep ball within screen
def keep_ball_in_screen(pos):
    if pos[0] < ball_radius:
        pos[0] = ball_radius
    if pos[0] > SCREEN_WIDTH - ball_radius:
        pos[0] = SCREEN_WIDTH - ball_radius
    if pos[1] < ball_radius:
        pos[1] = ball_radius
    if pos[1] > SCREEN_HEIGHT - ball_radius:
        pos[1] = SCREEN_HEIGHT - ball_radius


# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # move ball with arrow keys
            if event.key == pygame.K_UP:
                ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += 20

    # update ball position and keep it within screen
    keep_ball_in_screen(ball_pos)

    # draw screen and ball
    screen.fill(WHITE)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # update screen
    pygame.display.flip()

    # set frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()
