from pico2d import *

import game_framework
import game_world
import random

PIXEL_PER_METER = 10.0 / 0.3
BIRD_SIZE_M = 1.5 # 150cm정도의 크기
BIRD_SPEED_KMPH = 80.0 # 시속 80km 속도
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.velocity = random.randint(200,1400),random.randint(300,550) , BIRD_SPEED_PPS # 초당 픽셀이 가는 거리를 계산한 값
        self.frame = 0
        self.dir = 1

    def draw(self):
        Bird.image.clip_draw(int(self.frame) * 100, 0, 100, 100,self.x, self.y
                             ,BIRD_SIZE_M*PIXEL_PER_METER, BIRD_SIZE_M*PIXEL_PER_METER) # 실세계의 크기 30cm를 픽셀로 변환
        self.frame = (self.frame + 1) % 14

    def update(self):
        self.x += self.velocity * game_framework.frame_time * self.dir

        if self.x < 25:
            self.dir = 1
            self.x = 25
        elif self.x > 1600 - 25:
            self.dir = -1
            self.x = 1600 - 25

