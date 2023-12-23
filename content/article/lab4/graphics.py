import pygame as pg


class Drawer:
    # Class constructor
    def __init__(self, res_x: int, res_y: int, color_depth: int):
        self.instance = pg.display.set_mode((res_x, res_y), color_depth)

    # Initialize 'pygame' graphics separately
    def initialize(self, caption: str):
        pg.init()
        pg.font.init()
        pg.display.set_caption(caption)

    # Put a text on the graphic surface
    def draw_text(self, x: float, y: float, text: str, size, color,
                  offset: float):
        f = pg.font.SysFont('Times New Roman', size)
        self.instance.blit(f.render(text, True, color),
                           (x + offset, y + offset))

    # Draw a line
    def draw_line(self, Mat, width: int, color, offset):
        pg.draw.lines(self.instance, color, True, Mat * 65 + offset, width)

    # Draw axes Ox and Oy with point O
    def draw_axes(self, x_min: float, x_max: float, y_min: float, y_max: float,
                  width: int, color, offset: float):
        pg.draw.lines(self.instance, color, True,
                      ([x_min + offset, y_max + offset
                        ], [x_max + offset, y_max + offset]), width)
        pg.draw.lines(self.instance, color, True,
                      ([offset, y_min + offset], [offset, y_max + offset]),
                      width)
