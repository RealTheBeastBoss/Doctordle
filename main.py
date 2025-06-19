from doctordle import *
from sys import exit

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.VIDEORESIZE:
            Doctordle.width = event.w
            Doctordle.height = event.h
            Doctordle.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key in ALLOWED_KEYS:
                if event.key == pygame.K_BACKSPACE:
                    Doctordle.current_search = Doctordle.current_search[:-1]
                    update_search_list()
                elif event.key == pygame.K_RETURN and len(Doctordle.search_list) > 0:
                    Doctordle.current_search = ""
                    print("Guessed Episode: " + Doctordle.search_list[Doctordle.search_index].title)
                    Doctordle.guessed_episodes.append(Doctordle.search_list[Doctordle.search_index])
                    Doctordle.search_index = 0
                    Doctordle.search_list.clear()
                elif event.key != pygame.K_RETURN:
                    Doctordle.current_search += event.unicode
                    update_search_list()
            elif event.key == pygame.K_UP:
                Doctordle.search_index -= 1
                if Doctordle.search_index == -1:
                    Doctordle.search_index = len(Doctordle.search_list) - 1
            elif event.key == pygame.K_DOWN:
                Doctordle.search_index += 1
                if Doctordle.search_index == len(Doctordle.search_list):
                    Doctordle.search_index = 0

def draw_window():
    # Draw Background:
    Doctordle.screen.fill((100, 100, 100))
    # Add Logo:
    logo = pygame.transform.scale(LOGO, (2167 // 4, 402 // 4))
    Doctordle.screen.blit(logo, ((Doctordle.width // 2) - 270, 40))
    # Draw Search Bar:
    draw_text("Guess a Doctor Who Episode:", (Doctordle.width // 2, 170), "Black", 3)
    search_rect = pygame.rect.Rect(((Doctordle.width // 2) - 300, 200), (600, 60))
    pygame.draw.rect(Doctordle.screen, "White", search_rect, 0, 10)
    pygame.draw.rect(Doctordle.screen, "Black", search_rect, 10, 10)
    draw_text(Doctordle.current_search, (Doctordle.width // 2, 230), "Black", 3.5)
    if len(Doctordle.search_list) > 0:
        draw_text(Doctordle.search_list[Doctordle.search_index].code + " - " + Doctordle.search_list[Doctordle.search_index].title, (Doctordle.width // 2, 280), "Black", 3.5)

def draw_text(text, pos, colour, scale):
    text_surface = FONT.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if scale != 1:
        text_surface = pygame.transform.scale(text_surface, (text_width // scale, text_height // scale))
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
    Doctordle.screen.blit(text_surface, (pos[0] - (text_width // 2), pos[1] - (text_height // 2)))

def update_search_list():
    Doctordle.search_list.clear()
    Doctordle.search_index = 0
    for episode in EPISODE_LIST:
        if Doctordle.current_search.lower() in episode.code.lower() or Doctordle.current_search.lower() in episode.title.lower():
            Doctordle.search_list.append(episode)

if __name__ == "__main__":
    print("Correct Episode: " + CORRECT_EPISODE.title)
    while True:
        event_handler()
        draw_window()
        pygame.display.flip()
        CLOCK.tick(FPS)