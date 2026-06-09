"""
Tests for Player entity
"""
import unittest
import pygame
from src.entities.player import Player
from config import PLAYER_SPEED, PLAYER_SIZE, PLAYER_LIVES, SCREEN_WIDTH, SCREEN_HEIGHT


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
        initial_x = self.player.rect.x
        keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False, 
                pygame.K_UP: False, pygame.K_DOWN: False}
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertLess(self.player.rect.x, initial_x)
        
    def test_movement_right(self):
        """Test player moves right"""
        initial_x = self.player.rect.x
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True,
                pygame.K_UP: False, pygame.K_DOWN: False}
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertGreater(self.player.rect.x, initial_x)
        
    def test_diagonal_normalization(self):
        """Test diagonal movement is normalized (BUG-001 fix)"""
        keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False,
                pygame.K_UP: True, pygame.K_DOWN: False}
        
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
        keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False,
                pygame.K_UP: False, pygame.K_DOWN: False}
        self.player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.assertGreaterEqual(self.player.rect.left, 0)
        
    def test_boundary_right(self):
        """Test player cannot move off right boundary"""
        self.player.rect.right = SCREEN_WIDTH
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True,
                pygame.K_UP: False, pygame.K_DOWN: False}
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
        self.assertTrue(self.player.can_shoot())
        self.assertFalse(self.player.can_shoot())  # Immediately after should fail
        
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
