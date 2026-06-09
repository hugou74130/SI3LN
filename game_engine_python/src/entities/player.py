"""
Player entity for ARCAD3X
"""
import pygame
from config import PLAYER_SPEED, PLAYER_SIZE, PLAYER_LIVES, PLAYER_SHOOT_COOLDOWN, GREEN


class Player(pygame.sprite.Sprite):
    """Player ship controlled by user"""
    
    def __init__(self, x, y, character=None):
        super().__init__()
        self.character = character or {'name': 'Default', 'color': GREEN, 'speed_bonus': 0}
        self.speed = PLAYER_SPEED + self.character['speed_bonus']
        self.lives = PLAYER_LIVES
        self.score = 0
        self.level = 1
        self.shield_active = False
        self.mega_shot_active = False
        
        # Visual
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(self.character['color'])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        
        # Shooting cooldown
        self.last_shot = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        
    def update(self, keys, screen_width, screen_height):
        """Update player position based on input"""
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed
            
        # Normalize diagonal movement (BUG-001 fix)
        if dx != 0 and dy != 0:
            dx *= 0.707  # 1/sqrt(2)
            dy *= 0.707
            
        self.rect.x += dx
        self.rect.y += dy
        
        # Keep on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, screen_width, screen_height))
        
    def can_shoot(self):
        """Check if player can shoot (cooldown)"""
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_cooldown:
            self.last_shot = now
            return True
        return False
        
    def take_damage(self):
        """Player takes damage"""
        if self.shield_active:
            self.shield_active = False
            return False
        self.lives -= 1
        return self.lives <= 0
        
    def add_score(self, points):
        """Add points to score"""
        self.score += points
        # Level up every 1000 points
        new_level = (self.score // 1000) + 1
        if new_level > self.level:
            self.level = new_level
            
    def activate_shield(self):
        """Activate shield bonus"""
        self.shield_active = True
        
    def activate_mega_shot(self):
        """Activate mega shot bonus"""
        self.mega_shot_active = True
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN // 2
        
    def draw(self, screen):
        """Draw player with shield indicator"""
        screen.blit(self.image, self.rect)
        if self.shield_active:
            pygame.draw.circle(screen, (0, 255, 255), self.rect.center, PLAYER_SIZE // 2 + 5, 2)
            
    def to_dict(self):
        """Serialize player state"""
        return {
            'x': self.rect.centerx,
            'y': self.rect.centery,
            'lives': self.lives,
            'score': self.score,
            'level': self.level,
            'shield': self.shield_active,
            'character': self.character['name']
        }
