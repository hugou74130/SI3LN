"""
Enemy entity for ARCAD3X
"""
import pygame
import random
from config import ENEMY_SPEED, ENEMY_SIZE, RED


class Enemy(pygame.sprite.Sprite):
    """Enemy ship with movement patterns"""
    
    def __init__(self, x, y, pattern='basic', difficulty=1):
        super().__init__()
        self.pattern = pattern
        self.difficulty = difficulty
        self.speed = ENEMY_SPEED + (difficulty * 0.5)
        
        # Visual
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Movement
        self.direction = random.choice([-1, 1])
        self.amplitude = random.randint(30, 100)
        self.frequency = random.uniform(0.02, 0.05)
        self.start_x = x
        self.time = 0
        
    def update(self, screen_width, screen_height):
        """Update enemy position based on pattern"""
        self.time += 1
        
        if self.pattern == 'basic':
            # Straight down
            self.rect.y += self.speed
        elif self.pattern == 'zigzag':
            # Zigzag movement
            self.rect.y += self.speed
            # Use math.sin instead of pygame.math.sin
            import math
            self.rect.x = self.start_x + int(self.amplitude * math.sin(self.frequency * self.time))
        elif self.pattern == 'chase':
            # Move toward player (simplified)
            self.rect.y += self.speed
            
        # Remove if off screen
        if self.rect.top > screen_height:
            self.kill()
            
    def draw(self, screen):
        """Draw enemy"""
        screen.blit(self.image, self.rect)
