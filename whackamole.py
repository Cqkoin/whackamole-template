import pygame, random


def main():
    mole_x = 2
    mole_y = 2
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # When the user clicks on the mole's square,
                # it should move to a different random square.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mouse_col = mouse_x // 32
                    mouse_row = mouse_y // 32
                    mole_col = mole_x // 32
                    mole_row = mole_y // 32
                    if mouse_row == mole_row and mouse_col == mole_col:
                        mole_row = random.randrange(0, 16)
                        mole_col = random.randrange(0, 20)
                        mole_x = mole_col * 32
                        mole_y = mole_row * 32
            screen.fill("light green") # screen is light green

            # The window should be divided into a 20x16 grid of 32x32 squares
            # draw lines horizontally
            for i in range(16):
                pygame.draw.line(screen, "purple", (0, (i * 32)), (640, (i * 32)))
            # draw lines vertically
            for i in range(20):
                pygame.draw.line(screen, "purple", ((i * 32), 0), ((i * 32), 640))

            # draw mole in top left (mole_x =0, mole_y = 0)
            screen.blit(mole_image, mole_image.get_rect(topleft=(2 + mole_x, 2 + mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

