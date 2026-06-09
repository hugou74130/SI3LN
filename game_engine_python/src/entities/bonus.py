"""
Bonus entity for ARCAD3X
"""
import pygame
import random
from config import BONUS_SPEED, BONUS_SIZE, CYAN, GREEN, MAGENTA


class Bonus(pygame.sprite.Sprite):
    """Power-up bonus falling from top"""
    
    BONUS_TYPES = {
        'shield': {'color': CYAN, 'effect': 'shield'},
        'mega_shot': {'color': (255, 100, 0), 'effect': 'mega_shot'},
        'life': {'color': GREEN, 'effect': 'life'},
        'score': {'color': MAGENTA, 'effect': 'score'},
    }
    
    def __init__(self, x, y):
        super().__init__()
        self.bonus_type = random.choice(list(self.BONUS_TYPES.keys()))
        self.effect = self.BONUS_TYPES[self.bonus_type]['effect']
        
        # Visual
        self.image = pygame.Surface((BONUS_SIZE, BONUS_SIZE))
        self.image.fill(self.BONUS_TYPES[self.bonus_type]['color'])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = BONUS_SPEED
        
    def update(self, screen_height):
        """Move bonus downward"""
        self.rect.y += self.speed
        
        # Remove if off screen
        if self.rect.top > screen_height:
            self.kill()
            
    def apply(self, player):
        """Apply bonus effect to player"""
        if self.effect == 'shield':
            player.activate_shield()
        elif self.effect == 'mega_shot':
            player.activate_mega_shot()
        elif self.effect == 'life':
            player.lives += 1
        elif self.effect == 'score':
            player.add_score(500)
            
    def draw(self, screen):
        """Draw bonus"""
        screen.blit(self.image, self.rect)
