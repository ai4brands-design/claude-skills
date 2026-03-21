---
name: Manim Animation
description: Create programmatic animations using Python and Manim Community.
---

# Manim Skill

Manim is an animation engine for explanatory math videos.

## Prerequisites

- Python 3.8+
- FFmpeg (Must be on system PATH)
- libcairo (Usually handled by pip, but might need separate install on some systems)

## Setup

1. Run the installer: `python scripts/setup_manim.py`
2. **Important**: Ensure `ffmpeg` is installed and on your PATH.

## Usage

1. Create a python file (e.g., `scene.py`) with your animation code.
2. Run: `manim -pql scene.py SceneName`
   - `-p`: Preview the animation once done.
   - `-ql`: Low quality (faster rendering).
   - `-qh`: High quality.

## Example

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```
