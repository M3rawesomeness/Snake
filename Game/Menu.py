import pygame as pg


class Menu:
    screen: pg.SurfaceType

    def __init__(self, screen: pg.SurfaceType):
        pass

    def window_loop(self):
        pass

    def starting_menu(self, button_dict: dict) -> bool:
        self.window_loop()
        return False

    def escape_menu(self):
        pass

    def setting_menu(self):
        pass

    def controls_menu(self):
        pass
