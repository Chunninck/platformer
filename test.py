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
        super().__init__()
        if isinstance(player_image, str):
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
        else:
            self.image = transform.scale(player_image, (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.on_platform = False
        self.gravity = 0
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, color, width, height, player_x, player_y, player_speed):
        self.image = Surface((width, height))
        self.image.fill(color)
        super().__init__(self.image, player_x, player_y, width, height, player_speed)

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

class Platform(GameSprite):
    def __init__(self, color, width, height, plat_x, plat_y):
        self.image = Surface((width, height))
        self.image.fill(color)
        super().__init__(self.image, plat_x, plat_y, width, height, 0)

# Создаем игрока
player = Player((255, 0, 0), 40, 40, 100, 750, 5)

# Создаем платформы
platforms = sprite.Group()
platforms.add(Platform((0, 255, 0), 200, 30, 0, 800))
platforms.add(Platform((0, 255, 0), 150, 30, 300, 700))
platforms.add(Platform((0, 255, 0), 150, 30, 550, 600))
platforms.add(Platform((0, 255, 0), 150, 30, 750, 730))
platforms.add(Platform((0, 255, 0), 200, 30, 950, 650))
platforms.add(Platform((0, 255, 0), 150, 30, 1250, 550))
platforms.add(Platform((0, 255, 0), 150, 30, 1450, 450))
platforms.add(Platform((0, 255, 0), 150, 30, 1250, 350))

platforms.add(Platform((0, 255, 0), 150, 30, 950, 300))
platforms.add(Platform((0, 255, 0), 150, 30, 750, 400))
platforms.add(Platform((0, 255, 0), 150, 30, 550, 300))
platforms.add(Platform((0, 255, 0), 150, 30, 300, 350))
platforms.add(Platform((0, 255, 0), 150, 30, 50, 250))
platforms.add(Platform((0, 255, 0), 150, 30, 270, 130))
platforms.add(Platform((0, 255, 0), 150, 30, 500, 100))
platforms.add(Platform((0, 255, 0), 150, 30, 800, 100))

platforms.add(Platform((0, 255, 0), 150, 30, 1100, 100))
platforms.add(Platform((0, 255, 0), 150, 30, 1400, 100))

platforms.add(Platform((0, 255, 0), 1600, 30, 0, 899))

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    player.update()  
    
    window.fill((135, 206, 235))
    
    for plat in platforms:
        plat.reset()

    if player.rect.y - 50 == win_height:
        player.rect.x = 40
        player.rect.y = 40
    
    player.reset()

    clock.tick(FPS)
    display.update()