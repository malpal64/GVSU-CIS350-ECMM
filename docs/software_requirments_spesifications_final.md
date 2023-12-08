 # Overview

The purpose of this Software Requirements Specification (SRS) document is to provide a comprehensive and detailed blueprint for the development of the "Shop 'n Dash'' roguelike game. It outlines the functional and nonfunctional requirements, gameplay features, user interactions, and technical specifications needed to create an engaging and delightful gaming experience that transforms grocery shopping into a whimsical and humorous escapade. This document serve/s as a clear and unified reference for the game's developers, designers, and stakeholders, ensuring a common understanding of the game's objectives and facilitating its successful development and delivery to players.
 
# Software Requirements
 
3 different categories for both functional and non-functional requirements, each containing a minimum of 5 requirements.
 
## Functional Requirements
 
### Movement 
 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR1 | The player shall move up one unit when the user presses the up arrow. | 
| FR2 | The player shall move down one unit when the user presses the down arrow. | 
| FR3 | The player shall move left one unit when the user presses the left arrow. | 
| FR4 | The player shall move right one unit when the user presses the right arrow. |
| FR5 | The player shall move diagonally one unit up and right when the user presses both the up and right arrow. |
| FR6 | The player shall move diagonally one unit up and left when the user presses both the up and left arrow. |
| FR7 | The player shall move diagonally one unit down and right when the user presses both the down and right arrow. |
| FR8 | The player shall move diagonally one unit down and left when the user presses both the down and left arrow. |
 
### Procedurally Generated Levels
 
| ID  | Requirement     | 
| :-------------: | :----------: |
| FR9 | The game shall produce unique levels. | 
| FR10 | The shopping list shall randomly generate when continuing to the next level. | 
| FR11 | The system shall generate a new level once the current level’s objectives have been reached. | 
| FR12 | The system shall generate a new level once the current level’s objectives have been reached. |
| FR13 | The system shall produce levels that are contained, having walls around the entire level map. |
| FR14 | The system shall generate a new level once all items have been collected on the current level. |

### Character 
 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR15 | The system shall display the character the user selected on the character select screen. | 
| FR16 | The system shall not move the character’s position when an arrow push will result in the character colliding with the walls. | 
| FR17 | The system shall track the character’s position within the level. | 
| FR18 | The system shall remove the corresponding item from the shopping list when the player collides with an item. |
| FR19 | The system shall show the corresponding animation of the character when running or idle. |

## Non-Functional Requirements
 
### Performance
 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR1 | The system shall maintain a consistent frame rate to ensure a smooth and enjoyable player experience. | 
| NFR2 | The system shall allow the player to move in real time with minimal lag. |
| NFR3 | The system shall have minimal wait times between levels to keep players engaged. |
| NFR4 | The system shall have an easy-to-use interface. |
| NFR5 | The system shall seamlessly load items at the start of each level. | 

### Reliability
 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR6 | The system shall not crash | 
| NFR7 | The game shall have consistent graphics for each level. |
| NFR8 | The system shall support multiple players to play concurrently. |
| NFR9 | The game shall run reliably on various platforms and operating systems without significant performance discrepancies. |
| NFR10 | The system shall load in a timely manner. | 

###  Maintainability
 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR11 | The system shall be scalable. | 
| NFR12 | The system shall be able to run in any python compiler. |
| NFR13 | The system shall be maintainable. |
| NFR14 | The system shall be well documented. |
| NFR15 | The system shall have focused classes. | 

 
# Software Artifacts
 
Below are the links to all of our previously created artifacts that contributed to the development of the project.
 
[ECMM Midterm Presentation](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/docs/ECMM%20presentation.pdf)
[Project Proposal](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/docs/project-proposal.md)
[Coin Use case diagram](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/artifacts/Use_case_diagrams/coin_use_case.pdf)
[Inventory Use case diagram](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/artifacts/Use_case_diagrams/inventory_use_case.pdf)
[Movement Use case diagram](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/artifacts/Use_case_diagrams/movement_use_case.pdf)
[Midterm SRS](https://github.com/malpal64/GVSU-CIS350-ECMM/blob/main/docs/software_requirements_specification.md)
