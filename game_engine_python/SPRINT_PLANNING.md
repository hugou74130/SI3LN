# ARCAD3X — Sprint Planning & Execution

## 🎯 Objectif
Livrer un MVP fonctionnel d'ARCAD3X en 3 sprints de 2 semaines chacun.

---

## 📅 Sprint 1: MVP Core (Semaines 1-2)
**Objectif:** Le jeu est jouable de bout en bout (launch → play → die → submit score)

### Tâches Assignées

| ID | Tâche | Assigné | Statut | Estimation | Dépendances |
|----|-------|---------|--------|------------|-------------|
| **T1.1** | Créer la structure du projet (dossiers, config.ini) | Hugo | ✅ Done | 2h | — |
| **T1.2** | Implémenter le State Machine (Menu, Game, GameOver) | Hugo | ✅ Done | 4h | T1.1 |
| **T1.3** | Game Loop 60 FPS (update + render) | Hugo | ✅ Done | 4h | T1.1 |
| **T1.4** | Player entity (mouvement, tir) | Hugo | ✅ Done | 3h | T1.3 |
| **T1.5** | Enemy entity (spawn, mouvement, patterns) | Hugo | ✅ Done | 4h | T1.3 |
| **T1.6** | Collision detection (AABB) | Hugo | ✅ Done | 2h | T1.4, T1.5 |
| **T1.7** | HUD (score, vies, niveau) | Hugo | ✅ Done | 2h | T1.4 |
| **T1.8** | Score submission (API POST) | Hugo | ✅ Done | 3h | T1.6 |
| **T1.9** | Guest play (sans auth) | Hugo | ✅ Done | 2h | T1.2 |
| **T1.10** | AuthSystem local (JSON) | Hugo | ✅ Done | 3h | T1.9 |

### User Stories Couvertes
- ✅ US-M1: Guest launch
- ✅ US-M2: Login/Register
- ✅ US-M3: Gameplay basique
- ✅ US-M4: HUD temps réel
- ✅ US-M5: Score submission

### Livrables
- [x] Code source structuré dans `game_engine_python/`
- [x] `main.py` se lance sans erreur
- [x] Gameplay fonctionnel (tirer, esquiver, mourir)
- [x] Scores sauvegardés localement
- [x] Tests unitaires pour Player et Collisions

### Rétrospective Sprint 1
**What went well:**
- Structure claire dès le début avec séparation des responsabilités
- State Machine facilite la navigation entre écrans
- BUG-001 identifié et fixé rapidement (normalisation diagonale ×0.707)

**Challenges:**
- Diagonale trop rapide (vitesse × √2) → Fix avec normalisation 0.707
- Collision parfois décalée → Ajustement du hitbox

**Actions d'amélioration:**
- Ajouter plus de tests pour les mouvements complexes
- Documenter les bugs connus dans un fichier dédié

---

## 📅 Sprint 2: Polish & Variété (Semaines 3-4)
**Objectif:** Ajouter de la variété et de l'accessibilité

### Tâches Assignées

| ID | Tâche | Assigné | Statut | Estimation | Dépendances |
|----|-------|---------|--------|------------|-------------|
| **T2.1** | 5 mondes (Space, Desert, Forest, Marine, Apocalyptic) | Hugo | ✅ Done | 6h | T1.5 |
| **T2.2** | Système de sélection de monde | Hugo | ✅ Done | 3h | T2.1 |
| **T2.3** | 7+ personnages jouables | Hugo | ✅ Done | 4h | T1.4 |
| **T2.4** | Écran de sélection de personnage | Hugo | ✅ Done | 3h | T2.3 |
| **T2.5** | Contrôles tactiles (mobile) | Hugo | ✅ Done | 5h | T1.4 |
| **T2.6** | Fullscreen et settings (config.ini) | Hugo | ✅ Done | 2h | T1.1 |
| **T2.7** | ResolutionManager (scaling) | Hugo | ✅ Done | 4h | T2.6 |
| **T2.8** | Bonus (shield, mega-shot) | Hugo | ✅ Done | 3h | T1.6 |
| **T2.9** | Effets visuels (explosions) | Hugo | ✅ Done | 3h | T1.5 |
| **T2.10** | Leaderboard local (top-20) | Hugo | ✅ Done | 3h | T1.8 |

### User Stories Couvertes
- ✅ US-S1: 5 mondes
- ✅ US-S2: 7 personnages
- ✅ US-S3: Desktop + mobile
- ✅ US-S4: Fullscreen et settings
- ✅ US-C1: Bonus spéciaux
- ✅ US-C2: Leaderboard local
- ✅ US-C3: Effets visuels

### Livrables
- [x] 5 mondes jouables avec visuels distincts
- [x] 7 personnages sélectionnables avec bonus de vitesse
- [x] Contrôles tactiles fonctionnels (drag-to-move)
- [x] Scaling responsive 1280×720 → toute taille
- [x] Bonus shield, mega-shot, life, score

### Rétrospective Sprint 2
**What went well:**
- ResolutionManager fonctionne sur toutes les tailles d'écran
- Assets graphiques cohérents entre les mondes
- Bonus system ajoute de la stratégie au gameplay

**Challenges:**
- Touch controls nécessitent calibration pour différentes tailles
- Performance sur mobile (optimisation des sprites nécessaire)

**Actions d'amélioration:**
- Implémenter un système de cache pour les assets
- Ajouter des tests de performance

---

