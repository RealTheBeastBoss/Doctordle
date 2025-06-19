import pygame
import random
from episode import *
import os

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
DEBUG = True
FONT = pygame.font.Font(os.path.join("Doctordle", "beastboss_font.ttf"), 90)
pygame.display.set_caption("Doctordle")

LOGO = pygame.image.load(os.path.join("Doctordle", "logo.png"))

EPISODE_LIST = [Episode("S01x01", "Rose", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Keith Boak", 8),
                Episode("S01x02", "The End of the World", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Euros Lyn", 8.25),
                Episode("S01x03", "The Unquiet Dead", 1, "9th Doctor", "RTD1", ["Mark Gatiss"], "Keith Boak", 7.5),
                Episode("S01x04", "Aliens of London", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Keith Boak", 7),
                Episode("S01x05", "World War Three", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Keith Boak", 8),
                Episode("S01x06", "Dalek", 1, "9th Doctor", "RTD1", ["Robert Shearman"], "Joe Ahearne", 8.5),
                Episode("S01x07", "The Long Game", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Brian Grant", 6.5),
                Episode("S01x08", "Father's Day", 1, "9th Doctor", "RTD1", ["Paul Cornell"], "Joe Ahearne", 10),
                Episode("S01x09", "The Empty Child", 1, "9th Doctor", "RTD1", ["Steven Moffat"], "James Hawes", 7.5),
                Episode("S01x10", "The Doctor Dances", 1, "9th Doctor", "RTD1", ["Steven Moffat"], "James Hawes", 9),
                Episode("S01x11", "Boom Town", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Joe Ahearne", 7.5),
                Episode("S01x12", "Bad Wolf", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Joe Ahearne", 9),
                Episode("S01x13", "The Parting of the Ways", 1, "9th Doctor", "RTD1", ["Russell T Davies"], "Joe Ahearne", 10)]
CORRECT_EPISODE = EPISODE_LIST[random.randint(0, len(EPISODE_LIST) - 1)]
ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_QUESTION, pygame.K_SPACE, pygame.K_RETURN, pygame.K_QUOTE]

class Doctordle:
    guessed_episodes = []
    current_search = ""
    search_index = 0
    search_list = []
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)