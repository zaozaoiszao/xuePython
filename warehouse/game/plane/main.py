import pygame  
from pygame.locals import *  
import sys  
import random
import math 
import time
import tkinter

# 设置生成新敌人的频率（例如，每30帧生成一次）  
#enemy_spawn_rate = int(input('请输入您的难度，请输入数字：'))
enemy_spawn_rate = 5

# 初始化pygame  
pygame.init()
  
# 设置窗口大小  
screen_width = 1410  
screen_height = 711  
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption("zaozao")  
  
# 尝试加载图片资源，并处理异常  
try:  
    background = pygame.image.load(r".\warehouse\game\plane\background.jpg")  
    player_img = pygame.image.load(r".\warehouse\game\plane\player.jpg")  
    enemy_img = pygame.image.load(r".\warehouse\game\plane\enemy.jpg")  
except pygame.error as e:  
    print(f"无法加载图片: {e}")  
    pygame.quit()  
    sys.exit()  
  
# 尝试加载声音资源  
try:  
    die_sound = pygame.mixer.Sound(r".\warehouse\game\plane\die.mp3")  
except pygame.error as e:  
    print(f"无法加载声音文件: {e}")  
    pygame.quit()  
    sys.exit()

# 定义子弹类  
class Bullet(pygame.sprite.Sprite):  
    def __init__(self, x, y):  
        super().__init__()  
        # 假设没有子弹图像，使用红色矩形代替  
        self.image = pygame.Surface((10, 20))  
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect(center=(x, y))  
        self.speed = 10  
  
    def update(self):  
        self.rect.y -= self.speed  
        # 如果子弹移出屏幕，则销毁  
        if self.rect.bottom < 0:  
            self.kill()  
  
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
  
    def shoot(self):  
        # 在玩家飞机底部中央创建子弹  
        bullet = Bullet(self.rect.centerx, self.rect.bottom)  
        all_sprites.add(bullet)  
        bullets.add(bullet)  
        
    def ultimate_shoot(self):  
        # 假设我们发射8个方向的子弹  
        directions = [0, 45, 90, 135, 180, 225, 270, 315]  
        for angle in directions:  
            # 计算子弹的初始位置（玩家底部中心沿角度偏移）  
            rad = math.radians(angle)  
            x_offset = math.cos(rad) * 50  # 偏移量可以根据需要调整  
            y_offset = math.sin(rad) * 50  # 偏移量可以根据需要调整  
            bullet_x = self.rect.centerx + x_offset  
            bullet_y = self.rect.bottom  
  
            # 创建子弹并添加到组  
            bullet = Bullet(bullet_x, bullet_y)  
            all_sprites.add(bullet)  
            bullets.add(bullet)  
  
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
    '''
    def dazhao(self):
        self.kill()
    '''

# 创建精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()  # 新增子弹组
  
# 创建玩家飞机实例  
player = Player()  
all_sprites.add(player)  
  
# 初始生成敌人飞机实例  
for _ in range(5):  
    enemy = Enemy()  
    all_sprites.add(enemy)  
    enemies.add(enemy)

# 添加一个计数器来跟踪帧数 
frame_counter = 0  
# 设置生成新敌人的频率（例如，每30帧生成一次）  
#enemy_spawn_rate = int(input('请输入您的难度，请输入数字：'))

# 游戏主循环  
clock = pygame.time.Clock()  
while True:  
    for event in pygame.event.get():  
        if event.type == QUIT:  
            pygame.quit()  
            sys.exit()  
        if event.type == KEYDOWN:  
            if event.key == K_SPACE:  
                player.shoot()  # 玩家按下空格键时发射子弹  
            if event.key == K_q:  
                player.ultimate_shoot()  # 玩家按下q键时执行大招  
            if event.key == K_ESCAPE:  
                pygame.quit()  
                sys.exit()  
            # 添加大招的按键检测  
            if event.key == K_1:  
                # 清空敌人组中的所有敌人  
                for enemy in enemies:  
                    enemy.kill()  
    # 更新帧计数器  
    frame_counter += 1  

    # 如果达到生成敌人的帧数，则生成新敌人  
    if frame_counter >= enemy_spawn_rate:  
        frame_counter = 0  # 重置计数器  
        for _ in range(5):  # 假设每次生成5个敌人  
            enemy = Enemy()  
            all_sprites.add(enemy)  
            enemies.add(enemy) 
  
    # 更新精灵位置  
    all_sprites.update()  

    # 检查玩家与敌人的碰撞  
    if pygame.sprite.spritecollide(player, enemies, False):  # False表示不删除碰撞的敌人  
        print("玩家与敌人发生碰撞！")  
        die_sound.play()  # 播放死亡声音
        #print('\a')
        # 这里可以添加玩家死亡后的逻辑，比如重置游戏或显示游戏结束界面
        time.sleep(1)
        pygame.quit()  
        sys.exit()
  
    # 检查子弹与敌人的碰撞  
    for bullet in list(bullets):  # 使用list避免在迭代时修改集合  
        if pygame.sprite.spritecollide(bullet, enemies, True):  # True表示删除碰撞的敌人  
            bullet.kill()  # 子弹击中敌人后也销毁
            
    # 绘制背景和所有精灵
    screen.blit(background, (0, 0))  
    all_sprites.draw(screen)  
  
    # 更新屏幕  
    pygame.display.flip()  
  
    # 控制帧率  
    clock.tick(60)   