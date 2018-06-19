#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
ساخته شده در ۸ امرداد ۱۳۹۵ ساعت ۱۰:۳۷
پایان در ۸ امرداد ۱۳۹۵ ساعت ۲۲:۰۰
Created on Jul 29, 2016

@author: sajedrakhshani
'''
# ***************************License:***********************************
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Author: Sajed Rakhshani
# E-mail: SajedRakhshani@msn.com
# gitlab: https://gitlab.com/sajed68/circle-clock-widget
# Start: 13 Mehr 1396
# First Release 13 Mehr 1396
# Third Release 24 Aban 1396
# version 2.0.1
# Release date: 28 Aban
# #####################################################


import pygame
import random
import numpy as np

pygame.init()
pygame.display.set_caption('Snake v 1')
screen = pygame.display.set_mode((640, 480))  # I set Screen size
background = pygame.Surface(screen.get_size())
background.fill((70, 70, 70))
background = background.convert()
screen.blit(background, (0,0))
clock = pygame.time.Clock()  # this is a clock
SNAKE_PLANE = pygame.Surface(screen.get_size())
SNAKE_PLANE.set_colorkey((0, 0, 0))
main_loop = True
FPS = 15  # change frame rate for velocity of Snake 



## Create Snake Object: ###############################################
class snake(object):
    '''
    help : ?
    '''
    __grow_num__ = 0
    def __init__(self):
        self.points = [(32, 21), (33, 21), (33,21)]
        self.stack_pos = ['s', 'd', 'd', 'e']
        self.__score__ = len(self.points) - 3
        self.__draw__()
        self.direction = 'left'
        self.length = len(self.points)
        self.crash = False
        self.grid = []
        self.__grow_num__ = 0
        for i in range(64):
            for j in range(48):
                self.grid.append((i, j))
        self.point_coor = None
        self.__create_point__()
        
        
    def __grow_up__(self):
        if snake.__grow_num__ > 0:
            x1, y1 = self.points[-1]
            x0, y0 = self.points[-2]
            if x1 == x0 and y1 == y0 + 1:
                x = x1
                y = y1 - 1
            elif x1 == x0 and y1 == y0 - 1:
                x = x1
                y = y1  + 1
            elif y1 == y0 and x1 == x0 + 1:
                x = x1 - 1
                y = y1
            elif y1 == y0 and x1 == x0 - 1:
                x = x1 + 1
                y = y1
            self.points.append((x, y))

            snake.__grow_num__ -= 1
            # print ((x1, y1), (x0, y0), (x, y))
            
    def __draw__(self):
        global SNAKE_PLANE
        SNAKE_PLANE = pygame.Surface(screen.get_size())
        SNAKE_PLANE.set_colorkey((0, 0, 0))
        self.__grow_up__()
        for point in self.points:
            x, y = point
            pygame.draw.rect(SNAKE_PLANE, (255, 255, 255), (x*10, y*10, 10, 10))
        font = pygame.font.SysFont('ArcadeClassic', size=20)
        text = 'score ' + str(self.__score__)
        txt = font.render(text, True, (211, 211, 211))
        SNAKE_PLANE.blit(txt, (20, 20))
        SNAKE_PLANE = SNAKE_PLANE.convert()
        
    def __crash_check__(self):
        start_point = self.points[0]
        if self.points.count(start_point) != 1:
            self.crash = True
            # print ('Crash')
        x, y = start_point
        if x < 0 or y < 0 or x > 63 or y > 47:
            self.crash = True
            # print ('Crash')
        
    def __move_left__(self):
        start_x, start_y = self.points[0]
        next_x, next_y = self.points[1]
        if start_y == next_y and start_x == next_x + 1:
            go_x = start_x
            go_y = start_y
            self.__move_down__()
        else:
            go_x = start_x - 1
            go_y = start_y
            length = len(self.points)
            for i in range(length):
                if i != length - 1:
                    self.points[length - 1 - i] = self.points[length - 2 - i]
                else:
                    self.points[0] = (go_x, go_y)
       
        self.__draw__()
        
    def __move_up__(self):
        start_x, start_y = self.points[0]
        next_x, next_y = self.points[1]
        if start_x == next_x and start_y == next_y + 1:
            go_x = start_x
            go_y = start_y
            self.__move_right__()
        else:
            go_x = start_x
            go_y = start_y - 1
            length = len(self.points)
            for i in range(length):
                if i != length - 1:
                    self.points[length - 1 - i] = self.points[length - 2 - i]
                else:
                    self.points[0] = (go_x, go_y)
       
        self.__draw__()
        
    def __move_right__(self):
        start_x, start_y = self.points[0]
        next_x, next_y = self.points[1]
        if start_y == next_y and start_x == next_x - 1:
            go_x = start_x
            go_y = start_y
            self.__move_up__()
        else:
            go_x = start_x + 1
            go_y = start_y
            length = len(self.points)
            for i in range(length):
                if i != length - 1:
                    self.points[length - 1 - i] = self.points[length - 2 - i]
                else:
                    self.points[0] = (go_x, go_y)
       
        self.__draw__()

    def __move_down__(self):
        start_x, start_y = self.points[0]
        next_x, next_y = self.points[1]
        if start_x == next_x and start_y == next_y - 1:
            go_x = start_x
            go_y = start_y
            self.__move_left__()
        else:
            go_x = start_x
            go_y = start_y + 1
            length = len(self.points)
            for i in range(length):
                if i != length - 1:
                    self.points[length - 1 - i] = self.points[length - 2 - i]
                else:
                    self.points[0] = (go_x, go_y)
       
        self.__draw__()
        


    def __create_point__(self):
        grid = self.grid[0:]
        for p in self.points:
            try:
                grid.remove(p)
            except:
                pass
        x, y = grid[random.randint(0,len(grid)-1)]
        self.point_putted = True
        self.point_coor = (x * 10, y * 10, 10, 10)
        pygame.draw.rect(SNAKE_PLANE, (0, 0, 0), self.point_coor)
            
    def __get_bounce_check__(self):
        point = (self.point_coor[0]/10, self.point_coor[1]/10)
        if self.points[0] == point:
            # print ('got a bounce...')
            self.__create_point__()
            snake.__grow_num__ = snake.__grow_num__ + 1
            
    
    def update(self, direction):
        if self.crash is False:
            self.__score__ = len(self.points) - 3
            direction = self.direction if direction == None else direction
            if direction == 'down':
                self.__move_down__()
            elif direction == 'left':
                self.__move_left__()
            if direction == 'right':
                self.__move_right__()
            elif direction == 'up':
                self.__move_up__()
            elif direction == 'paused':
                pass
            self.direction = direction if direction != 'paused' else self.direction
            # self.__create_point()
            pygame.draw.rect(SNAKE_PLANE, (255, 255, 255), self.point_coor)
            self.__get_bounce_check__()
            self.__crash_check__()
        
def main_game():
    Snake = snake()
    direction = 'left'
    main_loop = True
    #k = 1
    Q = np.zeros((4, 4))
    while main_loop:
        clock.tick(FPS)
        for event in pygame.event.get():
                if event.type is pygame.QUIT:   # for press (x) sign top of window 
                    main_loop = False
                elif event.type is pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        direction = 'left'
                    if event.key == pygame.K_w:
                        direction = 'up'
                    if event.key == pygame.K_s:
                        direction = 'down'
                    if event.key == pygame.K_d:
                        direction = 'right'
                    if event.key == pygame.K_p:
                        direction = 'pause'

        Snake.update(direction)
        screen.blit(background, (0,0))
        screen.blit(SNAKE_PLANE, (0,0))
        pygame.display.flip()
        #pygame.image.save(screen, str(k) + '.jpg')
        #k += 1
        if Snake.crash:
            return 0
        
        
if __name__ == '__main__':
    out = None
    while main_loop:
        milliseconds = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:   # for press (x) sign top of window 
                main_loop = False
            elif event.type is pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    out = main_game()
        if out is None:
            pygame.draw.rect(SNAKE_PLANE, (255, 255, 255), (150, 120, 340, 240))
            SNAKE_PLANE = SNAKE_PLANE.convert()
            font = pygame.font.SysFont('ArcadeClassic', size=25)
            txt = font.render('Press Enter to Start game', True, (0, 0, 0))
            SNAKE_PLANE.blit(txt, (160, 150))
            txt = font.render('or red (x) to close', True, (0, 0, 0))
            SNAKE_PLANE.blit(txt, (160, 180))
            txt = font.render('use w s a d to direction', True, (0, 0, 0))
            SNAKE_PLANE.blit(txt, (160, 210))
            font = pygame.font.SysFont('ArcadeClassic', size=20)
            txt = font.render('P to Pause  Return to Restart game', True, (0, 0, 0))
            SNAKE_PLANE.blit(txt, (160, 240))
        screen.blit(background, (0,0))
        screen.blit(SNAKE_PLANE, (0,0))
        pygame.display.flip()
        
