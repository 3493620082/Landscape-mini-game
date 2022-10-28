# --coding=utf-8
import random

import pygame
import sys

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("demo_2")

        self.load_sun()  # 加载太阳
        self.load_clouds()  # 加载云朵
        self.load_plane()  # 加载飞机
        self.load_car()  # 绘制汽车
        self.load_city()  # 加载城市场景
        self.load_volcano()  # 加载火山场景
        self.load_sea()  # 加载海洋场景
        self.load_grass()  # 加载草地场景
        self.load_choose_level()  # 加载主界面

        pygame.mixer.music.set_volume(0.2)  # 设置游戏音乐声音大小
        self.play_music("./music/辽阔行.mp3")

        self.clock = pygame.time.Clock()

        while True:
            self.clock.tick(60)  # 游戏帧率

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.key_list = pygame.key.get_pressed()  # 获取键盘事件

            if self.choose_true:  # 如果此变量为false
                if self.key_list[pygame.K_ESCAPE]:
                    self.choose_true = False
                    self.level_city = False
                    self.level_volcano = False
                    self.level_sea = False
                    self.level_grass = False
                if self.level_city:  # 如果触发了城市地图
                    self.play_music(self.city_music)
                    self.render_city()  # 渲染城市
                    self.render_sun()  # 渲染太阳
                    self.render_clouds()  # 渲染云朵
                    self.render_plane()  # 渲染飞机
                elif self.level_volcano:  # 如果触发了火山关卡
                    self.play_music(self.volcano_music)
                    self.render_volcano()
                    self.render_car(520)
                elif self.level_sea:
                    self.play_music(self.sea_music)
                    self.render_sea()
                    self.render_sun()
                    self.render_clouds()
                elif self.level_grass:
                    self.play_music(self.grass_music)
                    self.render_grass()
                    self.render_sun()
                    self.render_car(450)
            else:
                self.mouse_pos = pygame.mouse.get_pos()  # 获取鼠标坐标
                self.mouse_pressed = pygame.mouse.get_pressed()  # 获取鼠标状态，是否点击
                # print(self.mouse_pressed)  # (True, False, False)第一个为左键，第二个为中键，第三个为右键
                self.render_choose_level()

            pygame.display.update()  # 画面更新

    def load_choose_level(self):
        # 背景图片
        self.FengJing = pygame.image.load("./image/风景-1.jpg").convert()  # 加载风景图
        self.FengJing = pygame.transform.scale(self.FengJing, (1280, 720))  # 改变大小为1280x720
        # self.FengJingMask = pygame.Surface((1280, 720)).convert_alpha()  # 创建一个同等大小的Surface对象并开启alpha透明通道
        # self.FengJingMask.fill((0, 0, 0, 50))  # 将其填充为50%透明度的(0, 0, 0)
        # self.FengJing.blit(self.FengJingMask, (0, 0))  # 将其绘制在self.FengJing上就达到了想要的黑色遮罩效果
        # 字体设置
        self.f = pygame.font.SysFont('方正舒体', 25)  # 微软雅黑字体，25字号
        # 不同地图选项
        self.city_btn = pygame.Surface((192, 54)).convert_alpha()  # 城市按钮
        self.city_btn_rect = self.city_btn.get_rect()
        self.city_btn_text = self.f.render("城  市", True, (255, 128, 0), None)  # 城市，平滑字体True，颜色，背景色None
        self.city_btn_text_rect = self.city_btn_text.get_rect()
        self.volcano_btn = pygame.Surface((192, 54)).convert_alpha()  # 火山按钮
        self.volcano_btn_rect = self.volcano_btn.get_rect()
        self.volcano_btn_text = self.f.render("火  山", True, (255, 0, 255), None)  # 火山，平滑字体True，颜色，背景色None
        self.volcano_btn_text_rect = self.volcano_btn_text.get_rect()
        self.sea_btn = pygame.Surface((192, 54)).convert_alpha()  # 海洋按钮
        self.sea_btn_rect = self.sea_btn.get_rect()
        self.sea_btn_text = self.f.render("海  洋", True, (0, 255, 255), None)  # 海洋，平滑字体True，颜色，背景色None
        self.sea_btn_text_rect = self.sea_btn_text.get_rect()
        self.grass_btn = pygame.Surface((192, 54)).convert_alpha()  # 草地按钮
        self.grass_btn_rect = self.grass_btn.get_rect()
        self.grass_btn_text = self.f.render("草  地", True, (0, 255, 128), None)  # 草地，平滑字体True，颜色，背景色None
        self.grass_btn_text_rect = self.grass_btn_text.get_rect()
        # 存储所有按钮的列表和存储所有按钮rect的列表
        self.btn_list = [self.city_btn, self.volcano_btn, self.sea_btn, self.grass_btn]
        self.btn_rect_list = [self.city_btn_rect, self.volcano_btn_rect, self.sea_btn_rect, self.grass_btn_rect]
        # 将所有按钮的背景填充透明
        for btn in self.btn_list:
            btn.fill((0, 0, 0, 0))
        # 将所有文字居中绘制到按钮上
        # self.city_btn.blit(self.city_btn_text, (self.city_btn_rect[2] / 2 - self.city_btn_text_rect[2] / 2, self.city_btn_rect[3] / 2 - self.city_btn_text_rect[3] / 2))
        # self.volcano_btn.blit(self.volcano_btn_text, (self.volcano_btn_rect[2] / 2 - self.volcano_btn_text_rect[2] / 2, self.volcano_btn_rect[3] / 2 - self.volcano_btn_text_rect[3] / 2))
        # self.sea_btn.blit(self.sea_btn_text, (self.sea_btn_rect[2] / 2 - self.sea_btn_text_rect[2] / 2, self.sea_btn_rect[3] / 2 - self.sea_btn_text_rect[3] / 2))
        # self.grass_btn.blit(self.grass_btn_text, (self.grass_btn_rect[2] / 2 - self.grass_btn_text_rect[2] / 2, self.grass_btn_rect[3] / 2 - self.grass_btn_text_rect[3] / 2))
        # 一些变量
        self.choose_true = False  # choose_true判断是否已经开始进入游戏了，如果为False，则一直显示主界面
        self.btn_num = len(self.btn_list)  # 计算列表长度的变量，用于循环列表
        self.level_city = False  # 用于判断进入哪一个地图的布尔型变量
        self.level_volcano = False
        self.level_sea = False
        self.level_grass = False
        self.level_list = [self.level_city, self.level_volcano, self.level_sea, self.level_grass]

    def load_clouds(self):
        # 云朵图片
        self.clouds = pygame.image.load("./image/clouds_1.png").convert_alpha()  # 加载云朵的png图片
        self.clouds_rect = self.clouds.get_rect()
        self.clouds = pygame.transform.scale(self.clouds, (self.clouds_rect[2] * 0.2, self.clouds_rect[3] * 0.2))
        self.clouds_sum = random.randint(2, 5)  # 随机生成2-4朵数量的云
        self.clouds_size_list = []  # 用来存储每朵云的坐标信息
        for i in range(self.clouds_sum):  # 循环创建同等数量的云朵的随机开始坐标信息
            self.clouds_size = [random.randint(0, 1280), random.randint(0, 100)]  # 随机生成坐标
            self.clouds_size_list.append(self.clouds_size)  # 将坐标存储到列表里
        self.clouds_speed_list = []  # 创建列表用于存储每朵云朵的速度信息
        for i in range(self.clouds_sum):  # 循环同等数量的云朵并随机生成每朵云的速度信息
            self.clouds_speed = random.randint(1, 3)  # 随机生成速度信息
            self.clouds_speed_list.append(self.clouds_speed)  # 添加到列表里

    def load_sun(self):
        # 太阳图片
        self.sun = pygame.image.load("./image/sun_1.png").convert_alpha()
        self.sun_size = (random.randint(1, 1050), random.randint(1, 50))  # 随机生成坐标

    def load_plane(self):
        # 右向飞机
        self.plane_right = pygame.image.load("./image/plane_2.png").convert_alpha()  # 加载向右飞机的png图片
        self.plane_right_rect = self.plane_right.get_rect()
        self.plane_right = pygame.transform.scale(self.plane_right, (self.plane_right_rect[2] * 0.4, self.plane_right_rect[3] * 0.4))
        # print(self.plane_right.get_rect())
        # 左向飞机
        self.plane_left = pygame.image.load("./image/plane_1.png").convert_alpha()  # 加载向左飞机的png图片
        self.plane_left_rect = self.plane_left.get_rect()
        self.plane_left = pygame.transform.scale(self.plane_left, (self.plane_left_rect[2] * 0.4, self.plane_left_rect[3] * 0.4))
        # print(self.plane_left.get_rect())
        # 设置飞机起始位置
        self.plane = self.plane_right  # 用来表示用于绘制的那个飞机
        self.plane_size = [random.randint(1, 1100), random.randint(1, 600)]  # 随机生成飞机起始位置

    def load_car(self):
        # 右向汽车
        self.car_right = pygame.image.load("./image/car_1.png").convert_alpha()  # 加载向右汽车的png图片
        self.car_right_rect = self.car_right.get_rect()
        self.car_right = pygame.transform.scale(self.car_right,
                                                  (self.car_right_rect[2] * 0.2, self.car_right_rect[3] * 0.2))
        # print(self.plane_right.get_rect())
        # 左向汽车
        self.car_left = pygame.image.load("./image/car_2.png").convert_alpha()  # 加载向左汽车的png图片
        self.car_left_rect = self.car_left.get_rect()
        self.car_left = pygame.transform.scale(self.car_left,
                                                 (self.car_left_rect[2] * 0.2, self.car_left_rect[3] * 0.2))
        # print(self.plane_left.get_rect())
        # 设置汽车起始位置
        self.car = self.car_right  # 用来表示用于绘制的那个汽车
        self.car_size = [random.randint(1, 1100), 710 - self.car.get_rect()[3]]

    def load_city(self):  # 加载城市场景方法
        # 背景图片
        self.city_background = pygame.image.load("./image/city_background_2.jpg").convert()  # 加载城市图片
        self.city_background_rect = self.city_background.get_rect()  # (0, 0, 1920, 720)
        self.city_bg_size = [0, 0]  # 代表坐标的列表
        self.city_bg_width = self.city_background_rect[2]  # 获取图片的宽度
        # 游戏音乐
        self.city_music = "./music/summer-久石让.mp3"

    def load_volcano(self):
        # 背景图片
        self.volcano = pygame.image.load("./image/volcano_background_1.jpg").convert()  # 加载火山图片
        self.volcano_rect = self.volcano.get_rect()
        self.volcano_bg_size = [0, 0]  # 代表图片所处位置的坐标的列表
        self.volcano_bg_width = self.volcano_rect[2]  # 获取图片的宽度
        # 游戏音乐
        self.volcano_music = "./music/traveling light.mp3"

    def load_sea(self):
        self.sea = pygame.image.load("./image/sea_background_2.jpg").convert()
        self.sea_rect = self.sea.get_rect()
        self.sea_bg_size = [0, 0]
        self.sea_bg_width = self.sea_rect[2]
        # 游戏音乐
        self.sea_music = "./music/辽阔行.mp3"

    def load_grass(self):
        self.grass = pygame.image.load("./image/grass_background_1.jpg").convert()
        self.grass_rect = self.grass.get_rect()
        self.grass_bg_size = [0, 0]
        self.grass_bg_width = self.grass_rect[2]
        # 音乐
        self.grass_music = "./music/five hundred miles.mp3"

    def render_choose_level(self):
        # 绘制风景壁纸
        self.screen.blit(self.FengJing, (0, 0))
        # 判断鼠标是否点击按钮
        if (640 - self.city_btn_rect[2] / 2) < self.mouse_pos[0] < (640 + self.city_btn_rect[2] / 2) and 125 < self.mouse_pos[1] < (125 + self.city_btn_rect[3]):
            if self.mouse_pressed[0]:
                self.level_city = True
                self.choose_true = True
                pygame.mixer.music.load(self.city_music)
                pygame.mixer.music.play()
            self.city_btn.fill((255, 255, 255, 50))  # 只有被选中的按钮蒙上白色遮罩，其余的蒙上透明遮罩
            self.volcano_btn.fill((255, 255, 255, 0))
            self.sea_btn.fill((255, 255, 255, 0))
            self.grass_btn.fill((255, 255, 255, 0))
        elif (640 - self.volcano_btn_rect[2] / 2) < self.mouse_pos[0] < (640 + self.volcano_btn_rect[2] / 2) and 250 < self.mouse_pos[1] < (250 + self.volcano_btn_rect[3]):
            if self.mouse_pressed[0]:
                self.level_volcano = True
                self.choose_true = True
                pygame.mixer.music.load(self.volcano_music)
                pygame.mixer.music.play()
            self.city_btn.fill((255, 255, 255, 0))  # 只有被选中的按钮蒙上白色遮罩，其余的蒙上透明遮罩
            self.volcano_btn.fill((255, 255, 255, 50))
            self.sea_btn.fill((255, 255, 255, 0))
            self.grass_btn.fill((255, 255, 255, 0))
        elif (640 - self.sea_btn_rect[2] / 2) < self.mouse_pos[0] < (640 + self.sea_btn_rect[2] / 2) and 375 < self.mouse_pos[1] < (375 + self.sea_btn_rect[3]):
            if self.mouse_pressed[0]:
                self.level_sea = True
                self.choose_true = True
                pygame.mixer.music.load(self.sea_music)
                pygame.mixer.music.play()
            self.city_btn.fill((255, 255, 255, 0))  # 只有被选中的按钮蒙上白色遮罩，其余的蒙上透明遮罩
            self.volcano_btn.fill((255, 255, 255, 0))
            self.sea_btn.fill((255, 255, 255, 50))
            self.grass_btn.fill((255, 255, 255, 0))
        elif (640 - self.grass_btn_rect[2] / 2) < self.mouse_pos[0] < (640 + self.grass_btn_rect[2] / 2) and 500 < self.mouse_pos[1] < (500 + self.grass_btn_rect[3]):
            if self.mouse_pressed[0]:
                self.level_grass = True
                self.choose_true = True
                pygame.mixer.music.load(self.grass_music)
                pygame.mixer.music.play()
            self.city_btn.fill((255, 255, 255, 0))  # 只有被选中的按钮蒙上白色遮罩，其余的蒙上透明遮罩
            self.volcano_btn.fill((255, 255, 255, 0))
            self.sea_btn.fill((255, 255, 255, 0))
            self.grass_btn.fill((255, 255, 255, 50))
        else:
            self.city_btn.fill((255, 255, 255, 0))  # 只有被选中的按钮蒙上白色遮罩，其余的蒙上透明遮罩
            self.volcano_btn.fill((255, 255, 255, 0))
            self.sea_btn.fill((255, 255, 255, 0))
            self.grass_btn.fill((255, 255, 255, 0))

        # 绘制字体
        self.city_btn.blit(self.city_btn_text, (self.city_btn_rect[2] / 2 - self.city_btn_text_rect[2] / 2,
                                                self.city_btn_rect[3] / 2 - self.city_btn_text_rect[3] / 2))
        self.volcano_btn.blit(self.volcano_btn_text, (self.volcano_btn_rect[2] / 2 - self.volcano_btn_text_rect[2] / 2,
                                                      self.volcano_btn_rect[3] / 2 - self.volcano_btn_text_rect[3] / 2))
        self.sea_btn.blit(self.sea_btn_text, (self.sea_btn_rect[2] / 2 - self.sea_btn_text_rect[2] / 2,
                                              self.sea_btn_rect[3] / 2 - self.sea_btn_text_rect[3] / 2))
        self.grass_btn.blit(self.grass_btn_text, (self.grass_btn_rect[2] / 2 - self.grass_btn_text_rect[2] / 2,
                                                  self.grass_btn_rect[3] / 2 - self.grass_btn_text_rect[3] / 2))
        # 绘制按钮，因为字体本来就绘制在了按钮上，所以不用绘制字体
        for i in range(self.btn_num):
            self.screen.blit(self.btn_list[i], (640 - self.btn_rect_list[i][2] / 2, 125 * (i + 1)))
            # pygame.draw.rect(self.btn_list[i], (255, 255, 255), (0, 0, self.btn_rect_list[i][2], self.btn_rect_list[i][3]), 1)  # 绘制边框

    def render_city(self):
        # 图片滚动核心算法
        self.city_bg_size[0] -= 1  # 图片坐标后移
        if self.city_bg_size[0] == -self.city_bg_width:
            # 如果横坐标到达了-1920，也就是一张图片的长度，也就是刚好把第一张图片播放完，此时将横坐标变为0，
            # 代表将第一张图重新拉了回来，因为图片一样，坐标也一样，所以肉眼分辨不出异常，就达到了无限循环的效果，只需要再将图片设计一下就会顺眼许多
            self.city_bg_size[0] = 0
        self.screen.blit(self.city_background, (self.city_bg_size[0], 0))
        self.screen.blit(self.city_background, (self.city_bg_size[0] + self.city_background_rect[2], 0))

    def render_volcano(self):
        self.volcano_bg_size[0] -= 1
        if self.volcano_bg_size[0] == -self.volcano_bg_width:
            self.volcano_bg_size[0] = 0
        self.screen.blit(self.volcano, (self.volcano_bg_size[0], 0))
        self.screen.blit(self.volcano, (self.volcano_bg_size[0] + self.volcano_rect[2], 0))

    def render_sea(self):
        self.sea_bg_size[0] -= 1
        if self.sea_bg_size[0] == -self.sea_bg_width:
            self.sea_bg_size[0] = 0
        self.screen.blit(self.sea, (self.sea_bg_size[0], 0))
        self.screen.blit(self.sea, (self.sea_bg_size[0] + self.sea_rect[2], 0))

    def render_grass(self):
        self.grass_bg_size[0] -= 1
        if self.grass_bg_size[0] == -self.grass_bg_width:
            self.grass_bg_size[0] = 0
        self.screen.blit(self.grass, (self.grass_bg_size[0], 0))
        self.screen.blit(self.grass, (self.grass_bg_size[0] + self.grass_rect[2], 0))

    def render_sun(self):
        # 太阳绘制
        self.screen.blit(self.sun, self.sun_size)

    def render_clouds(self):
        # 云朵滚动核心算法
        for i in range(self.clouds_sum):  # 循环生成的云的数量
            self.screen.blit(self.clouds, (self.clouds_size_list[i][0], self.clouds_size_list[i][1]))  # 按照坐标列表里的坐标为每个云加载位置
            self.clouds_size_list[i][0] -= self.clouds_speed_list[i]  # 云朵左移，也就是坐标减去速度
            if self.clouds_size_list[i][0] < -200:  # 如果云朵的位置左移出了屏幕
                self.clouds_size_list[i][0] = 1280  # 就重新调整云朵的位置到屏幕右边的界面外，相当于重新移动到了界面外地方然后重新左移
                self.clouds_speed_list[i] = random.randint(1, 3)  # 不仅重置坐标还重置云朵的速度，显得不会那么死板

    def render_plane(self):
        # 玩家操控飞机
        if self.key_list[pygame.K_d]:
            if self.plane_size[0] + self.plane.get_rect()[2] < 1280:  # 如果触碰到右边界就不再移动
                self.plane_size[0] += 2
                self.plane = self.plane_right
        if self.key_list[pygame.K_a]:
            if self.plane_size[0] > 0:  # 如果触碰到左边界就不再移动
                self.plane_size[0] -= 2
                self.plane = self.plane_left
        if self.key_list[pygame.K_w]:
            if self.plane_size[1] > 0:  # 如果触碰到上边界就不再移动
                self.plane_size[1] -= 2
        if self.key_list[pygame.K_s]:
            if self.plane_size[1] + self.plane.get_rect()[3] < 720:  # 如果触碰到下边界就不再移动
                self.plane_size[1] += 2
        self.screen.blit(self.plane, (self.plane_size[0], self.plane_size[1]))  # 绘制飞机
        # pygame.draw.rect(self.plane, (255, 255, 255), (0, 0, self.plane.get_rect()[2], self.plane.get_rect()[3]), 1)  # 为飞机绘制一个矩形边框用来做测试

    def render_car(self, car_y=None):
        # 玩家操控汽车
        if self.key_list[pygame.K_d]:
            if self.car_size[0] + self.car.get_rect()[2] < 1280:  # 如果触碰到右边界就不再移动
                self.car_size[0] += 2
                self.car = self.car_right
        if self.key_list[pygame.K_a]:
            if self.car_size[0] > 0:  # 如果触碰到左边界就不再移动
                self.car_size[0] -= 2
                self.car = self.car_left
        if car_y:
            self.screen.blit(self.car, (self.car_size[0], car_y))  # 绘制汽车
        else:
            self.screen.blit(self.car, (self.car_size[0], self.car_size[1]))  # 绘制汽车

    def play_music(self, music_name):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(music_name)
            pygame.mixer.music.play()

App()