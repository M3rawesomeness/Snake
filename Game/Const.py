import pygame as pg

gen_const = {
    "length": 800,
    "width": 800,
    "color": (50, 168, 82),
    "color_shift": 10,
}

button_dict = {
    "start": {
        "pos": (50, 650),
        "length": 300,
        "width": 100,
        "color": (50, 50, 100),
    },
    "quit": {
        "pos": (450, 650),
        "length": 300,
        "width": 100,
        "color": (100, 50, 50),
    },
}
snake_const = {
    "starting_pos": (100, 100),
    "size": (25, 25),
    "color": (50, 113, 170),
    "length": 3,
    "increase": 5
}
apple_const = {
    "color": (207, 46, 10),
    "size": (25, 25)
}
