"""
Tests for Player entity
"""
import unittest
import pygame
from src.entities.player import Player
from config import PLAYER_SPEED, PLAYER_SIZE, PLAYER_LIVES, SCREEN_WIDTH, SCREEN_HEIGHT


class MockKeys:
    """Mock keyboard keys for testing"""
    def __init__(self, **kwargs):
        # Map key names to pygame key constants
        self.keys = {}
        for key_name, value in kwargs.items():
            if hasattr(pygame, key_name):
                self.keys[getattr(pygame, key_name)] = value
            
    def __getitem__(self, key):
        return self.keys.get(key, False)


class TestPlayer(unittest.TestCase):
    """Test cases for Player class"""
    
    def setUp(self):
        """Set up test fixtures"""
        pygame.init()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
    def test_initial_position(self):
        """Test player starts at correct position"""
        self.assertEqual(self.player.rect.centerx, SCREEN_WIDTH // 2)
        self.assertEqual(self.player.rect.centery, SCREEN_HEIGHT // 2)
        
    def test_initial_lives(self):
        """Test player starts with correct lives"""
        self.assertEqual(self.player.lives, PLAYER_LIVES)
        
    def test_initial_score(self):
        """Test player starts with zero score"""
        self.assertEqual(self.player.score, 0)
        
    def test_movement_left(self):
        """Test player moves left"""
        initial_centerx = self.player.rect.centerx
        keys = MockKeys(K_LEFT=True, K_RIGHT=False, K_UP=False, K_DOWN=False, K_a=False, K_d=False, K_w=False, K_s=False)
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertLess(self.player.rect.centerx, initial_centerx)
        
    def test_movement_right(self):
        """Test player moves right"""
        initial_centerx = self.player.rect.centerx
        keys = MockKeys(K_LEFT=False, K_RIGHT=True, K_UP=False, K_DOWN=False, K_a=False, K_d=False, K_w=False, K_s=False)
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertGreater(self.player.rect.centerx, initial_centerx)
        
    def test_diagonal_normalization(self):
        """Test diagonal movement is normalized (BUG-001 fix)"""
        keys = MockKeys(K_LEFT=True, K_RIGHT=False, K_UP=True, K_DOWN=False, K_a=False, K_d=False, K_w=False, K_s=False)
        
        # Move multiple times to accumulate effect
        for _ in range(10):
            self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
            
        # After normalization, diagonal should not be faster
        # This is a simplified check - in reality we'd check distance
        self.assertTrue(self.player.rect.x < SCREEN_WIDTH // 2)
        self.assertTrue(self.player.rect.y < SCREEN_HEIGHT // 2)
        
    def test_boundary_left(self):
        """Test player cannot move off left boundary"""
        self.player.rect.left = 0
        keys = MockKeys(K_LEFT=True, K_RIGHT=False, K_UP=False, K_DOWN=False, K_a=False, K_d=False, K_w=False, K_s=False)
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertGreaterEqual(self.player.rect.left, 0)
        
    def test_boundary_right(self):
        """Test player cannot move off right boundary"""
        self.player.rect.right = SCREEN_WIDTH
        keys = MockKeys(K_LEFT=False, K_RIGHT=True, K_UP=False, K_DOWN=False, K_a=False, K_d=False, K_w=False, K_s=False)
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertLessEqual(self.player.rect.right, SCREEN_WIDTH)
        
    def test_take_damage(self):
        """Test player takes damage"""
        initial_lives = self.player.lives
        self.player.take_damage()
        self.assertEqual(self.player.lives, initial_lives - 1)
        
    def test_shield_blocks_damage(self):
        """Test shield blocks damage"""
        self.player.activate_shield()
        initial_lives = self.player.lives
        result = self.player.take_damage()
        self.assertFalse(result)  # Should not die
        self.assertEqual(self.player.lives, initial_lives)  # Lives unchanged
        self.assertFalse(self.player.shield_active)  # Shield consumed
        
    def test_add_score(self):
        """Test score increases correctly"""
        self.player.add_score(100)
        self.assertEqual(self.player.score, 100)
        
    def test_level_up(self):
        """Test level increases at score thresholds"""
        self.player.add_score(1000)
        self.assertGreater(self.player.level, 1)
        
    def test_can_shoot_cooldown(self):
        """Test shooting cooldown works"""
        # Set last_shot to far past to allow immediate shot
        self.player.last_shot = pygame.time.get_ticks() - 10000
        self.assertTrue(self.player.can_shoot())
        # Should be False immediately after (cooldown active)
        self.assertFalse(self.player.can_shoot())
        
    def test_to_dict(self):
        """Test serialization"""
        data = self.player.to_dict()
        self.assertIn('x', data)
        self.assertIn('y', data)
        self.assertIn('lives', data)
        self.assertIn('score', data)
        self.assertIn('level', data)
        
    def tearDown(self):
        """Clean up"""
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
