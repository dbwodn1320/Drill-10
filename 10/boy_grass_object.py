from pico2d import *
import random

# Game object class here
# class Boy:
#     def __init__(self):
#         self.x, self.y = 0,90
#         self.image = load_image('run_animation.png')
#         self.frame = 0
#
#     def update(self):
#         self.frame = (self.frame + 1) % 8
#         self.x += 5
#
#     def draw(self):
#         self.image.clip(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class SmallBall():
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0,800),random.randint(500,600)
    def update(self):
        if self.y <= 40:
            self.y = 40
            return
        self.y -= 10
    def draw(self):
        self.image.clip_draw(0,0,23,23,self.x,self.y)

class BigBall():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0,800),random.randint(500,600)
    def update(self):
        if self.y <= 40:
            self.y = 40
            return
        self.y -= 10
    def draw(self):
        self.image.clip_draw(0,0,43,43,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()

#boy = Boy()
running = True
big_balls = [BigBall() for i in range(10)]
small_balls = [SmallBall() for i in range(10)]
# game main loop code
while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for BigBall in big_balls:
        BigBall.update()
    for BigBall in big_balls:
        BigBall.draw()
    for SmallBall in small_balls:
        SmallBall.update()
    for SmallBall in small_balls:
        SmallBall.draw()

    update_canvas()

close_canvas()
# finalization code
