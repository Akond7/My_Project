import pygame

from night_security_shift.settings import (
    DARK_GRAY,
    FPS,
    GAME_TITLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
)
from night_security_shift.utils.logger import setup_logger


class GameApp:
    def __init__(self):
        pygame.init()

        self.logger = setup_logger()
        self.logger.info("Game started")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.running = True

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

    def update(self):
        pass

    def draw(self):
        self.screen.fill(DARK_GRAY)

        title = self.font.render(GAME_TITLE, True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        self.screen.blit(title, title_rect)