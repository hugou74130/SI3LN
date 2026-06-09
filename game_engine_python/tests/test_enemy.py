"""
Tests for Enemy entity
"""
import unittest
import pygame
from src.entities.enemy import Enemy
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SIZE


class TestEnemy(unittest.TestCase):
    """Test cases for Enemy class"""
    
    def setUp(self):
        """Set up test fixtures"""
        pygame.init()
        
    def test_initial_position(self):
        """Test enemy starts at correct position"""
        enemy = Enemy(100, 50)
        self.assertEqual(enemy.rect.centerx, 100)
        self.assertEqual(enemy.rect.centery, 50)
        
    def test_basic_movement(self):
        """Test basic enemy moves downward"""
        enemy = Enemy(100, 50, 'basic')
        initial_y = enemy.rect.y
        enemy.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertGreater(enemy.rect.y, initial_y)
        
    def test_zigzag_movement(self):
        """Test zigzag enemy has horizontal movement"""
        enemy = Enemy(100, 50, 'zigzag')
        initial_x = enemy.rect.x
        
        # Update multiple times to see zigzag effect
        for _ in range(10):
            enemy.update(SCREEN_WIDTH, SCREEN_HEIGHT)
            
        # Should have moved horizontally at some point
        self.assertNotEqual(enemy.rect.x, initial_x)
        
    def test_difficulty_affects_speed(self):
        """Test higher difficulty = faster speed"""
        enemy_easy = Enemy(100, 50, 'basic', difficulty=1)
        enemy_hard = Enemy(100, 50, 'basic', difficulty=5)
        
        self.assertLess(enemy_easy.speed, enemy_hard.speed)
        
    def test_removes_off_screen(self):
        """Test enemy removes itself when off screen"""
        enemy = Enemy(100, SCREEN_HEIGHT + 100)
        enemy.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Enemy should have killed itself
        self.assertFalse(enemy.alive())
        
    def test_patterns_different(self):
        """Test different patterns have different behaviors"""
        enemy_basic = Enemy(100, 50, 'basic')
        enemy_zigzag = Enemy(100, 50, 'zigzag')
        
        self.assertNotEqual(enemy_basic.pattern, enemy_zigzag.pattern)
        
    def tearDown(self):
        """Clean up"""
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
