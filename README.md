<div align="center">

# ✨ Krishna Cosmic Particle Reveal ✨

### A devotional particle animation built with Python and Pygame

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Pygame CE](https://img.shields.io/badge/Pygame--CE-2.5.8-2E8B57)
![License](https://img.shields.io/badge/License-All_Rights_Reserved-C62828)

<img src="Lord_Krishna.png" alt="Lord Krishna cosmic artwork" width="420">

</div>

## 🌌 About the project

Krishna Cosmic Particle Reveal is a Python animation where thousands of
colourful particles travel through a dark cosmic background, form the image of
Lord Krishna, and smoothly reveal the complete artwork.

This project demonstrates image processing, animation timing, object-oriented
programming, alpha blending and particle motion using Pygame.

## ✨ Features

- Thousands of image-based coloured particles
- Smooth spiral movement with easing
- Glowing cosmic background and animated stars
- Automatic image scaling and centring
- Complete image reveal after five seconds
- Restart and exit keyboard controls
- Clear class-based Python structure
- Compatible with Python 3.14 through Pygame-CE

## 🛠️ Technologies used

- Python 3
- Pygame-CE
- Object-Oriented Programming
- Particle animation
- Image pixel sampling
- Alpha blending

## 📁 Project structure

```text
Krishna-Particle-Reveal/
├── main.py
├── Lord_Krishna.png
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## 🚀 How to run

### 1. Download or clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Krishna-Cosmic-Particle-Reveal.git
cd Krishna-Cosmic-Particle-Reveal
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install the required package

```bash
python3 -m pip install -r requirements.txt
```

### 3. Start the animation

```bash
python3 main.py
```

Keep `Lord_Krishna.png` in the same folder as `main.py`.

## 🎮 Controls

| Key | Action |
| --- | --- |
| `R` | Restart the particle animation |
| `Esc` | Close the application |

## ⚙️ Customisation

The main timing values are available near the top of `main.py`:

```python
REVEAL_AT = 5.0
REVEAL_SECONDS = 1.5
MAX_PARTICLES = 8500
```

- Reduce `REVEAL_AT` to show the image sooner.
- Increase `MAX_PARTICLES` for more detail on a powerful computer.
- Replace `Lord_Krishna.png` to animate another permitted image.

## 🧠 What I learned

- Reading colours from individual image pixels
- Creating smooth animations using interpolation
- Organising a graphical program with Python classes
- Handling keyboard and window events
- Managing transparent surfaces and glow effects

## 👤 Author

**Karan Badhani**  
BTech CSE (AI & Data Science)

The code and artwork were created specifically for this project with
AI-assisted ideation and implementation. The project was reviewed, customised
and assembled by the author.

## 📄 License

Copyright © 2026 Karan Badhani. All Rights Reserved.

No permission is granted to reuse or redistribute the source code or artwork
without prior written permission. See the [LICENSE](LICENSE) file for details.
