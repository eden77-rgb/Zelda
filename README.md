# 🗡️ Zelda — Fan project inspiré de *A Link to the Past*

Un petit jeu 2D développé en **Python** avec **Pygame**, inspiré de l’univers de *The Legend of Zelda: A Link to the Past*.  
Objectif : reproduire une expérience “Zelda-like” avec **maps**, **caméra**, **PNJ**, **HUD**, **items**, et un système de **sauvegarde**.

> ⚠️ **Fan project / projet perso** : ce dépôt n’est pas affilié à Nintendo.  
> Les marques et éléments de l’univers Zelda appartiennent à leurs ayants droit.

---

## ✨ Features
- 🧭 **Exploration 2D** avec caméra centrée sur le joueur
- 🗺️ **Chargement de maps** (via `pytmx` / `pyscroll`)
- 🧍 **Entités** : joueur + gestion de PNJ
- 🌿🪴 **Objets destructibles** (ex : herbes, pots) + drops/items
- ❤️💎 **HUD** : vie (cœurs) + rubis
- 💾 **Sauvegarde** rapide dans un fichier JSON

--- 

## 🎮 Contrôles
| Touche    | Action                                |
|-----------|---------------------------------------|
| `Z`       | Déplacement vers le haut              |
| `Q`       | Déplacement vers la gauche            |
| `S`       | Déplacement vers le bas               |
| `D`       | Déplacement vers la droite            |
| `ESPACE`  | Lance une attaque                     |
| `TAB`     | Lance la sauvegarde de la parti       |

---

## 🧰 Stack technique
- 🐍 **Python 3.13**
- 🎮 **Pygame**
- 🗺️ **pytmx** (lecture TMX)
- 🧭 **pyscroll** (affichage / scroll de maps)

---

## 🚀 Installation & lancement

### ✅ Prérequis
- Python **3.13** installé
- Un terminal à la racine du repo

### 📦 Installer les dépendances
```bash
python -m pip install -r requirements.txt
```

### ▶️ Lancer le jeu
```bash
cd src
python main.py
```

---

## 💾 Sauvegarde
- Le jeu essaye de charger une partie depuis : `data/save.json`
- Si le fichier n’existe pas : démarrage en **nouvelle partie**
- Tu peux sauvegarder à tout moment avec **TAB**

---

## 🗂️ Structure du projet (simple)
```text
assets/     → images / sons / musiques
data/       → fichiers JSON (save, positions caméra, etc.)
maps/       → maps (TMX, etc.)
src/        → code Python (point d’entrée : main.py)
```

---

## 📸 Screenshots / GIF

### Menu
<img width="642" height="600" alt="Capture d&#39;écran 2026-02-08 151905" src="https://github.com/user-attachments/assets/6030f1db-0bb0-4cee-8fd8-88d2566fbcd5" />

### En jeu
<img width="642" height="600" alt="Capture d&#39;écran 2026-02-08 152025" src="https://github.com/user-attachments/assets/a57e96a3-a769-448c-9239-376beda7dc57" />
<img width="642" height="600" alt="Capture d&#39;écran 2026-02-08 151651" src="https://github.com/user-attachments/assets/dbe78542-6b88-4013-bd4d-74e00054b6f0" />

### Items
<img width="642" height="600" alt="Capture d&#39;écran 2026-02-08 152228" src="https://github.com/user-attachments/assets/257d9ce8-d092-4138-b517-5051bfb06762" />

---

## 🧑‍💻 Auteur
- Eden — https://github.com/eden77-rgb

---

## 📄 Licence
MIT — voir `LICENSE`.
