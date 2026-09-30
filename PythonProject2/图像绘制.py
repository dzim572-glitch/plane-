import pygame
from enemy_sprite import GameSprite
pygame.init()
screen =pygame.display.set_mode((700,400))

#加载图像
bg=pygame.image.load('image1/sz.JPG')
bg=pygame.transform.scale(bg,(700,400))
screen.blit(bg,(0,0))
#绘制飞机
plane=pygame.image.load('image1/gy.JPG')
plane=pygame.transform.scale(plane,(102,126))
plane_rect=pygame.Rect(350,400,102,126)
screen.blit(plane,plane_rect)


pygame.display.update()

#实例化敌机精灵对象
enemy1=GameSprite('image1/ssl.JPG',3,size=(102,126))

enemy2=GameSprite('image1/wsc.JPG',1,size=(102,126))

#将精灵添加到精灵组中统一管理
enemy_group=pygame.sprite.Group()
enemy_group.add(enemy1,enemy2)
enemy2.rect.x=100
enemy2.rect.y=0

#创建时钟对象
clock=pygame.time.Clock()
#通过循环clock.tick(60)




#游戏开始
while True:
    clock.tick(60) #一个动画60帧

    #捕捉所有发送的时间列表
    event_list=pygame.event.get()
    if len(event_list)>0:
        print(event_list)

    #背景图像
    screen.blit(bg,(0,0))
    #修改飞机位置 向上移动
    plane_rect.y-=3
    if plane_rect.y<-plane_rect.height:
        plane_rect.y=600#当飞机飞出屏幕顶部后 从屏幕下方重新进入屏幕
    #控制飞机不飞出屏幕
    # if plane_rect.y<0:
    #     plane_rect.y=0
    #调用blit方法将图像位置更新
    screen.blit(plane,plane_rect)

    #敌机精灵组调用update和draw来更新位置绘制到屏幕上
    enemy_group.update()#self.rect.y+=1
    enemy_group.draw(screen) #screen.blit(self.image,self.rect)

    #调用update方法
    pygame.display.update()























