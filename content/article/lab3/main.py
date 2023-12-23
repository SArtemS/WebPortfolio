import numpy as np
import pygame as pg
import math
from pprint import pprint as pp
import sys
from pygame.locals import *

# Переменные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализируем игровую библиотеку, игровое окно и один из шрифтов для надписей в окне
pg.init()
pg.font.init()
window = pg.display.set_mode((0, 0), FULLSCREEN)
window.fill((255, 255, 255))
my_game_font = pg.font.SysFont('Fira Code', 40)
pg.display.update()


def main():
    diag = 500
    menu(diag)
    FPS = 30
    clock = pg.time.Clock()
    while True:
        pressed_keys = pg.key.get_pressed()
        for event in pg.event.get():
            if (event.type == QUIT) or (pressed_keys[K_ESCAPE]):
                pg.quit()
                sys.exit()
            if pressed_keys[K_1]:
                window.fill(WHITE)
                lab3_1(diag)
            if pressed_keys[K_2]:
                window.fill(WHITE)
                lab3_2(diag)
            if pressed_keys[K_0]:
                window.fill(WHITE)
                menu(diag)
            if pressed_keys[K_UP]:
                diag += 50
                window.fill(WHITE)
                menu(diag)
            if pressed_keys[K_DOWN]:
                diag -= 50
                window.fill(WHITE)
                menu(diag)
        clock.tick(FPS)
        pg.display.update()


# "Главное меню"
def menu(d):
    window.blit(my_game_font.render("'1-2' - выбор задания", True, BLACK),
                (5, 5))
    window.blit(my_game_font.render("'0' - возвращение в меню", True, BLACK),
                (5, 45))
    window.blit(
        my_game_font.render("'UP', 'DOWN' - изменить смещение по осям x, y",
                            True, BLACK), (5, 85))
    window.blit(
        my_game_font.render("'Escape' - выход из программы", True, BLACK),
        (5, 125))
    window.blit(
        my_game_font.render(f"Оси x и y смещаются на {d}", True, BLACK),
        (5, 165))
    pg.display.update()


# Самостоятельная работа 1
def lab3_1(d):
    m = 0.9
    n = 20
    a = math.pi / 32
    X = np.array([[2, -2, -2, 2], [2, 2, -2, -2]]) * 100 + d
    M = np.array([[m, 0], [0, m]])
    V = ([[math.cos(a), -math.sin(a)], [-math.sin(a), math.cos(a)]])
    print("X:")
    mat_out(X)
    print("M:")
    mat_out(M)
    print("V:")
    mat_out(V)
    pg.draw.lines(window, BLUE, True, X.transpose(), 3)
    Xtransform = np.copy(X)
    for i in range(1, n + 1):
        Xtransform = V @ M @ Xtransform
        mat_out(Xtransform)
        pg.draw.lines(window, RED, True, Xtransform.transpose(), 3)
    pg.display.update()


# Самостоятельная работа 2
def lab3_2(d):
    a = 210
    b = 180
    h = 1
    O = 0
    r = b + 2 * a * math.cos(O)
    x = r * math.cos(O)
    y = r * math.sin(O)
    snail = np.array([[x, y]])
    O += h
    while O <= 360:
        r = b + 2 * a * math.cos(O)
        x = r * math.cos(O)
        y = r * math.sin(O)
        snail = np.append(snail, [[x, y]], axis=0)
        O += h
    print(snail)
    pg.draw.lines(window, GREEN, False, snail + d, 3)
    pg.display.update()


# Функция вывода матрицы
def mat_out(n):
    print("-------------")
    pp(n)
    print("-------------\n")

if __name__ == '__main__':
    main()
