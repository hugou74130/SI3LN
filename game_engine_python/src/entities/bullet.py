"""
Bullet entity for ARCAD3X
"""
import pygame
from config import BULLET_SPEED, BULLET_SIZE, YELLOW


class Bullet(pygame.sprite.Sprite):
    """Player bullet projectile"""
    
    def __init__(self, x, y, speed=-BULLET_SPEED, is_mega=False):
        super().__init__()
        self.is_mega = is_mega
        size = BULLET_SIZE * 3 if is_mega else BULLET_SIZE
        
        # Visual
        self.image = pygame.Surface((size, size * 2))
        self.image.fill(YELLOW if not is_mega else (255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = speed
        
    def update(self, screen_height):
        """Move bullet upward"""
        self.rect.y += self.speed
        
        # Remove if off screen
        if self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill()
            
    def draw(self, screen):
        """Draw bullet"""
        screen.blit(self.image, self.rect)
