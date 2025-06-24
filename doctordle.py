import pygame
import random
from episode import *

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
DEBUG = True
FONT = pygame.font.Font("beastboss_font.ttf", 90)
pygame.display.set_caption("Doctordle")

LOGO = pygame.image.load("logo.png")

SERIES_NAMES = {
    1: "Series One",
    2: "Series Two",
    3: "Series Three",
    4: "Series Four",
    5: "Series Five",
    6: "Series Six",
    7: "Series Seven",
    8: "Series Eight",
    9: "Series Nine",
    10: "Series Ten",
    11: "Series Eleven",
    12: "Series Twelve",
    13: "Series Thirteen",
    14: "60th",
    15: "Season One",
    16: "Season Two"
}

EPISODE_LIST = [Episode("S01x01", "Rose", 1, "9th Doctor", "RTD1", "Russell T Davies", "Keith Boak", 8),
                Episode("S01x02", "The End of the World", 1, "9th Doctor", "RTD1", "Russell T Davies", "Euros Lyn", 8.25),
                Episode("S01x03", "The Unquiet Dead", 1, "9th Doctor", "RTD1", "Mark Gatiss", "Keith Boak", 7.5),
                Episode("S01x04", "Aliens of London", 1, "9th Doctor", "RTD1", "Russell T Davies", "Keith Boak", 7),
                Episode("S01x05", "World War Three", 1, "9th Doctor", "RTD1", "Russell T Davies", "Keith Boak", 8),
                Episode("S01x06", "Dalek", 1, "9th Doctor", "RTD1", "Robert Shearman", "Joe Ahearne", 8.5),
                Episode("S01x07", "The Long Game", 1, "9th Doctor", "RTD1", "Russell T Davies", "Brian Grant", 6.5),
                Episode("S01x08", "Father's Day", 1, "9th Doctor", "RTD1", "Paul Cornell", "Joe Ahearne", 10),
                Episode("S01x09", "The Empty Child", 1, "9th Doctor", "RTD1", "Steven Moffat", "James Hawes", 7.5),
                Episode("S01x10", "The Doctor Dances", 1, "9th Doctor", "RTD1", "Steven Moffat", "James Hawes", 9),
                Episode("S01x11", "Boom Town", 1, "9th Doctor", "RTD1", "Russell T Davies", "Joe Ahearne", 7.5),
                Episode("S01x12", "Bad Wolf", 1, "9th Doctor", "RTD1", "Russell T Davies", "Joe Ahearne", 9),
                Episode("S01x13", "The Parting of the Ways", 1, "9th Doctor", "RTD1", "Russell T Davies", "Joe Ahearne", 10),
                Episode("S02x00", "The Christmas Invasion", 2, "10th Doctor", "RTD1", "Russell T Davies", "James Hawes", 8),
                Episode("S02x01", "New Earth", 2, "10th Doctor", "RTD1", "Russell T Davies", "James Hawes", 7.5),
                Episode("S02x02", "Tooth and Claw", 2, "10th Doctor", "RTD1", "Russell T Davies", "Euros Lyn", 7.5),
                Episode("S02x03", "School Reunion", 2, "10th Doctor", "RTD1", "Toby Whithouse", "James Hawes", 8),
                Episode("S02x04", "The Girl in the Fireplace", 2, "10th Doctor", "RTD1", "Steven Moffat", "Euros Lyn", 10),
                Episode("S02x05", "Rise of the Cybermen", 2, "10th Doctor", "RTD1", "Tom McRae", "Graeme Harper", 7.75),
                Episode("S02x06", "The Age of Steel", 2, "10th Doctor", "RTD1", "Tom McRae", "Graeme Harper", 7.75),
                Episode("S02x07", "The Idiot's Lantern", 2, "10th Doctor", "RTD1", "Mark Gatiss", "Euros Lyn", 7),
                Episode("S02x08", "The Impossible Planet", 2, "10th Doctor", "RTD1", "Matt Jones", "James Strong", 6.5),
                Episode("S02x09", "The Satan Pit", 2, "10th Doctor", "RTD1", "Matt Jones", "James Strong", 6.25),
                Episode("S02x10", "Love and Monsters", 2, "10th Doctor", "RTD1", "Russell T Davies", "Dan Zeff", 5.75),
                Episode("S02x11", "Fear Her", 2, "10th Doctor", "RTD1", "Matthew Graham", "Euros Lyn", 6.75),
                Episode("S02x12", "Army of Ghosts", 2, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 8.5),
                Episode("S02x13", "Doomsday", 2, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 9),
                Episode("S03x00", "The Runaway Bride", 3, "10th Doctor", "RTD1", "Russell T Davies", "Euros Lyn", 9.25),
                Episode("S03x01", "Smith & Jones", 3, "10th Doctor", "RTD1", "Russell T Davies", "Charles Palmer", 8.5),
                Episode("S03x02", "The Shakespeare Code", 3, "10th Doctor", "RTD1", "Gareth Roberts", "Charles Palmer", 8),
                Episode("S03x03", "Gridlock", 3, "10th Doctor", "RTD1", "Russell T Davies", "Richard Clark", 7.25),
                Episode("S03x04", "Daleks in Manhattan", 3, "10th Doctor", "RTD1", "Helen Raynor", "James Strong", 5.5),
                Episode("S03x05", "Evolution of the Daleks", 3, "10th Doctor", "RTD1", "Helen Raynor", "James Strong", 5),
                Episode("S03x06", "The Lazarus Experiment", 3, "10th Doctor", "RTD1", "Stephen Greenhorn", "Richard Clark", 7.75),
                Episode("S03x07", "42", 3, "10th Doctor", "RTD1", "Chris Chibnall", "Graeme Harper", 9.75),
                Episode("S03x08", "Human Nature", 3, "10th Doctor", "RTD1", "Paul Cornell", "Charles Palmer", 10),
                Episode("S03x09", "The Family of Blood", 3, "10th Doctor", "RTD1", "Paul Cornell", "Charles Palmer", 10),
                Episode("S03x10", "Blink", 3, "10th Doctor", "RTD1", "Steven Moffat", "Hettie MacDonald", 10),
                Episode("S03x11", "Utopia", 3, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 9.25),
                Episode("S03x12", "The Sound of Drums", 3, "10th Doctor", "RTD1", "Russell T Davies", "Colin Teague", 8.5),
                Episode("S03x13", "The Last of the Time Lords", 3, "10th Doctor", "RTD1", "Russell T Davies", "Colin Teague", 7.5),
                Episode("S04x00", "Voyage of the Damned", 4, "10th Doctor", "RTD1", "Russell T Davies", "James Strong", 9.75),
                Episode("S04x01", "Partners in Crime", 4, "10th Doctor", "RTD1", "Russell T Davies", "James Strong", 9),
                Episode("S04x02", "The Fires of Pompeii", 4, "10th Doctor", "RTD1", "James Moran", "Colin Teague", 8.75),
                Episode("S04x03", "Planet of the Ood", 4, "10th Doctor", "RTD1", "Keith Temple", "Graeme Harper", 7.5),
                Episode("S04x04", "The Sontaran Stratagem", 4, "10th Doctor", "RTD1", "Helen Raynor", "Douglas MacKinnon", 8.5),
                Episode("S04x05", "The Poison Sky", 4, "10th Doctor", "RTD1", "Helen Raynor", "Douglas MacKinnon", 8.5),
                Episode("S04x06", "The Doctor's Daughter", 4, "10th Doctor", "RTD1", "Stephen Greenhorn", "Alice Troughton", 7),
                Episode("S04x07", "The Unicorn and the Wasp", 4, "10th Doctor", "RTD1", "Gareth Roberts", "Graeme Harper", 10),
                Episode("S04x08", "Silence in the Library", 4, "10th Doctor", "RTD1", "Steven Moffat", "Euros Lyn", 10),
                Episode("S04x09", "Forest of the Dead", 4, "10th Doctor", "RTD1", "Steven Moffat", "Euros Lyn", 10),
                Episode("S04x10", "Midnight", 4, "10th Doctor", "RTD1", "Russell T Davies", "Alice Troughton", 10),
                Episode("S04x11", "Turn Left", 4, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 10),
                Episode("S04x12", "The Stolen Earth", 4, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 9),
                Episode("S04x13", "Journey's End", 4, "10th Doctor", "RTD1", "Russell T Davies", "Graeme Harper", 10),
                Episode("S04x14", "The Next Doctor", 4, "10th Doctor", "RTD1", "Russell T Davies", "Andy Goddard", 8),
                Episode("S04x15", "Planet of the Dead", 4, "10th Doctor", "RTD1", "Gareth Roberts", "James Strong", 8.5),
                Episode("S04x16", "The Waters of Mars", 4, "10th Doctor", "RTD1", "Phil Ford", "Graeme Harper", 10),
                Episode("S04x17", "The End of Time Part One", 4, "10th Doctor", "RTD1", "Russell T Davies", "Euros Lyn", 9),
                Episode("S04x18", "The End of Time Part Two", 4, "10th Doctor", "RTD1", "Russell T Davies", "Euros Lyn", 10),
                Episode("S05x01", "The Eleventh Hour", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Adam Smith", 10),
                Episode("S05x02", "The Beast Below", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Andrew Gunn", 8),
                Episode("S05x03", "Victory of the Daleks", 5, "11th Doctor", "The Grand Moff", "Mark Gatiss", "Andrew Gunn", 7.75),
                Episode("S05x04", "The Time of Angels", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Adam Smith", 7),
                Episode("S05x05", "Flesh and Stone", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Adam Smith", 6),
                Episode("S05x06", "The Vampires of Venice", 5, "11th Doctor", "The Grand Moff", "Toby Whithouse", "Jonny Campbell", 8),
                Episode("S05x07", "Amy's Choice", 5, "11th Doctor", "The Grand Moff", "Simon Nye", "Catherine Morshead", 10),
                Episode("S05x08", "The Hungry Earth", 5, "11th Doctor", "The Grand Moff", "Chris Chibnall", "Ashley Way", 6.5),
                Episode("S05x09", "Cold Blood", 5, "11th Doctor", "The Grand Moff", "Chris Chibnall", "Ashley Way", 7),
                Episode("S05x10", "Vincent and the Doctor", 5, "11th Doctor", "The Grand Moff", "Richard Curtis", "Jonny Campbell", 10),
                Episode("S05x11", "The Lodger", 5, "11th Doctor", "The Grand Moff", "Gareth Roberts", "Catherine Morshead", 7.5),
                Episode("S05x12", "The Pandorica Opens", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Toby Haynes", 8),
                Episode("S05x13", "The Big Bang", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Toby Haynes", 9.5),
                Episode("S05x14", "A Christmas Carol", 5, "11th Doctor", "The Grand Moff", "Steven Moffat", "Toby Haynes", 10),
                Episode("S06x01", "The Impossible Astronaut", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Toby Haynes", 8),
                Episode("S06x02", "Day of the Moon", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Toby Haynes", 8.5),
                Episode("S06x03", "The Curse of the Black Spot", 6, "11th Doctor", "The Grand Moff", "Steve Thompson", "Jeremy Webb", 8),
                Episode("S06x04", "The Doctor's Wife", 6, "11th Doctor", "The Grand Moff", "Neil Gaiman", "Richard Clark", 10),
                Episode("S06x05", "The Rebel Flesh", 6, "11th Doctor", "The Grand Moff", "Matthew Graham", "Julian Simpson", 8.75),
                Episode("S06x06", "The Almost People", 6, "11th Doctor", "The Grand Moff", "Matthew Graham", "Julian Simpson", 9),
                Episode("S06x07", "A Good Man Goes to War", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Peter Hoar", 9),
                Episode("S06x08", "Let's Kill Hitler", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Richard Senior", 7.5),
                Episode("S06x09", "Night Terrors", 6, "11th Doctor", "The Grand Moff", "Mark Gatiss", "Richard Clark", 6.5),
                Episode("S06x10", "The Girl Who Waited", 6, "11th Doctor", "The Grand Moff", "Tom McRae", "Nick Hurran", 8.75),
                Episode("S06x11", "The God Complex", 6, "11th Doctor", "The Grand Moff", "Toby Whithouse", "Nick Hurran", 10),
                Episode("S06x12", "Closing Time", 6, "11th Doctor", "The Grand Moff", "Gareth Roberts", "Steve Hughes", 6),
                Episode("S06x13", "The Wedding of River Song", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Jeremy Webb", 6.5),
                Episode("S06x14", "The Doctor, the Widow, and the Wardrobe", 6, "11th Doctor", "The Grand Moff", "Steven Moffat", "Farren Blackburn", 6)
                ]
CORRECT_EPISODE = EPISODE_LIST[random.randint(0, len(EPISODE_LIST) - 1)]
ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                pygame.K_BACKSPACE, pygame.K_COMMA, pygame.K_QUESTION, pygame.K_SPACE, pygame.K_RETURN, pygame.K_QUOTE]

class Doctordle:
    guessed_episodes = []
    current_search = ""
    search_index = 0
    text_surfaces = []
    search_list = []
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)