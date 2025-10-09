import random

import pygame as pg
from pygame import SurfaceType
from Const import apple_const as const
from Const import gen_const as gen_const


class Apple:
    screen: SurfaceType
    size = const["size"]
    screen_length = gen_const["length"]
    screen_width = gen_const["width"]
    color = const["color"]
    apple_rect = []

    def __init__(self, screen: SurfaceType):
        pg.init()
        self.set_screen(screen)

        # The size of which the apples could spawn is less than the actual screen length and width
        # But instead is smaller by the size of the apple

    def process(self) -> None:
        self.draw()

    def generate_apple(self, snake_rect: list, wall_rect: list) -> None:
        snake_rect_coords = self.get_coords(snake_rect)
        wall_rect_coords = self.get_coords(wall_rect)
        apple_rect_coords = self.get_coords(self.apple_rect)

        x = self.check_coord(snake_rect_coords, wall_rect_coords, apple_rect_coords, self.screen_width)
        y = self.check_coord(snake_rect_coords, wall_rect_coords, apple_rect_coords, self.screen_length)

        self.apple_rect.append(pg.Rect((x, y), self.size))

    def check_coord(self, list_1: list, list_2: list, list_3: list, limit: int) -> int:
        coord = random.randrange(0, limit, self.size[0])
        while coord in list_1 or coord in list_2 or coord in list_3:
            coord = random.randrange(0, limit, self.size[0])
        return coord

    @staticmethod
    def get_coords(arr: list) -> list:
        return_list = []
        for i in arr:
            return_list.append((i.x, i.y))
        return return_list

    def draw(self) -> None:
        """Draws the apple to the screen"""
        for apple in self.apple_rect:
            pg.draw.rect(self.screen, self.color, apple)

    def set_screen(self, screen: SurfaceType) -> None:
        self.screen = screen
