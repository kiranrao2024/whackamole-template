import pygame, random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_pos_x, mole_pos_y = 0, 0
        running = True
        began = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0] // 32
                    posy = event.pos[1] // 32

                    if posx == mole_pos_x and posy == mole_pos_y:
                        mole_pos_x, mole_pos_y = set_position()
                        began = True

            screen.fill("light green")

            if not began:
                screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            else:
                screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos_x * 32, mole_pos_y * 32)))

            draw_board(screen)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

def draw_board(screen):
    # draw rows
    for row in range(0, 20):
        pygame.draw.line(screen, (0, 0, 0), (0, row * 32), (640, row * 32))

    # draw columns
    for col in range(0, 20):
        pygame.draw.line(screen, (0, 0, 0), (col * 32, 0), (col * 32, 512))

def set_position():
    x = random.randrange(0, 20)
    y = random.randrange(0, 16)

    return x, y

if __name__ == "__main__":
    main()