import pygame
from pygame.locals import *
import sys
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 1410
screen_height = 711
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("zaozao")

# 尝试加载图片资源，并处理异常
try:
    background = pygame.image.load("background.jpg")
    player_img = pygame.image.load("player.jpg")
    enemy_img = pygame.image.load("enemy.jpg")
except pygame.error as e:
    print(f"无法加载图片: {e}")
    pygame.quit()
    sys.exit()


# 定义玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < screen_width:
            self.rect.move_ip(5, 0)

        # 定义敌人飞机类


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, screen_width)
        self.rect.top = 0

    def update(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > screen_height:
            self.kill()

        # 创建精灵组


all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# 创建玩家飞机实例
player = Player()
all_sprites.add(player)

# 初始生成敌人飞机实例
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏主循环
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            # 更新精灵位置
    all_sprites.update()

    # 检查碰撞
    if pygame.sprite.spritecollide(player, enemies, True):
        print("Game Over! Regenerating enemies...")
        # 重置敌人
        enemies.empty()
        all_sprites.remove(player)  # 如果需要重置玩家位置或状态也在这里做
        player = Player()  # 重新创建玩家实例
        all_sprites.add(player)
        # 重新生成敌人
        for _ in range(5):
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

            # 绘制背景和所有精灵
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(30)