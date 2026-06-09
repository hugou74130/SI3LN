"""
Game State Manager for ARCAD3X
Implements State Machine pattern
"""
import pygame
import random
from config import (
    STATE_MENU, STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER,
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ENEMY_SPAWN_RATE, BONUS_SPAWN_RATE,
    SCORE_PER_ENEMY, SCORE_PER_LEVEL, WORLDS, CHARACTERS
)
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.bullet import Bullet
from src.entities.bonus import Bonus


class GameState:
    """Manages game states and transitions"""
    
    def __init__(self, screen):
        self.screen = screen
        self.state = STATE_MENU
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        # Game settings
        self.selected_world = None
        self.selected_character = None
        self.current_world = None
        
        # Timers
        self.last_enemy_spawn = 0
        self.last_bonus_spawn = 0
        self.game_time = 0
        
        # Font
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def change_state(self, new_state):
        """Transition to new state"""
        self.state = new_state
        
        if new_state == STATE_PLAYING:
            self.start_game()
        elif new_state == STATE_MENU:
            self.reset_game()
            
    def start_game(self):
        """Initialize new game session"""
        # Create player
        char = self.selected_character or CHARACTERS[0]
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, char)
        self.all_sprites.add(self.player)
        
        # Set world
        self.current_world = self.selected_world or WORLDS[0]
        
        # Reset timers
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.last_bonus_spawn = pygame.time.get_ticks()
        self.game_time = 0
        
    def reset_game(self):
        """Reset game objects"""
        self.enemies.empty()
        self.bullets.empty()
        self.bonuses.empty()
        self.all_sprites.empty()
        self.player = None
        self.selected_world = None
        self.selected_character = None
        
    def update(self, keys):
        """Update game logic"""
        if self.state == STATE_PLAYING:
            self.update_playing(keys)
        
    def update_playing(self, keys):
        """Update playing state"""
        if not self.player:
            return
            
        # Update player
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Update bullets
        self.bullets.update(SCREEN_HEIGHT)
        
        # Update enemies
        self.enemies.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Update bonuses
        self.bonuses.update(SCREEN_HEIGHT)
        
        # Spawn enemies
        now = pygame.time.get_ticks()
        if now - self.last_enemy_spawn > ENEMY_SPAWN_RATE:
            self.spawn_enemy()
            self.last_enemy_spawn = now
            
        # Spawn bonuses
        if now - self.last_bonus_spawn > BONUS_SPAWN_RATE:
            self.spawn_bonus()
            self.last_bonus_spawn = now
            
        # Check collisions
        self.check_collisions()
        
        # Check game over
        if self.player.lives <= 0:
            self.change_state(STATE_GAME_OVER)
            
    def spawn_enemy(self):
        """Spawn new enemy at random x position"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        patterns = ['basic', 'zigzag', 'chase']
        pattern = random.choice(patterns)
        difficulty = self.current_world['difficulty'] if self.current_world else 1
        enemy = Enemy(x, -50, pattern, difficulty)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)
        
    def spawn_bonus(self):
        """Spawn bonus at random x position"""
        x = random.randint(50, SCREEN_WIDTH - 50)
        bonus = Bonus(x, -30)
        self.bonuses.add(bonus)
        self.all_sprites.add(bonus)
        
    def check_collisions(self):
        """Check and handle all collisions"""
        if not self.player:
            return
            
        # Bullets hitting enemies
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        for enemy, bullets in hits.items():
            self.player.add_score(SCORE_PER_ENEMY)
            
        # Enemies hitting player
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            if self.player.take_damage():
                self.change_state(STATE_GAME_OVER)
                
        # Bonuses hitting player
        bonus_hits = pygame.sprite.spritecollide(self.player, self.bonuses, True)
        for bonus in bonus_hits:
            bonus.apply(self.player)
            
    def shoot(self):
        """Player shoots bullet"""
        if self.player and self.player.can_shoot():
            bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
            self.bullets.add(bullet)
            self.all_sprites.add(bullet)
            
    def draw(self):
        """Draw current state"""
        # Clear screen
        if self.current_world:
            self.screen.fill(self.current_world['color'])
        else:
            self.screen.fill((10, 10, 30))
            
        if self.state == STATE_MENU:
            self.draw_menu()
        elif self.state == STATE_PLAYING:
            self.draw_playing()
        elif self.state == STATE_PAUSED:
            self.draw_playing()
            self.draw_pause_overlay()
        elif self.state == STATE_GAME_OVER:
            self.draw_playing()
            self.draw_game_over()
            
    def draw_menu(self):
        """Draw main menu"""
        title = self.font.render("ARCAD3X", True, (255, 255, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 200))
        self.screen.blit(title, title_rect)
        
        # Menu options
        options = [
            "1. PLAY (Guest)",
            "2. LOGIN",
            "3. LEADERBOARD",
            "4. QUIT"
        ]
        for i, option in enumerate(options):
            text = self.small_font.render(option, True, (200, 200, 200))
            rect = text.get_rect(center=(SCREEN_WIDTH//2, 350 + i * 50))
            self.screen.blit(text, rect)
            
    def draw_playing(self):
        """Draw playing state"""
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        
        # Draw HUD
        if self.player:
            self.draw_hud()
            
    def draw_hud(self):
        """Draw heads-up display"""
        # Score
        score_text = self.small_font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        # Lives
        lives_text = self.small_font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))
        
        # Level
        level_text = self.small_font.render(f"Level: {self.player.level}", True, (255, 255, 255))
        self.screen.blit(level_text, (10, 70))
        
        # World
        if self.current_world:
            world_text = self.small_font.render(f"World: {self.current_world['name']}", True, (255, 255, 255))
            self.screen.blit(world_text, (SCREEN_WIDTH - 200, 10))
            
    def draw_pause_overlay(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        text = self.font.render("PAUSED", True, (255, 255, 255))
        rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(text, rect)
        
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        self.screen.blit(text, rect)
        
        # Final score
        if self.player:
            score_text = self.small_font.render(f"Final Score: {self.player.score}", True, (255, 255, 255))
            rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
            self.screen.blit(score_text, rect)
            
        # Continue prompt
        continue_text = self.small_font.render("Press ENTER for menu", True, (200, 200, 200))
        rect = continue_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        self.screen.blit(continue_text, rect)
        
    def get_final_score(self):
        """Get final score for submission"""
        if self.player:
            return {
                'score': self.player.score,
                'level': self.player.level,
                'completed': self.player.lives > 0
            }
        return None
