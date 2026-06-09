# ARCAD3X Game Engine

## 🎮 Description

Moteur de jeu arcade shooter développé en **Python/Pygame** pour le projet ARCAD3X.

## 📁 Structure

```
game_engine_python/
├── main.py              # Point d'entrée
├── config.py            # Configuration
├── src/
│   ├── entities/        # Joueur, ennemis, projectiles, bonus
│   ├── game/            # Game state, collisions, niveaux
│   ├── ui/              # Menus, HUD, boutons
│   ├── api/             # Client API
│   └── utils/           # Utilitaires
└── tests/               # Tests unitaires
```

## 🚀 Lancement

```bash
pip install pygame
python main.py
```

## 🎮 Contrôles

- **Flèches/WASD** — Déplacement
- **ESPACE** — Tirer
- **ÉCHAP** — Pause/Menu

## 🧪 Tests

```bash
python -m pytest tests/
```

## 👤 Auteur

Hugo Ramos — Holberton School SI3LN
