import pygame
import os

# menu images
MENU = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        # transform pictures scale
        self.menu = pygame.transform.scale(MENU, (200, 200))
        self.upgrade = pygame.transform.scale(UPGRADE, (80, 40))
        self.sell = pygame.transform.scale(SELL, (60, 50))
        # create rect
        self.menu_rect = self.menu.get_rect()
        self.upgrade_rect = self.upgrade.get_rect()
        self.sell_rect = self.sell.get_rect()
        # Set center coordinates for rect
        self.menu_rect.center = (x, y)
        self.upgrade_rect.center = (x, y - 72)
        self.sell_rect.center = (x, y + 75)
        # button list, including self.upgrade and self.sell button
        self.__buttons = [Button(self.upgrade, 'upgrade', self.upgrade_rect.center[0], self.upgrade_rect.center[1]),
                          Button(self.sell, 'sell', self.sell_rect.center[0], self.sell_rect.center[1])]

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu, self.menu_rect)
        # draw button
        win.blit(self.upgrade, self.upgrade_rect)
        win.blit(self.sell, self.sell_rect)

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons

class Button:

    def __init__(self, image, name, x, y):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()    # create rect
        self.rect.center = (x, y)            # Set center coordinates for rect


    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # check if the mouse is within the rect
        return True if self.rect.collidepoint(x, y) else False


    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






