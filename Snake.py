import pygame as pg
from pygame import SurfaceType
from Const import gen_const
from Const import snake_const as const


class SnakeBody:
    surface: SurfaceType
    starting_pos = const["starting_pos"]
    size = const["size"]
    color = const["color"]
    length = const["length"]
    increase = const["increase"]

    screen_length = gen_const["length"]
    screen_width = gen_const["width"]
    direction = pg.Vector2(1, 0)
    snake_length: int = const["length"]
    snake_rect = []
    MAX_SNAKE_LENGTH: int

    game_end_cause = {
        "out_of_x": False,
        "out_of_y": False,
        "snake_length_reached": False,
        "collide_with_self": False,
    }

    def __init__(self, screen: SurfaceType) -> None:
        for body_section in range(self.snake_length):
            # The positions of the snake body change depending on the current length of the snake,
            # Each part of the snake is the length of the snake less than the previous snake in the x direction
            # This is only done once for the beginning of the snake as it creates the first snake_length number of body sections
            self.snake_rect.append(
                pg.Rect((self.starting_pos[0] - self.size[0] * body_section, self.starting_pos[1]), self.size))
        pg.init()
        self.set_surface(screen)
        self.SCREEN_WIDTH = screen.get_size()[0]
        self.SCREEN_LENGTH = screen.get_size()[1]
        self.MAX_SNAKE_LENGTH = (self.SCREEN_WIDTH // self.size[0]) * (self.SCREEN_LENGTH // self.size[1]) - 2

    def process(self, _delta: float) -> None:
        # Deals with the current direction of the snake
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and not self.direction == pg.Vector2(1, 0):
            self.direction = pg.Vector2(-1, 0)
        if keys[pg.K_d] and not self.direction == pg.Vector2(-1, 0):
            self.direction = pg.Vector2(1, 0)
        if keys[pg.K_w] and not self.direction == pg.Vector2(0, 1):
            self.direction = pg.Vector2(0, -1)
        if keys[pg.K_s] and not self.direction == pg.Vector2(0, -1):
            self.direction = pg.Vector2(0, 1)
        self.draw()

    def draw(self) -> None:
        """Draws the snake each frame"""
        for i in range(len(self.snake_rect)):
            snake_color = (
                self.color[0],
                self.color[1],
                self.color[2]
            )

            pg.draw.rect(self.surface, snake_color, self.snake_rect[i])

    def move_body(self) -> None:
        """Moves the last snake section to the appropriate position"""
        self.snake_rect[len(self.snake_rect) - 1].update((self.snake_rect[0].x + self.size[0] * self.direction.x,
                                                          self.snake_rect[0].y + self.size[1] * self.direction.y),
                                                         self.size)
        self.snake_rect.insert(0, self.snake_rect[len(self.snake_rect) - 1])
        self.snake_rect.pop()  # dont care for return

    def set_surface(self, surface: SurfaceType) -> None:
        self.surface = surface

    def get_snake_rect(self) -> list:
        return self.snake_rect

    def increase_length(self) -> None:
        """Increases the length of the snake"""
        for i in range(self.increase):
            tail_index: int = len(self.snake_rect) - 1

            x = self.get_x_from_list(self.snake_rect, tail_index)
            y = self.get_y_from_list(self.snake_rect, tail_index)

            rect = pg.Rect((x, y), self.size)
            self.snake_rect.append(rect)

    @staticmethod
    def get_x_from_list(rect: list, index: int) -> int:
        return rect[index].x

    @staticmethod
    def get_y_from_list(rect: list, index: int) -> int:
        return rect[index].y

    def get_head_position(self) -> tuple:
        head_index = 0
        x = self.get_x_from_list(self.snake_rect, head_index)
        y = self.get_y_from_list(self.snake_rect, head_index)
        return x, y

    def check_game_over(self) -> bool:
        position = self.get_head_position()
        buffer = 5
        if position[0] >= self.screen_width - self.size[0] + buffer or position[0] <= 0 - buffer:
            self.game_end_cause["out_of_x"] = True
            return True
        if position[1] >= self.screen_length - self.size[1] + buffer or position[1] <= 0 - buffer:
            self.game_end_cause["out_of_y"] = True
            return True
        if len(self.snake_rect) == self.MAX_SNAKE_LENGTH:
            self.game_end_cause["snake_length_reached"] = True
            return True
        if self.snake_rect[0].collidelist(self.snake_rect[1:]) != -1:
            self.game_end_cause["collide_with_self"] = True
            return True
        return False
