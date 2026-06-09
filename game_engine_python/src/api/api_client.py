"""
API Client for ARCAD3X
Implements API Facade pattern
"""
import requests
import json
from config import API_BASE_URL, API_TIMEOUT


class APIClient:
    """Facade for all API calls"""
    
    def __init__(self, base_url=None):
        self.base_url = base_url or API_BASE_URL
        self.token = None
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
    def set_token(self, token):
        """Set JWT token for authenticated requests"""
        self.token = token
        self.session.headers.update({
            'Authorization': f'Bearer {token}'
        })
        
    def register(self, username, email, password):
        """Register new user"""
        try:
            response = self.session.post(
                f'{self.base_url}/auth/register',
                json={'username': username, 'email': email, 'password': password},
                timeout=API_TIMEOUT
            )
            return response.json() if response.ok else None
        except requests.RequestException as e:
            print(f"Registration error: {e}")
            return None
            
    def login(self, username, password):
        """Login and get JWT token"""
        try:
            response = self.session.post(
                f'{self.base_url}/auth/login',
                json={'username': username, 'password': password},
                timeout=API_TIMEOUT
            )
            if response.ok:
                data = response.json()
                if 'token' in data:
                    self.set_token(data['token'])
                return data
            return None
        except requests.RequestException as e:
            print(f"Login error: {e}")
            return None
            
    def create_game_session(self, world_id, character_id):
        """Create new game session"""
        if not self.token:
            return None
            
        try:
            response = self.session.post(
                f'{self.base_url}/game/sessions',
                json={'world_id': world_id, 'character_id': character_id},
                timeout=API_TIMEOUT
            )
            return response.json() if response.ok else None
        except requests.RequestException as e:
            print(f"Session creation error: {e}")
            return None
            
    def update_game_session(self, session_id, score, level_reached, completed):
        """Update game session with final score
        
        Idempotency guard: WHERE completed = FALSE
        Prevents double-counting on retry
        """
        if not self.token:
            return None
            
        try:
            response = self.session.patch(
                f'{self.base_url}/game/sessions/{session_id}',
                json={
                    'score': score,
                    'level_reached': level_reached,
                    'completed': completed
                },
                timeout=API_TIMEOUT
            )
            return response.json() if response.ok else None
        except requests.RequestException as e:
            print(f"Session update error: {e}")
            return None
            
    def get_leaderboard(self, world_id=None, limit=20):
        """Get global or world-specific leaderboard"""
        try:
            url = f'{self.base_url}/leaderboard'
            if world_id:
                url = f'{url}/{world_id}'
                
            response = self.session.get(
                url,
                params={'limit': limit},
                timeout=API_TIMEOUT
            )
            return response.json() if response.ok else None
        except requests.RequestException as e:
            print(f"Leaderboard error: {e}")
            return None
            
    def get_player_stats(self, player_id):
        """Get player statistics"""
        if not self.token:
            return None
            
        try:
            response = self.session.get(
                f'{self.base_url}/players/{player_id}/stats',
                timeout=API_TIMEOUT
            )
            return response.json() if response.ok else None
        except requests.RequestException as e:
            print(f"Stats error: {e}")
            return None
