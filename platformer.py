from pygame import *

win_width = 1600
win_height = 900

font.init()
font1 = font.Font(None, 80)

window = display.set_mode((win_width, win_height))
display.set_caption('this is not my game')

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, color, width, height, player_x, player_y, player_speed):
        super().__init__(color, width, height, player_x, player_y, player_speed)
        self.on_platform = False
        self.gravity = 0

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 50:
            self.rect.x += self.speed

        self.gravity += 0.5
        self.rect.y += self.gravity

        self.on_platform = False
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                # Падение на платформу сверху
                if self.gravity >= 0 and self.rect.bottom >= plat.rect.top:
                    self.rect.bottom = plat.rect.top
                    self.gravity = 0
                    self.on_platform = True

        if keys[K_UP] and self.on_platform:
            self.gravity = -10

        if self.rect.bottom >= win_height:
            self.rect.bottom = win_height
            self.gravity = 0
            self.on_platform = True

class platform(GameSprite):
    def __init__(self, color, width, height, plat_x, plat_y):
        super().__init__(color, width, height, plat_x, plat_y, 0)

player = Player((255, 0, 0), 40, 40, 100, 500, 5)

platforms = sprite.Group()
platforms.add(Platform((0, 255, 0), 200, 30, 0, 550))
platforms.add(Platform((0, 255, 0), 150, 30, 300, 450))
platforms.add(Platform((0, 255, 0), 150, 30, 550, 350))
platforms.add(Platform((0, 255, 0), 150, 30, 750, 250))

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    player.update(platforms)
    
    window.fill((135, 206, 235))
    
    for plat in platforms:
        plat.reset()
    
    player.reset()

    clock.tick(FPS)
    display.update()