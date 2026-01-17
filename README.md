a snake game build with pygame wasd contorls 


# Diablo_BALL 1.0

A simple Snake-style game built with **pygame**, with a main menu, lose screen, and a starfield-style background overlay.

## Requirements

- Python 3.10+
- `pygame`

Install pygame:

```bash
pip install pygame
```

## Run

From this folder:

```bash
python game.py
```

If you use `pyenv` (example from this workspace):

```bash
/home/war-0ck/.pyenv/versions/3.12.3/bin/python game.py
```

## Controls

**Menu**
- `ENTER` — Start
- `ESC` — Quit

**In Game**
- Arrow keys — Move

**Game Over**
- `R` — Restart
- `M` — Main menu
- `ESC` — Quit

## Files

- `game.py` — main game loop and gameplay logic
- `main_menu.py` — menu screen draw + input handling
- `lose_screen.py` — lose screen draw + input handling
- `theme.py` — background overlay drawing
- `color.py` — shared color constants
