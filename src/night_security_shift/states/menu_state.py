import pygame

from night_security_shift.settings import DARK_GRAY, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


class MenuState:
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "playing"

            if event.key == pygame.K_ESCAPE:
                return "quit"

        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(DARK_GRAY)

        title_font = pygame.font.Font(None, 72)
        text_font = pygame.font.Font(None, 36)

        title = title_font.render("Night Security Shift", True, WHITE)
        start_text = text_font.render("Press Enter to Start", True, WHITE)
        exit_text = text_font.render("Press Esc to Exit", True, WHITE)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        screen.blit(title, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)