import pygame as pg
import Const


class Menu:
    button_dict = Const.button_dict
    button_rect_dict = {}
    button_color: list[tuple[int, int, int]] = []
    button_color_prime: list[tuple[int, int, int]] = []

    screen: pg.SurfaceType

    def __init__(self, screen: pg.SurfaceType):
        self.screen = screen
        self.set_button_rect(self.button_dict)
        self.set_color(self.button_dict)
        self.set_color_prime(self.button_color)

    def set_button_rect(self, button: dict) -> None:
        """
        Set button_rect list with all the buttons provided in Const.py file
        :param button: The dictionary containing all the buttons
        :return: Returns nothing, but manipulates button_rect list
        """
        button_keys = button.keys()
        for key in button_keys:
            self.button_rect_dict[key] = pg.Rect(button[key]["pos"], (button[key]["length"], button[key]["width"]))

    def set_color(self, button: dict) -> None:
        """
        Extracts color of each rectangle as provided in the Const.py File
        :param button: The dictionary of buttons
        :return: None, change button_color list
        """
        keys = button.keys()
        for key in keys:
            self.button_color.append(button[key]["color"])

    def set_color_prime(self, colors: list[tuple[int, int, int]]) -> None:
        """
        Set the color primes for each button, color which it is when hovered over with mouse
        :param colors:
        :return: None
        """
        shift = Const.gen_const["color_shift"]
        for color in colors:
            self.button_color_prime.append((color[0] - shift, color[1] - shift, color[2] - shift))

    def calc_color(self, index: int, mouse_pos: tuple[int, int]) -> tuple[int, int, int]:
        """
        Calculate the color of each button
        :param index: The current button in question
        :param mouse_pos: The position of the mouse
        :return: Return the proper color of the button depending on if the mouse is hovering on it
        """
        counter = 0  # Used to track current colliding button
        for rect in self.button_rect_dict.values():
            # Must check is colliding AND colliding with
            # And colliding with the current button whom color
            # is being chosen
            if rect.collidepoint(mouse_pos) and counter == index:
                return self.button_color_prime[index]
            counter += 1
        return self.button_color[index]

    def starting_menu(self) -> None:
        running = True
        while running:
            self.screen.fill(Const.gen_const["color"])
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            index = 0
            for rect in self.button_rect_dict.values():
                color = self.calc_color(index, mouse_pos)
                pg.draw.rect(self.screen, color, rect)
                index += 1
            pg.display.flip()

    def escape_menu(self):
        pass

    def setting_menu(self):
        pass

    def controls_menu(self):
        pass
