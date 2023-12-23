import pygame
import numpy as np
import graphics as g


def main():
    window = g.Drawer(800, 600, 64)
    window.initialize("ManySquares")
    window.draw_text(-20, 7 * 65 + 5, "O", 36, (255, 255, 255), 100)
    window.draw_axes(0, 8 * 65, 0, 7 * 65, 3, (255, 255, 255), 100)
    L = np.array([[2, 0.5], [8, 0.5], [8, 6.5], [2, 6.5]])
    window.draw_line(L, 3, (255, 255, 255), 100)
    p = 0.95
    q = 1 - p
    Lo = np.copy(L)
    for i in range(50):
        Lo[0][0] = p * Lo[0][0] + q * Lo[1][0]
        Lo[0][1] = p * Lo[0][1] + q * Lo[1][1]
        Lo[1][0] = p * Lo[1][0] + q * Lo[2][0]
        Lo[1][1] = p * Lo[1][1] + q * Lo[2][1]
        Lo[2][0] = p * Lo[2][0] + q * Lo[3][0]
        Lo[2][1] = p * Lo[2][1] + q * Lo[3][1]
        Lo[3][0] = p * Lo[3][0] + q * Lo[0][0]
        Lo[3][1] = p * Lo[3][1] + q * Lo[0][1]
        window.draw_line(Lo, 3, (255, 0, 0), 100)


if __name__ == '__main__':
    main()

    FPS = 30
    clock = pygame.time.Clock()
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
                pygame.quit()
            clock.tick(FPS)
            pygame.display.update()
