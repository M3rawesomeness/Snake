import pygame as pg
from pygame import MOUSEBUTTONDOWN

import Snake
import Apple
import Physics
from Const import gen_const
from Const import button_dict

pg.init()
SCREEN_SIZE = (gen_const["length"], gen_const["width"])

clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("SNAKE")

button_color = []
keys = button_dict.keys()
for key in keys:
    button_color.append(button_dict[key]["color"])
shift_in_color = 10

button_color_prime = []
for color in button_color:
    current_color = []
    for i in range(3):
        current_color.append(color[i] - shift_in_color)
    button_color_prime.append(tuple(current_color))
button_rect = []
for key in keys:
    button_rect.append(pg.Rect(button_dict[key]["pos"], (button_dict[key]["length"], button_dict[key]["width"])))


def starting_menu() -> bool:
    running = True
    while running:
        screen.fill(gen_const["color"])
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == MOUSEBUTTONDOWN:
                # TODO: check for mouse pos on specific rectangle, output its function
                pass
        i = 0
        for rect in button_rect:
            if rect.collidepoint(mouse_pos):
                color = button_color_prime[i]
            else:
                color = button_color[i]

            pg.draw.rect(screen, color, rect)
            i += 1
        pg.display.flip()
    return True


def main() -> None:
    delta: float = 0.0
    snake = Snake.SnakeBody(screen)
    draw_snake_body_event = pg.USEREVENT + 1
    pg.time.set_timer(draw_snake_body_event, 60)

    # Physics Vars
    phys = Physics.Physics()
    colliding_bool: bool = False

    # Apple vars
    apples = Apple.Apple(screen)
    num_of_apples_at_one_time: int = 1
    # Wall vars
    wall_rect = []

    running: bool = starting_menu()
    while running:
        # Event handling for closing the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == draw_snake_body_event:
                snake.move_body()

        # Testing Should be deleted, used to quick close program:
        k = pg.key.get_pressed()
        if k[pg.K_q]:
            running = False

        # Redraws backgrounds
        screen.fill(gen_const["color"])

        # Snake
        snake.process(delta)

        # Apples
        while len(apples.apple_rect) < num_of_apples_at_one_time:
            apples.generate_apple(snake.get_snake_rect(), wall_rect)
        apples.process()

        # Collisions
        collision_index = phys.check_collisions(snake.snake_rect[0], apples.apple_rect)
        if collision_index > -1 and not colliding_bool:
            colliding_bool = True
            snake.increase_length()
            apples.apple_rect.pop(collision_index)  # Don't need return
        if collision_index <= -1 and colliding_bool:
            colliding_bool = False
        # print(len(snake.snake_rect))

        if snake.check_game_over():
            running = False

        delta = clock.tick(60) / 1000
        pg.display.flip()
    pg.quit()

    def check_game_over() -> bool:
        values = snake.game_end_cause.values()
        return True in values


main()
