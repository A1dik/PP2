import os
import pygame


def stop_play_a_song():
    global _is_music_playing

    pygame.mixer.music.stop()
    _is_music_playing = False


def play_a_song():
    global _is_music_playing

    _is_music_playing = True
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


def turn_previous_song():
    global _songs, _is_music_playing

    _songs = [_songs[-1]] + _songs[:-1]

    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    _is_music_playing = True


def turn_next_song():
    global _songs, _is_music_playing

    _songs = _songs[1:] + [_songs[0]]

    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    _is_music_playing = True


MUSIC_DIR = os.path.join(os.getcwd() + '\\music')
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

_songs = []

_is_music_playing = False

for item in os.listdir(MUSIC_DIR):
    target_path = os.path.join(MUSIC_DIR, item)
    # print(target_path)
    if os.path.isfile(target_path):
        if '.mp3' in item:
            _songs.append(target_path)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.37)

screen = pygame.display.set_mode((960, 240))

font1 = pygame.font.SysFont('Verdana', 23, True)
font2 = pygame.font.SysFont('Verdana', 20)
font3 = pygame.font.SysFont('Verdana', 15)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                turn_next_song()
            elif event.key == pygame.K_UP:
                turn_previous_song()
            elif event.key == pygame.K_p:
                if _is_music_playing:
                    print('Music is playing')
                else:
                    play_a_song()
            elif event.key == pygame.K_s:
                if _is_music_playing:
                    stop_play_a_song()
                else:
                    print('No music is playing')

    screen.fill(pygame.Color('White'))

    pygame.draw.rect(screen, pygame.Color('pink'), (0,0,960,115), 2)

    screen.blit(font3.render(os.path.basename(_songs[-1]), True, pygame.Color('indigo')), (172, 15))
    screen.blit(font1.render(os.path.basename(_songs[0]), True, pygame.Color('magenta')), (170, 40))
    screen.blit(font3.render(os.path.basename(_songs[1]), True, pygame.Color('indigo')), (172, 70))

    screen.blit(font2.render('Current song:', True, pygame.Color('orange')), (16, 40))

    screen.blit(font3.render(
        'Press [s] to stop playing the music' if _is_music_playing
        else 'Press [p] to start play the music', True, pygame.Color('black')), (16, 125))

    screen.blit(font3.render('Press [arrow_up] to turn the previous song', True, pygame.Color('black')), (16, 145))
    screen.blit(font3.render('Press [arrow_down] to turn the next song', True, pygame.Color('black')), (16, 165))

    screen.blit(font1.render('U\'Pygame music player. v.2.0.1', True, pygame.Color('Indigo')), (16, 200))
    pygame.display.flip()

