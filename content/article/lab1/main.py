import numpy as np
import pygame as pg
from pprint import pprint as pp
import sys


def main():
    T = np.array([[1, 3], [4, 1]])
    lab1_1(T)
    lab1_2()
    lab1_3(T)
    lab1_4(T)


# Самостоятельная работа 1
def lab1_1(tran):
    print("Enter A:")
    A = mat_in(2)
    print("A")
    mat_out(A)
    print("T")
    mat_out(tran)
    A1 = A @ tran
    print("A1")
    mat_out(A1)


# Самостоятельная работа 2
def lab1_2():
    sc = pg.display.set_mode((600, 400))
    pg.font.init()
    print("Line/Circle/Text\nClose the pygame's window to continue\n")
    pg.draw.line(sc, (255, 255, 255), [10, 30], [290, 15], 3)
    pg.draw.circle(sc, (230, 50, 230), (100, 100), 50, 5)
    f = pg.font.SysFont('serif', 48)
    t = f.render("Hello world!", False, (190, 60, 30))
    sc.blit(t, (10, 170))
    pg.display.update()
    pg_window()


# Самостоятельная работа 3
def lab1_3(tran):
    print("Enter B:")
    B = mat_in(2)
    print("B")
    mat_out(B)
    print("T")
    mat_out(tran)
    B1 = B @ tran
    print("B1")
    mat_out(B1)
    sc = pg.display.set_mode((600, 400))
    pg.font.init()
    pg.draw.circle(sc, (10, 50, 230), (B[0], B[1]), 50, 10)
    pg.draw.circle(sc, (10, 150, 10), (B1[0], B1[1]), 50, 10)
    f1 = pg.font.SysFont('serif', 24)
    t1 = f1.render(f"{B}", False, (10, 50, 230))
    f2 = pg.font.SysFont('serif', 24)
    t2 = f2.render(f"{B1}", False, (10, 150, 10))
    sc.blit(t1, (B[0], B[1] + 75))
    sc.blit(t2, (B1[0], B1[1] + 75))
    pg.display.update()
    print("Close the pygame's window to continue\n")
    pg_window()


# Самостоятельная работа 4
def lab1_4(tran):
    print("Enter C:")
    C = mat_in(2)
    print("C")
    mat_out(C)
    print("T")
    mat_out(tran)
    C1 = C @ tran
    print("C1")
    mat_out(C1)
    print("Enter D:")
    D = mat_in(2)
    print("D")
    mat_out(D)
    print("T")
    mat_out(tran)
    D1 = D @ tran
    print("D1")
    mat_out(D1)
    sc = pg.display.set_mode((600, 400))
    pg.font.init()
    print("Close the pygame's window to continue\n")
    pg.draw.line(sc, (255, 0, 0), C, D, 3)
    pg.draw.line(sc, (0, 0, 255), C1, D1, 3)
    f = pg.font.SysFont('serif', 24)
    t1_1 = f.render(f"{C}", False, (255, 0, 0))
    t1_2 = f.render(f"{D}", False, (255, 0, 0))
    t2_1 = f.render(f"{C1}", False, (0, 0, 255))
    t2_2 = f.render(f"{D1}", False, (0, 0, 255))
    sc.blit(t1_1, (C[0], C[1] + 5))
    sc.blit(t1_2, (D[0], D[1] + 5))
    sc.blit(t2_1, (C1[0], C1[1] + 5))
    sc.blit(t2_2, (D1[0], D1[1] + 5))
    pg.display.update()
    pg_window()


# Функция ввода матрицы
def mat_in(n):
    mat = []
    for i in range(n):
        mat.append(int(input()))
    return np.array(mat)


# Функция вывода матрицы
def mat_out(n):
    print("-------------")
    pp(n)
    print("-------------\n")


# Функция открытого окна pygame
def pg_window():
    running = True
    while running:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                running = False
                pg.quit()


if __name__ == '__main__':
    main()
