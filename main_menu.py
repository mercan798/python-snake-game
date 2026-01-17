import pygame


WHITE = (255, 255, 255)
CYAN = (120, 200, 255)


def handle_menu_event(event):
    if event.type != pygame.KEYDOWN:
        return None
    if event.key == pygame.K_RETURN:
        return "start"
    if event.key == pygame.K_ESCAPE:
        return "quit"
    return None


def draw_menu(screen, draw_center_text, title, title_font=None):
    h = screen.get_height() // 2
    draw_center_text(screen, title, y=h - 70, color=CYAN, font_obj=title_font)
    draw_center_text(screen, "ENTER: Start", y=h - 5, color=WHITE)
    draw_center_text(screen, "ESC: Quit", y=h + 25, color=WHITE)
    draw_center_text(screen, "Good luck.", y=h + 70, color=CYAN)
