import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        '''加载图像获取其外接矩形'''
        self.image = pygame.image.load('images/spaceship-g9bfe45d3c_1920.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新对象
        self.rect.centerx = self.center


    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)