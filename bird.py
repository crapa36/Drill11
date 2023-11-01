from pico2d import *
import game_world
import game_framework
import random
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 20.0):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.velocity =random.randint(20, 40)
        self.x=random.randint(100, 1400)
        self.y= random.randint(200, 500)
        self.frame=0
        self.dir=1.0

    def draw(self):
        frame_width = 182
        frame_height = 167
        sheet_columns = 5
        sheet_rows = 3
        frame_index = int(self.frame) % (sheet_columns * sheet_rows)
        frame_x = (frame_index % sheet_columns) * frame_width
        frame_y = (sheet_rows - 1 - frame_index // sheet_columns) * frame_height
        if self.dir>0:
            self.image.clip_draw(frame_x, frame_y, frame_width, frame_height, self.x, self.y)
        else:
            self.image.clip_composite_draw(
                frame_x,
                frame_y,
                frame_width,
                frame_height,
                0,
                "h",
                self.x,
                self.y,
                frame_width,
                frame_height,
            )
    def update(self):
        PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
        RUN_SPEED_KMPH = self.velocity # Km / Hour
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600-25)
       

        if self.x > 1600 - 50:
            self.dir=-1
        elif self.x < 50:
            self.dir=1