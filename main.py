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
            Doctordle.text_surfaces.clear()
            for episode in Doctordle.guessed_episodes:
                add_text_surface(episode)
        elif event.type == pygame.KEYDOWN:
            if event.key in ALLOWED_KEYS:
                if event.key == pygame.K_BACKSPACE:
                    Doctordle.current_search = Doctordle.current_search[:-1]
                    update_search_list()
                elif event.key == pygame.K_RETURN and len(Doctordle.search_list) > 0 and Doctordle.search_list[Doctordle.search_index] not in Doctordle.guessed_episodes:
                    Doctordle.current_search = ""
                    episode = Doctordle.search_list[Doctordle.search_index]
                    Doctordle.guessed_episodes.append(episode)
                    add_text_surface(episode)
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
    # Draw Logo:
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
    # Draw Guessed Episodes:
    draw_text("---------", (Doctordle.width // 2, 300), "Black", 1)
    for text in Doctordle.text_surfaces:
        Doctordle.screen.blit(text[0], (text[1], text[2]))

def draw_text(text, pos, colour, scale):
    text_surface = FONT.render(text, True, colour)
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    if scale != 1:
        text_surface = pygame.transform.scale(text_surface, (text_width // scale, text_height // scale))
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
    Doctordle.screen.blit(text_surface, (pos[0] - (text_width // 2), pos[1] - (text_height // 2)))

def add_text_surface(episode):
    title_colour = "Black"
    series_colour = "Black"
    doctor_colour = "Black"
    era_colour = "Black"
    writer_colour = "Black"
    director_colour = "Black"
    rating_colour = "Black"
    rating_words = str(episode.rating)
    series_words = SERIES_NAMES[episode.series]
    if episode.title == CORRECT_EPISODE.title:
        title_colour = "Green"
    if episode.series == CORRECT_EPISODE.series:
        series_colour = "Green"
    elif episode.series > CORRECT_EPISODE.series:
        series_words += " \/"
    else:
        series_words += " /\\"
    if episode.doctor == CORRECT_EPISODE.doctor:
        doctor_colour = "Green"
    if episode.era == CORRECT_EPISODE.era:
        era_colour = "Green"
    if episode.writer == CORRECT_EPISODE.writer:
        writer_colour = "Green"
    if episode.director == CORRECT_EPISODE.director:
        director_colour = "Green"
    if episode.rating == CORRECT_EPISODE.rating:
        rating_colour = "Green"
    elif CORRECT_EPISODE.rating - 1 <= episode.rating <= CORRECT_EPISODE.rating + 1:
        rating_colour = "Orange"
    if episode.rating > CORRECT_EPISODE.rating:
        rating_words += " \/"
    elif episode.rating < CORRECT_EPISODE.rating:
        rating_words += " /\\"
    title_text = FONT.render(episode.code + " - " + episode.title, True, title_colour)
    series_text = FONT.render(series_words, True, series_colour)
    doctor_text = FONT.render(episode.doctor, True, doctor_colour)
    era_text = FONT.render(episode.era, True, era_colour)
    writer_text = FONT.render(episode.writer, True, writer_colour)
    director_text = FONT.render(episode.director, True, director_colour)
    rating_text = FONT.render(rating_words, True, rating_colour)
    title_text = pygame.transform.scale(title_text, (title_text.get_width() // 4, title_text.get_height() // 4))
    series_text = pygame.transform.scale(series_text, (series_text.get_width() // 4, series_text.get_height() // 4))
    doctor_text = pygame.transform.scale(doctor_text, (doctor_text.get_width() // 4, doctor_text.get_height() // 4))
    era_text = pygame.transform.scale(era_text, (era_text.get_width() // 4, era_text.get_height() // 4))
    writer_text = pygame.transform.scale(writer_text, (writer_text.get_width() // 4, writer_text.get_height() // 4))
    director_text = pygame.transform.scale(director_text,
                                           (director_text.get_width() // 4, director_text.get_height() // 4))
    rating_text = pygame.transform.scale(rating_text, (rating_text.get_width() // 4, rating_text.get_height() // 4))
    text_height = 330 + (30 * Doctordle.guessed_episodes.index(episode))
    surfaces = [title_text, series_text, doctor_text, era_text, writer_text, director_text, rating_text]
    complete_surfaces = []
    text_width = 0
    for text in surfaces:
        complete_surfaces.append([text, text_width, text_height])
        if text != rating_text:
            text_width += text.get_width() + 10
        else:
            text_width += text.get_width()
    left_margin = 0
    while left_margin <= Doctordle.width - (left_margin + text_width):
        for text in complete_surfaces:
            text[1] += 1
        left_margin += 1
    Doctordle.text_surfaces += complete_surfaces

def update_search_list():
    Doctordle.search_list.clear()
    Doctordle.search_index = 0
    for episode in EPISODE_LIST:
        if Doctordle.current_search.lower() in episode.code.lower() or Doctordle.current_search.lower() in episode.title.lower():
            Doctordle.search_list.append(episode)

if __name__ == "__main__":
    while True:
        event_handler()
        draw_window()
        pygame.display.flip()
        CLOCK.tick(FPS)