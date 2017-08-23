import pygame as pg
import sys

class GraphicUtility():
    def __init__(self, title, env, grid_pixel=150, img_rate=0.5):
        # 한 칸당 픽셀 수와 개수
        self.grid_pixel = grid_pixel
        self.grid_size = env.grid_size

        # 한 칸안의 이미지 비율
        self.img_rate = img_rate

        # 스크린 초기화
        self.screen = self._screen_init(title)

        # 이미지 딕셔너리 ('unit', 'obstacle', 'goal')
        self.images_dict = self._image_load()

    def _screen_init(self, title):
        pg.init()

        screen_size = self.grid_size * self.grid_pixel
        screen = pg.display.set_mode((screen_size, screen_size), 0, 32)
        pg.display.set_caption(title)

        return screen

    def _image_load(self):
        unit_img = pg.image.load('../img/rectangle.png')
        obstacle_img = pg.image.load('../img/triangle.png')
        goal_img = pg.image.load('../img/circle.png')

        img_size = int(self.grid_pixel * (1.0 - self.img_rate))

        unit = pg.transform.scale(unit_img, (img_size, img_size))
        obstacle = pg.transform.scale(obstacle_img, (img_size, img_size))
        goal = pg.transform.scale(goal_img, (img_size, img_size))

        images = {'unit': unit,
                  'obstacle': obstacle,
                  'goal': goal}

        return images

    def _draw_img(self, image, coord):
        # 좌표 지점과 padding(0.4)을 더하고 곱하면 이미지 좌표
        x = (coord[0] + (self.img_rate / 2)) * self.grid_pixel
        y = (coord[1] + (self.img_rate / 2)) * self.grid_pixel

        self.screen.blit(image, (x, y))

    def render(self, env):

        # 배경화면 그리기
        width, height = pg.display.get_surface().get_size()

        pg.draw.rect(self.screen, (255, 255, 255),
                     pg.Rect(0, 0, width, height))

        # 라인 그리기
        for n in range(self.grid_size):
            # 왼쪽 선 그리기 |
            pg.draw.line(self.screen, (0, 0, 0),
                         (0, n * self.grid_pixel), (width-1, n * self.grid_pixel))
            # 위쪽 선 그리기 ㅡ
            pg.draw.line(self.screen, (0, 0, 0),
                         (n * self.grid_pixel, 0), (n * self.grid_pixel, height-1))  # 위쪽 선 그리기 ㅡ

        # 유닛, 장애물, 목표 그리기
        for coord in env.coord['obstacle']:
            self._draw_img(self.images_dict['obstacle'], coord)

        self._draw_img(self.images_dict['goal'], env.coord['goal'])
        self._draw_img(self.images_dict['unit'], env.coord['unit'])


        pg.display.flip()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_i:
                    pass