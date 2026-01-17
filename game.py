import pygame 
import random 
import sys
from color import BLACK, WHITE, GREEN, DARK_GREEN, RED
from main_menu import handle_menu_event, draw_menu
from lose_screen import handle_lose_event, draw_lose_screen
from theme import draw_overlay

pygame.init()

X, x = 800, 800

size = 20

height = X // size
width = x // size

beginning_fps = 10

GAME_NAME = "Diablo_BALL 1.0"



screen= pygame.display.set_mode((X, x))
pygame.display.set_caption(GAME_NAME)

ctrl_fps=pygame.time.Clock()

font= pygame.font.SysFont("Courier New", 20)
title_font = pygame.font.SysFont("Courier New", 40, bold=True)

def game_over():
    pygame.quit()
    sys.exit()

def draw_center_text(surface, text, y, color=WHITE, font_obj=None):
    if font_obj is None:
        font_obj = font
    rendered = font_obj.render(text, True, color)
    rect = rendered.get_rect(center=(X // 2, y))
    surface.blit(rendered, rect)

class snake():
    def __init__(self):
        self.body = [[width // 2, height // 2]]
        self.direction = [1, 0]
        self.grow = False
    
    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) == tuple(self.direction):
            return 
        self.direction = new_direction
    
    def snake_draw(self , surface):
        for i, ( x, y) in enumerate (self.body):
            if i ==0:
                pygame.draw.rect(surface, DARK_GREEN, (x * size, y * size, size, size))
            else:
                pygame.draw.rect(surface, GREEN, (x * size, y * size, size -2, size-2))
            
           
    
    def move(self):
        skull_x, skull_y = self.body[0]
        up, down = self.direction
        new_skull = ((skull_x + up) % width, (skull_y + down) % height)
        if new_skull in self.body:
            return False
        else:
            self.body.insert(0, new_skull)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            return True
        return True
    
class food():
    def __init__(self, snake_body):
        self.position = self.found_place(snake_body)
    
    def found_place(self, snake_body):
        position=(
            random.randint(0, width - 1),
            random.randint(0, height - 1))
        if position not in snake_body:
            return position
        return self.found_place(snake_body)
    
    def draw_foot (self, surface):
        x, y = self.position
        pygame.draw.rect(surface, RED, (x * size, y * size, size, size))
        
    
def interface():
    state = "menu"  # menu | playing | gameover
    fps = beginning_fps
    score = 0
    snake_game = None
    food_game = None

    def reset_game():
        nonlocal score, snake_game, food_game
        score = 0
        snake_game = snake()
        food_game = food(snake_game.body)

    running = True
    while running:
        tick = pygame.time.get_ticks() // 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()

            if event.type == pygame.KEYDOWN:
                if state == "menu":
                    action = handle_menu_event(event)
                    if action == "start":
                        reset_game()
                        state = "playing"
                    elif action == "quit":
                        game_over()

                elif state == "gameover":
                    action = handle_lose_event(event)
                    if action == "restart":
                        reset_game()
                        state = "playing"
                    elif action == "menu":
                        state = "menu"
                    elif action == "quit":
                        game_over()

                elif state == "playing":
                    if event.key == pygame.K_UP:
                        snake_game.change_direction([0, -1])
                    elif event.key == pygame.K_DOWN:
                        snake_game.change_direction([0, 1])
                    elif event.key == pygame.K_LEFT:
                        snake_game.change_direction([-1, 0])
                    elif event.key == pygame.K_RIGHT:
                        snake_game.change_direction([1, 0])

        screen.fill(BLACK)
        draw_overlay(screen, tick=tick)

        if state == "menu":
            draw_menu(screen, draw_center_text, GAME_NAME, title_font)

        elif state == "playing":
            alive = snake_game.move()
            if not alive:
                state = "gameover"
            else:
                if snake_game.body[0] == food_game.position:
                    snake_game.grow = True
                    score += 1
                    food_game = food(snake_game.body)

            snake_game.snake_draw(screen)
            food_game.draw_foot(screen)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

        elif state == "gameover":
            draw_lose_screen(screen, draw_center_text, score, title_font)

        pygame.display.flip()
        ctrl_fps.tick(fps)

if __name__ == "__main__":
    interface()
            
     
     
        
          
    
        
    
       
    
    
    


        
