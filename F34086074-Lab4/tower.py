import pygame
import os
import math
from settings import WIN_WIDTH, WIN_HEIGHT

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        """
        check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """
        # detect the distance between the enemy and the tower
        x1, y1 = enemy.get_pos()
        distance = math.sqrt((x1 - self.center[0]) ** 2 + (y1 - self.center[1]) ** 2)

        if distance < self.radius:
            return True
        else:
            return False


    def draw_transparent(self, win):
        """
        draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
        # draw transparent circles
        transparency = 50  # define transparency (0~255, 0 is fully transparent)
        transparent_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(transparent_surface, (255, 255, 255, transparency), self.center, self.radius)
        win.blit(transparent_surface, (0, 0))

class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()60
        self.is_selected = False  # the state of whether the tower is selected
        self.type = "tower"
        self.is_clicked_range = 40  # acceptable tower defense error


    def is_cool_down(self):
        """
        Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down
        :return: Bool
        """
        if self.cd_count < self.cd_max_count:  # still in cool down mode
            self.cd_count += 1
            return False
        else:                                  # complete cool down mode
            self.cd_count = 0
            return True


    def attack(self, enemy_group):
        """
        Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: Nonen
        """
        if self.is_cool_down():                       # check out if cool down mode is complete
            for enemy in enemy_group.get():           # get one enemy in each loop
                if self.range_circle.collide(enemy):  # check out if the enemy is in attack range
                    enemy.get_hurt(self.damage)       # attack enemy
                    return


    def is_clicked(self, x, y):
        """
        Return whether the tower is clicked
        (1) If the mouse position is in the tower image(self.rect.center) range(self.is_clicked_range), return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        if abs(self.rect.center[0] - x) < self.is_clicked_range \
                and abs(self.rect.center[1] - y) < self.is_clicked_range:  # check out if (x, y) is on tower image
            return True
        else:
            return False


    def get_selected(self, is_selected):
        """
        Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected


    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower



