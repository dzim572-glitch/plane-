#精灵
import pygame
import random
#敌机出场 事件代号
ENEMY_EVENT=pygame.USEREVENT
#子弹发射事件代号
FIRE=pygame.USEREVENT+1

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
#背景精灵类
class Background(GameSprite):
    def update(self):
        #调用父类方法实现向下移动
        super().update()
        #判断是否移出屏幕 如果是将图像设置在屏幕上方
        if self.rect.y >= 700:
            self.rect.y=-self.rect.height


class Enemy(GameSprite):
    #调用父类 传递敌机图片
    def __init__(self):
        super().__init__('image1/wsc.png')
        #指定敌机的初始随机速度
        self.speed=random.randint(2,4)
        #指定敌机的初始随机位置
        self.rect.x=random.randint(0,500)


        def update(self):
            #调用父类方法，保持垂直向下飞机
            if self.rect.y>=700:
                print('敌机飞出，需要删除')
                self.kill()#精灵类提供的方法能够删除精灵对象

#英雄飞机精灵组
class Hero(GameSprite):
    def __init__(self):
        super().__init__('image1/gy.png',0)
        #设置飞机初始位置
        self.rect.x=600-self.rect.width
        self.rect.y=600-self.rect.height
        #用来控制英雄上下移动的属性
        self.upanddown=0
        #组合使用，创建子弹精灵组
        self.bullet_group=pygame.sprite.Group()


    def update(self):
        self.rect.x+=self.speed
        self.rect.y+=self.upanddown
        if self.rect.x>=700-self.rect.width:
            self.rect.x=700-self.rect.width
        elif self.rect.x <=0:
            self.rect.x=0
        #垂直方向同理：不让飞机飞出屏幕上下边缘
        if self.rect.y>=700-self.rect.height:
            self.rect.y=700-self.rect.height
        elif self.rect.y<=0:
            self.rect.y=0
        if self.rect.y>=700-self.rect.height:
            self.rect.y=700-self.rect.height
        elif self.rect.y<=0:
            self.rect.y=0

    def fire(self):
        print("发射子弹")
        for i in range(3):
            bullet=Bullet()
            #设置每颗子弹的初始位置
            bullet.rect.centerx=self.rect.centerx #self指飞机
            bullet.rect.y=self.rect.y-(i+1)*20


            self.bullet_group.add(bullet)




#子弹精灵类
class Bullet(GameSprite):
    def __init__(self):
        super().__init__('image1/ssl.png',-2)
        # self.image=pygame.image.load('image1/bullet.png')
    def update(self):
        # self.rect.y-=self.speed
        #调用父类让子弹垂直移动
        super().update()
        if self.rect.y<=0:
            self.kill()




























