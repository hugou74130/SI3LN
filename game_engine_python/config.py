"""
ARCAD3X Game Engine - Configuration
"""
import os

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "ARCAD3X - Arcade Shooter"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Player settings
PLAYER_SPEED = 5
PLAYER_SIZE = 50
PLAYER_LIVES = 3
PLAYER_SHOOT_COOLDOWN = 250  # milliseconds

# Bullet settings
BULLET_SPEED = 10
BULLET_SIZE = 5

# Enemy settings
ENEMY_SPEED = 2
ENEMY_SIZE = 40
ENEMY_SPAWN_RATE = 1000  # milliseconds

# Bonus settings
BONUS_SPEED = 3
BONUS_SIZE = 30
BONUS_SPAWN_RATE = 5000  # milliseconds

# Score settings
SCORE_PER_ENEMY = 100
SCORE_PER_LEVEL = 500

# API settings
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000/api')
API_TIMEOUT = 5

# Auth settings
JWT_EXPIRY_HOURS = 24

# Game states
STATE_MENU = 'menu'
STATE_PLAYING = 'playing'
STATE_PAUSED = 'paused'
STATE_GAME_OVER = 'game_over'
STATE_LEADERBOARD = 'leaderboard'

# Asset paths
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')

# World settings
WORLDS = [
    {'id': 1, 'name': 'Space', 'color': (10, 10, 30), 'difficulty': 1},
    {'id': 2, 'name': 'Desert', 'color': (194, 178, 128), 'difficulty': 2},
    {'id': 3, 'name': 'Forest', 'color': (34, 139, 34), 'difficulty': 3},
    {'id': 4, 'name': 'Marine', 'color': (0, 105, 148), 'difficulty': 4},
    {'id': 5, 'name': 'Apocalyptic', 'color': (80, 20, 20), 'difficulty': 5},
]

# Characters
CHARACTERS = [
    {'id': 1, 'name': 'Falcon', 'color': CYAN, 'speed_bonus': 0},
    {'id': 2, 'name': 'Viper', 'color': RED, 'speed_bonus': 1},
    {'id': 3, 'name': 'Raptor', 'color': GREEN, 'speed_bonus': 2},
    {'id': 4, 'name': 'Hawk', 'color': YELLOW, 'speed_bonus': 1},
    {'id': 5, 'name': 'Eagle', 'color': MAGENTA, 'speed_bonus': 0},
    {'id': 6, 'name': 'Phoenix', 'color': (255, 100, 0), 'speed_bonus': 3},
    {'id': 7, 'name': 'Ghost', 'color': (200, 200, 200), 'speed_bonus': 2},
]
