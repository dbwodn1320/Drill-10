import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from bird import Bird

name = "MainState"

boy = None

bird0 = None
bird1 = None
bird2 = None
bird3 = None
bird4 = None

def enter():
    global boy
    global bird0,bird1,bird2,bird3,bird4
    boy = Boy()
    bird0 = Bird()
    bird1 = Bird()
    bird2 = Bird()
    bird3 = Bird()
    bird4 = Bird()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(bird0, 1)
    game_world.add_object(bird1, 1)
    game_world.add_object(bird2, 1)
    game_world.add_object(bird3, 1)
    game_world.add_object(bird4, 1)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






