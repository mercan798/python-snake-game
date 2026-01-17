import pygame


WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (120, 200, 255)


def handle_lose_event(event):
    if event.type != pygame.KEYDOWN:
        return None
    if event.key == pygame.K_r:
        return "restart"
    if event.key == pygame.K_m:
        return "menu"
    if event.key == pygame.K_ESCAPE:
        return "quit"
    return None


def draw_lose_screen(screen, draw_center_text, score, title_font=None):
    h = screen.get_height() // 2
    draw_center_text(screen, "Game Over", y=h - 70, color=RED, font_obj=title_font)
    draw_center_text(screen, f"Score: {score}", y=h - 10, color=CYAN)
    draw_center_text(screen, "R: Restart", y=h + 25, color=WHITE)
    draw_center_text(screen, "M: Main Menu", y=h + 55, color=WHITE)
    draw_center_text(screen, "ESC: Quit", y=h + 85, color=WHITE)
