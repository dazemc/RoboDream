# RoboDream 

![Enabling](https://github.com/dazemc/RoboDream/assets/5232234/a7484bfe-10b7-4d79-a1ef-3822c31721f3)


**Note: This project is a work-in-progress and currently has limited functionality.**

RoboDream is an interactive 2D game under development, using the Pygame library. The current version of the game presents a character, the Swordsman, who can move and perform an attack action in a graphical environment. These actions are accompanied by sound effects and sprite animations to enhance the user experience. 

## Features 

- **Interactive Gameplay**: The Swordsman can move right or left across the screen, and perform an attack action.
- **Animations**: Each action of the Swordsman character is accompanied by a corresponding sprite animation.
- **Sound Effects**: Sound effects are played corresponding to certain actions to make the game more immersive.
- **Scalable Sprites**: The game includes a custom `SpriteSheet` class to handle sprite sheets, allowing to extract, scale, and manage individual sprites from a sprite sheet image.

## Structure

The project contains the following key Python scripts:

- `main.py`: This is the entry point of the game. It initializes Pygame, sets up the game window, handles event loop, manages the game state, and controls the rendering of the game elements on the screen.
- `fighter.py`: This script defines the `Fighter` class representing the Swordsman character. It manages the character's animations, movements, and actions, as well as the corresponding sound effects.
- `spritesheet.py`: This script defines the `SpriteSheet` class, which is used to manage the sprite sheets used for the character's animations.

The game's assets, such as images and sounds, are located in the respective folders in the project directory.

## Built with

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

## Future Work

This project is still under development. Future updates will include new characters, more interactive elements, level designs, and other enhancements to improve the game experience.

![Dead](https://github.com/dazemc/RoboDream/assets/5232234/9698f03e-53a8-4190-ad44-bf06ee05982d)
