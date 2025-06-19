## Markdown

# Crown of Creation A single-player, turn-based RPG built with Python and Tkinter. 
## Description You are a banished general, cast out from a homeland now ruled by the malevolent Harbinger of Death. To reclaim your home and create a new empire, you must fight your way back, defeat three powerful mini-bosses to reassemble the legendary Crown of Creation, and finally confront the Harbinger in a decisive battle.

 ## Features 
 * **Class-Based System:** Choose from 5 unique character classes, each with different stats and special abilities. 
 * **Turn-Based Combat:** Engage in strategic battles where you can perform basic attacks or use powerful abilities. 
 * **Narrative Progression:** A story-driven adventure that unfolds through narrative screens. 
 * **Boss Encounters:** Battle three distinct mini-bosses (Aurelia, Nero, Decimus) and the final boss (The Harbinger of Death). 
 * **Graphical User Interface:** A fully graphical experience built with Python's native Tkinter library. 

 ## Dependencies 
 This project uses only Python's standard libraries (`tkinter`). No external packages are required. See `requirements.txt` for details. 

 ## How to Run 
 1. Ensure you have Python 3 installed. 
 2. Navigate to the project's root directory (`crown_of_creation/`). 
 3. Run the main game file from your terminal: ```bash python game.py ``` 
 
 ## Project Structure
 crown_of_creation/
├── game.py # Main application, game state, and screen controller
├── character.py # Character, PlayerCharacter, and Enemy class definitions
├── battle.py # Turn-based combat logic
├── ui.py # GUI screen classes (StartScreen, BattleScreen, etc.)
├── story.py # Stores all narrative and dialogue text
├── items.py # Item definitions (e.g., Crown Pieces)
└── requirements.txt # (Empty)