import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘新飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # #设置背景颜色
    # bg_color = (230, 230, 230)无用消息

    #开始游戏主循环
    while True:
        #监听鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        #每次循环都重绘屏幕并显示
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
