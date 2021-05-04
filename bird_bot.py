import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("resource", "img", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("resource", "img", "bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("resource", "img", "bird3.png")))]
