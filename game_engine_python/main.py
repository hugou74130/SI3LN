"""
ARCAD3X Game Engine - Main Entry Point
"""
import pygame
import sys
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE,
    STATE_MENU, STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER, STATE_LEADERBOARD
)
from src.game.game_state import GameState


def main():
    """Main game loop"""
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption(TITLE)
    
    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create game state
    game = GameState(screen)
    
    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game.state == STATE_PLAYING:
                        game.change_state(STATE_PAUSED)
                    elif game.state == STATE_PAUSED:
                        game.change_state(STATE_PLAYING)
                    elif game.state == STATE_MENU:
                        running = False
                        
                elif event.key == pygame.K_RETURN:
                    if game.state == STATE_GAME_OVER:
                        game.change_state(STATE_MENU)
                    elif game.state == STATE_MENU:
                        game.change_state(STATE_PLAYING)
                        
                elif event.key == pygame.K_SPACE:
                    if game.state == STATE_PLAYING:
                        game.shoot()
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.state == STATE_MENU:
                    # Handle menu clicks
                    mouse_pos = pygame.mouse.get_pos()
                    handle_menu_click(game, mouse_pos)
                    
        # Get key states for continuous input
        keys = pygame.key.get_pressed()
        
        # Update game
        game.update(keys)
        
        # Draw
        game.draw()
        pygame.display.flip()
        
        # Cap FPS
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()


def handle_menu_click(game, pos):
    """Handle menu click based on position"""
    x, y = pos
    # Simple zone-based menu (would be more sophisticated with actual buttons)
    if 325 < y < 375:
        game.change_state(STATE_PLAYING)
    elif 375 < y < 425:
        # Login option
        pass
    elif 425 < y < 475:
        # Leaderboard option
        pass
    elif 475 < y < 525:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