## 📅 Sprint 3: Intégration API & QA (Semaines 5-6)
**Objectif:** Connecter au backend, tester, documenter

### Tâches Assignées

| ID | Tâche | Assigné | Statut | Estimation | Dépendances |
|----|-------|---------|--------|------------|-------------|
| **T3.1** | APIClient (facade HTTP) | Hugo | ✅ Done | 4h | T1.8 |
| **T3.2** | JWT authentication (login/register) | Hugo | ✅ Done | 4h | T3.1 |
| **T3.3** | Game session API (create, update) | Hugo | ✅ Done | 3h | T3.2 |
| **T3.4** | Leaderboard API (fetch global) | Hugo | ✅ Done | 2h | T3.3 |
| **T3.5** | Idempotency guard (BUG-002 fix) | Hugo | ✅ Done | 2h | T3.3 |
| **T3.6** | Tests unitaires (gameplay) | Hugo | ✅ Done | 4h | T1-T2 |
| **T3.7** | Tests d'intégration (API) | Hugo | ✅ Done | 3h | T3.1-T3.4 |
| **T3.8** | Documentation technique (STAGE3.md) | Hugo | ✅ Done | 6h | T1-T3 |
| **T3.9** | README professionnel | Hugo | ✅ Done | 2h | T3.8 |
| **T3.10** | Préparation présentation orale | Hugo | ✅ Done | 3h | T3.8-T3.9 |

### User Stories Couvertes
- Toutes les user stories Must/Should/Could Have sont complétées

### Livrables
- [x] API connectée et fonctionnelle (9 endpoints)
- [x] JWT auth sécurisé (HS256, 24h expiration)
- [x] Idempotency guard: `WHERE completed = FALSE`
- [x] Tests passent (Player, Enemy, Collisions)
- [x] Documentation complète (STAGE3.md, README.md)
- [x] Présentation 5 min préparée

### Rétrospective Sprint 3
**What went well:**
- API Facade simplifie tous les appels HTTP
- JWT avec expiration 24h = bon équilibre UX/sécurité
- BUG-002 fixé avec idempotency guard

**Challenges:**
- Sync offline/online → Queue locale + retry
- Tests d'intégration nécessitent API running

**Actions d'amélioration:**
- Ajouter des mocks pour les tests d'intégration
- Implémenter un système de retry avec backoff exponentiel

---

## 📊 Métriques de Velocity

| Sprint | Tâches Planifiées | Tâches Complétées | Velocity | Notes |
|--------|-------------------|-------------------|----------|-------|
| Sprint 1 | 10 | 10 | 100% | MVP core stable |
| Sprint 2 | 10 | 10 | 100% | Polish complet |
| Sprint 3 | 10 | 10 | 100% | API + QA done |
| **Total** | **30** | **30** | **100%** | **All delivered** |

**Burndown Chart:**
```
Sprint 1: ████████████████████ 100% (10/10)
Sprint 2: ████████████████████ 100% (10/10)
Sprint 3: ████████████████████ 100% (10/10)
```

---

## 🐛 Bug Tracker

| ID | Description | Sprint | Statut | Severité | Fix |
|----|-------------|--------|--------|----------|-----|
| BUG-001 | Diagonale trop rapide (vitesse × √2) | S1 | ✅ Fix | Medium | Normalisation ×0.707 |
| BUG-002 | Score compté 2× (retry submission) | S3 | ✅ Fix | High | `WHERE completed = FALSE` |
| BUG-003 | Collision décalée sur mobile | S2 | ✅ Fix | Low | Ajustement ResolutionManager |

---

## 🎯 Definition of Done

Pour chaque tâche:
- [x] Code écrit et commenté
- [x] Tests unitaires passent
- [x] Code review par SCM (self-review pour solo)
- [x] Merge sur `main`
- [x] Documentation mise à jour

---

## 📝 Daily Stand-ups (Exemples)

### Jour 1 — Sprint 1
**Hier:** Setup projet, structure dossiers
**Aujourd'hui:** Implémenter State Machine
**Bloqueurs:** —

### Jour 5 — Sprint 1
**Hier:** Player movement done
**Aujourd'hui:** Enemy patterns + collision
**Bloqueurs:** BUG-001 diagonale trop rapide → Fix en cours

### Jour 15 — Sprint 3
**Hier:** APIClient facade done
**Aujourd'hui:** JWT auth + tests
**Bloqueurs:** Besoin de l'API running pour tests d'intégration

---

## 🛠️ Outils Utilisés

| Outil | Usage |
|-------|-------|
| **GitHub** | Repo, issues, PRs |
| **Git** | Version control, branches feature/fix |
| **Pygame** | Game engine |
| **Django** | Backend API |
| **pytest** | Tests unitaires |
| **Discord** | Communication équipe |

---

## 📈 Rapport de Progression

### Sprint 1 Review
- **Démo:** Gameplay basique fonctionnel
- **Feedback:** Ajouter plus de patterns d'ennemis
- **Action:** Planifié pour Sprint 2

### Sprint 2 Review
- **Démo:** 5 mondes, 7 personnages, mobile controls
- **Feedback:** Performance mobile à optimiser
- **Action:** Asset caching pour Sprint 3

### Sprint 3 Review
- **Démo:** API connectée, auth JWT, leaderboard
- **Feedback:** Documentation très complète
- **Action:** Prêt pour MR !

---

*Sprint Planning — ARCAD3X MVP — Hugo Ramos — Holberton School SI3LN*
