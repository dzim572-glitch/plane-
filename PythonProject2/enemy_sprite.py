#敌机精灵
import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name,speed=1,size=None):
        super().__init__()#Sprite初始化没有参数
        self.image=pygame.image.load(image_name)
        if size is not None:
            self.image=pygame.transform.scale(self.image,size)
        self.rect=self.image.get_rect() #获取图片的宽和高，是一个位置对象
        #默认x,y点是(0,0)
        self.speed=speed
    def update(self,*args):
        #垂直向下运动
        self.rect.y+=self.speed

