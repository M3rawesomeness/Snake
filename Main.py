import pygame as pg
import Snake
import Apple
import Physics
from Const import gen_const

pg.init()
SCREEN_SIZE = (gen_const["length"], gen_const["width"])

clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("SNAKE")

"""def starting_menu() -> None:
    running = True
    while running:
        pass

"""


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
    running: bool = True
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
