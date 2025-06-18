from game import *
from sys import exit

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


if __name__ == "__main__":
    while True:
        event_handler()
        pygame.display.flip()
        CLOCK.tick(FPS)