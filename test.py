from pygame import *

win_width = 1600
win_height = 900

window = display.set_mode((win_width, win_height))
display.set_caption('this is not my game')

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()