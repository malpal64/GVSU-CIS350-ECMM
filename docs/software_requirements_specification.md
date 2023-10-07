# Overview

The purpose of this Software Requirements Specification (SRS) document is to provide a comprehensive and detailed blueprint for the development of the "Shop 'n Dash'' roguelike game. It outlines the functional and nonfunctional requirements, gameplay features, user interactions, and technical specifications needed to create an engaging and delightful gaming experience that transforms grocery shopping into a whimsical and humorous escapade. This document serves as a clear and unified reference for the game's developers, designers, and stakeholders, ensuring a common understanding of the game's objectives and facilitating its successful development and delivery to players.

# Functional Requirements

1. Movement
    1. The player shall move up one unit when the user presses the up arrow.
    2. The player shall move down one unit when the user presses the down arrow.
    3. The player shall move left one unit when the user presses the left arrow.
    4. The player shall move right one unit when the user presses the right arrow.
  
2. Procedurally Generated Levels
    1. The game shall produce unique levels.
    2. The game shall increase difficulty when continuing to the next level.
    3. The system shall generate a new level once the current level’s objectives have been reached.

3. User Tutorial and Help Guide
    1. A help guide shall be available to remind users of player controls.
    2. The user shall be able to open a menu with detailed information on gameplay rules.

4. Objectives
    1. The system shall generate new item lists that the player must collect to complete the level.
    2. The user shall have enough coins to purchase items to complete the level.
  
5. Permadeath
    1. The user when they die shall lose their progress.
    2. The user shall be able to purchase/unlock a replay of the level.
    3. The system shall change the death status if the player fails to complete an objective when the time has reached zero, or when the player’s health points has reached zero.

6. Inventory
    1. The system shall update the inventory when the player runs into an item.
    2. The system shall add 10 to coins when the player runs into a coin.

7. Character Progression
    1. The player shall have the ability to power up and increase abilities at the end of every level using coins collected by the player.
    2. The game shall include a variety of character abilities to power up such as health and special abilities. 

# Non-Functional Requirements

1. Graphics
    1. The system shall have an easy to use interface.
        1. The system shall be visually appealing. 
        1. The system shall provide clear information on character status, inventory, game world, and time.
