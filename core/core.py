# coding: utf-8

import os
import pygame

def main():
    bg1_x = 0
    bg1_y = 0
    bg1_x_speed = 10
    bg2_x = 1000
    bg2_y = 0
    bg2_x_speed = 10

    screen = pygame.display.set_mode((1000, 500))

    screen.fill((255, 255, 255))

    bg1 = pygame.image.load(r"lib\pictures\background_one.png")

    bg2 = pygame.image.load(r"lib\pictures\background_two.png")
    refer = pygame.image.load(r"lib\pictures\refer.png")

    # screen.blit(bg1, (bg1_x, bg1_y))
    screen.blit(bg2, (1000, bg2_y))

    pygame.display.flip()
    running = True

    while running:
        screen.blit(refer, (100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # bg1
        bg1_x -= bg1_x_speed
        pygame.draw.rect(screen, [255, 255, 255],
                         [bg1_x + bg1_x_speed, bg1_y, 1000, 500], 0)
        screen.blit(bg1, (bg1_x, bg1_y))

        # bg2
        bg2_x -= bg2_x_speed
        pygame.draw.rect(screen, [255, 255, 255],
                         [bg2_x + bg2_x_speed, bg2_y, 1000, 500], 0)
        screen.blit(bg2, (bg2_x, bg2_y))


        pygame.display.flip()

        if bg1_x == -1000:
            bg1_x = 1000
            screen.blit(bg1, (bg1_x, 0))
            pygame.display.flip()
        elif bg2_x == -1000:
            bg2_x = 1000
            screen.blit(bg2, (bg2_x, 0))
            pygame.display.flip()

        pygame.time.delay(100)


    pygame.quit()


if __name__ == '__main__':
    main()

