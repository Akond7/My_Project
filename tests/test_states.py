import pygame

from night_security_shift.states.game_state import GameState
from night_security_shift.states.menu_state import MenuState


def test_menu_enter_starts_game():
    state = MenuState()
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)

    assert state.handle_event(event) == "playing"


def test_menu_escape_quits_game():
    state = MenuState()
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

    assert state.handle_event(event) == "quit"


def test_game_escape_returns_to_menu():
    state = GameState()
    event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

    assert state.handle_event(event) == "menu"