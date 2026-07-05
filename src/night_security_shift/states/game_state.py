import pygame

from night_security_shift.settings import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


class GameState:
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLACK)

        title_font = pygame.font.Font(None, 64)
        text_font = pygame.font.Font(None, 36)

        title = title_font.render("Game placeholder", True, WHITE)
        text = text_font.render("Press Esc to return to menu", True, WHITE)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))

        screen.blit(title, title_rect)
        screen.blit(text, text_rect)