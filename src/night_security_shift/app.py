import pygame

from night_security_shift.settings import FPS, GAME_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH
from night_security_shift.states.game_state import GameState
from night_security_shift.states.menu_state import MenuState
from night_security_shift.utils.logger import setup_logger


class GameApp:
    def __init__(self):
        pygame.init()

        self.logger = setup_logger()
        self.logger.info("Game started")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_state_name = "menu"
        self.states = {
            "menu": MenuState(),
            "playing": GameState(),
        }

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

        self.logger.info("Game closed")
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.info("Window close button clicked")
                self.running = False
                continue

            next_state = self.current_state.handle_event(event)

            if next_state == "quit":
                self.logger.info("Exit from menu")
                self.running = False
            elif next_state in self.states:
                self.change_state(next_state)

    def change_state(self, next_state):
        if next_state == self.current_state_name:
            return

        self.logger.info(
            "State changed: %s -> %s",
            self.current_state_name,
            next_state,
        )
        self.current_state_name = next_state

    def update(self):
        self.current_state.update()

    def draw(self):
        self.current_state.draw(self.screen)

    @property
    def current_state(self):
        return self.states[self.current_state_name]