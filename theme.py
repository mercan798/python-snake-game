import random
import pygame


_field_cache: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}


def _get_field(w: int, h: int, count: int) -> list[tuple[int, int, int]]:
    key = (w, h, count)
    cached = _field_cache.get(key)
    if cached is not None:
        return cached

    rng = random.Random(1337)
    points: list[tuple[int, int, int]] = []
    for _ in range(count):
        x = rng.randint(0, w - 1)
        y = rng.randint(0, h - 1)
        r = rng.randint(1, 3)
        points.append((x, y, r))

    _field_cache[key] = points
    return points


def draw_overlay(screen: pygame.Surface, tick: int = 0) -> None:
    """Draw a simple starfield-style overlay."""
    w, h = screen.get_size()

    for x, y, r in _get_field(w, h, count=180):
        twinkle = (tick + x + y) % 16
        if twinkle in (0, 1):
            color = (200, 220, 255)
        elif twinkle in (2, 3):
            color = (140, 170, 255)
        else:
            color = (230, 230, 230)
        pygame.draw.circle(screen, color, (x, y), r)
