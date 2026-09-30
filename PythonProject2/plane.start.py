import pygame
import plane_sprite

class PlaneGame:
    def __init__(self):
        #游戏初始化
        pygame.init()
        #设置游戏窗口
        self.screen=pygame.display.set_mode((700,700))
        #设置游戏时钟
        self.clock = pygame.time.Clock()

        #创建敌机出场定时器 每隔一秒钟出现敌机
        pygame.time.set_timer(plane_sprite.ENEMY_EVENT,1000)

        #创建一个子弹发射定时器 （每隔0.5秒发射一次）
        pygame.time.set_timer(plane_sprite.FIRE,500)


        #创建精灵 精灵组（初始化图像位置）#包含背景子弹敌方自己
        self.create_sprite() #通过调用函数来实现
        # 创建精灵 精灵组
    def create_sprite(self):
        #背景实现方式一

        #创建两个背景精灵 实现背景类似于扶梯操作
        bg1=plane_sprite.Background("image1/sz.jpg",size=(700,700))

        bg2=plane_sprite.Background("image1/sz.jpg",size=(700,700))
        bg2.rect.y=-bg2.rect.height
        #背景精灵组
        self.bg_group=pygame.sprite.Group() #创建精灵组
        self.bg_group.add(bg1,bg2)#将背景对象添加到精灵组中
        #创建敌机精灵组
        self.enemy_group=pygame.sprite.Group()

        #创建英雄飞机精灵 和精灵组
        self.hero=plane_sprite.Hero()
        self.hero_group=pygame.sprite.Group()
        self.hero_group.add(self.hero)



    # 事件监听
    def event_handler(self):
        #获取按键
        keys=pygame.key.get_pressed()
        #左右移动：只决定水平方向的速度
        if keys[pygame.K_RIGHT]:
            self.hero.speed=3
        elif keys[pygame.K_LEFT]:
            self.hero.speed=-3
        else:
            self.hero.speed=0
        #上下移动：只决定垂直方向的速度，和左右互不影响
        if keys[pygame.K_UP]:
            self.hero.upanddown=-2
        elif keys[pygame.K_DOWN]:
            self.hero.upanddown=2
        else:
            self.hero.upanddown=0


        for event in pygame.event.get():
            #判断当前事件的代号是否是敌机出场的代号
            if event.type == plane_sprite.ENEMY_EVENT:
                print('敌机出场')
                #创建敌机对象
                enemy=plane_sprite.Enemy()
                #将创建的敌机对象添加到敌机精灵组
                self.enemy_group.add(enemy)


            elif event.type==pygame.QUIT:
                pygame.quit()

            elif event.type==plane_sprite.FIRE:
                print("子弹发射")
                self.hero.fire()








    #碰撞检测
    def collide(self):

    # 子弹撞毁敌方飞机
    # 子弹和敌机都消失
         pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)

    # 敌方飞机撞英雄飞机
         ret=pygame.sprite.groupcollide(self.hero_group,self.enemy_group,True,True)
         if ret:
             pygame.quit()
    # 更新精灵组位置/绘制精灵组到屏幕上
    def update_sprite(self):
        #调用update draw方法
        #更新绘制背景精灵组
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        #更新绘制敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        #更新绘制英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        #更新绘制子弹精灵组
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)





    def start(self):
        while True:
            pass
            #设置刷新帧率
            self.clock.tick(60)
            #事件监听
            self.event_handler()

            #碰撞检测（游戏退出）
            self.collide()
            #更新精灵组位置/绘制精灵组到屏幕上‘
            self.update_sprite()
            #更新屏幕显示
            pygame.display.update()
if __name__=="__main__":
    game = PlaneGame()
    game.start()































