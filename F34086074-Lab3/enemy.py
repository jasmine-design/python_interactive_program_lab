import pygame
import math
import os
from settings import PATH, RED, GREEN

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

class Enemy:

    def __init__(self, path_num):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.max_health_width = 40       # The size of the health bar
        self.max_health_height = 5       # The size of the health bar
        self.path = PATH[path_num]  # determine which path to attack
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[self.path_index]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # per health width
        health_per_width = self.max_health_width / self.max_health
        # remaining health width
        remaining_health_width = health_per_width * self.health
        # losing health width
        losing_health_width = health_per_width * (self.max_health - self.health)
        # draw health bar
        pygame.draw.rect(win, GREEN, [self.x - 20, self.y - 35,
                                      remaining_health_width, self.max_health_height])
        pygame.draw.rect(win, RED, [self.x - 20 + remaining_health_width, self.y - 35,
                                    losing_health_width, self.max_health_height])


    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        stride = 1
        ax, ay = self.path[self.path_index]  # x, y position of point A
        bx, by = self.path[self.path_index + 1] # x, y position of point B
        distance_A_B = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        max_count = int(distance_A_B / stride)  # total footsteps that needed from A to B

        if self.move_count < max_count:
            unit_vector_x = (bx - ax) / distance_A_B
            unit_vector_y = (by - ay) / distance_A_B
            delta_x = unit_vector_x * stride
            delta_y = unit_vector_y * stride
            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1

        else:
            self.move_count = 0
            self.path_index += 1


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = []
        self.path_choice = '2'

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        if self.gen_count >= self.gen_period and not self.is_empty():
            self.expedition.append(self.reserved_members.pop())
            self.gen_count = 0

        else:
            self.gen_count += 1
            print(self.gen_count)


    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # determine which path to attack
        if self.path_choice == '1':
            path_num = '2'
            self.path_choice = '2'
        else:
            path_num = '1'
            self.path_choice = '1'

        for i in range(num):
            self.reserved_members.append(Enemy(path_num))

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





