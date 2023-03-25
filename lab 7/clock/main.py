import math
import os
import datetime

import pygame

_image_lib = {}


def get_image(path):
    global _image_lib
    image = _image_lib.get(path)
    if image is None:
        can_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(can_path)
        _image_lib[path] = image
    return image


size = width, height = 480, 360+20
center = (width//2, (height-20)//2)
pygame.init()
screen = pygame.display.set_mode(size)
done = False

clock = pygame.time.Clock()
fps = 1

im_min = get_image('seconds_arrow.png')
im_sec = get_image('minutes_arrow.png')

angle_for_minutes_arrow, angle_for_seconds_arrow = 0, 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((255, 255, 255))

    now = datetime.datetime.now()

    rot_min = pygame.transform.rotate(
        im_min,
        -6*now.minute+306
        # 0
                                      )
    dm = rot_min.get_rect(center=rot_min.get_rect(center=center).center)
    rot_sec = pygame.transform.rotate(im_sec, 0 -6*now.second+60 ) # 360 degree / 60 seconds
    ds = rot_sec.get_rect(center=rot_sec.get_rect(center=center).center)
    screen.blit(get_image('clock.jpg'), (0, 0))

    screen.blit(rot_min, dm)
    screen.blit(rot_sec, ds)

    font = pygame.font.SysFont("Verdana", 25)
    time_render = font.render(f'{now.__format__("%H:%M:%S")}', True, (0, 0, 255))
    pygame.draw.line(screen, (255,0,0), (0,337), (480, 337), 5)
    screen.blit(time_render, (190, 345))

    pygame.display.flip()
    clock.tick(fps)