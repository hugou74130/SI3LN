"""
Tests for collision detection
"""
import unittest
import pygame
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.bullet import Bullet
from src.entities.bonus import Bonus
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class TestCollisions(unittest.TestCase):
    """Test cases for collision detection"""
    
    def setUp(self):
        """Set up test fixtures"""
        pygame.init()
        
    def test_bullet_hits_enemy(self):
        """Test bullet destroys enemy"""
        bullet = Bullet(100, 100)
        enemy = Enemy(100, 100)
        
        # Check collision
        self.assertTrue(pygame.sprite.collide_rect(bullet, enemy))
        
    def test_enemy_hits_player(self):
        """Test enemy damages player"""
        player = Player(100, 100)
        enemy = Enemy(100, 100)
        
        initial_lives = player.lives
        player.take_damage()
        self.assertEqual(player.lives, initial_lives - 1)
        
    def test_bonus_hits_player(self):
        """Test bonus applies effect"""
        player = Player(100, 100)
        bonus = Bonus(100, 100)
        
        initial_score = player.score
        bonus.apply(player)
        
        # Bonus should have some effect
        self.assertTrue(
            player.score > initial_score or 
            player.lives > 3 or 
            player.shield_active or 
            player.mega_shot_active
        )
        
    def test_no_collision_far_apart(self):
        """Test no collision when far apart"""
        player = Player(100, 100)
        enemy = Enemy(500, 500)
        
        self.assertFalse(pygame.sprite.collide_rect(player, enemy))
        
    def test_shield_blocks_enemy_damage(self):
        """Test shield prevents damage from enemy"""
        player = Player(100, 100)
        player.activate_shield()
        
        initial_lives = player.lives
        result = player.take_damage()
        
        self.assertFalse(result)
        self.assertEqual(player.lives, initial_lives)
        
    def tearDown(self):
        """Clean up"""
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
