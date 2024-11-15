import pygame
import sys
import modules.buttons as menu_tc
import subprocess


pygame.init()

WIDTH = 900
HEIGHT = 700

# Музика
pygame.mixer.init()
pygame.mixer.music.load('music/Miper - relax.mp3')
pygame.mixer.music.play(-1)  # Циклічне відтворення музики

music_playing = True  # Флаг, що музика грає

window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(pygame.image.load("images/cf.png"), (WIDTH, HEIGHT))

window.fill((92, 92, 92))

clock = pygame.time.Clock()

FPS = 60

game = True


def run_game():
    global game
    while game:

        window.blit(background, (0, 0))
        menu_tc.start_button.reset() 
        menu_tc.setting_button.reset()
        menu_tc.aftors_button.reset() 
        menu_tc.exit_button.reset()
        menu_tc.mario_button.reset()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if menu_tc.start_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'mario.py'])

                if menu_tc.setting_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'setting.py'])
                    # process.wait()

                if menu_tc.aftors_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'developed.py'])

                if menu_tc.exit_button.collidepoint(x, y):
                    game = False      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    if music_playing:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)  # Циклічне відтворення музики
                    music_playing = not music_playing  # Перемикаємо стан музики

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    run_game()

