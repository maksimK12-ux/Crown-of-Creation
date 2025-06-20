# 11SE Assessment Task 2

## By Maksim Kniazev

# Sprint 1
## Requirements defintion
### Functional Requirements
* Data Retrieval: The user must be able to view their character and the game while they play it. The user must be able to play the game and view what they're doing regarding their gameplay.
* User Interface: To interact with the system, the user must move their mouse/keypad. The user also needs a working computer and connection to the internet.
* Data Display: The user must be able to obtain certain information about their character such as their health, strength and other aspects. The output for the user must be the desired information regarding their game and character.
### Non-functional Requirements
* Performance: The system must perform to the users standards and if problems are encountered in the code, they must be solved straight away. The system must function on all computers with the most recent versions of python.
* Reliability: The system and data must be reliable to the level where the user understands everything that happens and trusts the code completely.
* Useability and Accessibility: The system must be very easily navigated and the user must know what is happening and where everything is.

## Determining Specifications
### Functional Specifications
* User Requirements: The user must be able to move their character, potentailly solve problems in-game and fight bosses. These aspects build up the game and help the user to understand what is happening and how the game works
* Inputs and Outputs: The system must accept what the user writes/chooses to do in-game such as move or fight a boss. The code must then output exactly what the user does and what they decide their character should do.
* Core features: At its core, the program must be able to run the game successfully and everything must work to the users standards. The user must be able to do various things such as move their character, fight enemies and solve puzzles
* User Interaction: To interact with the system, the user must move their arrowkeys and potentailly write things to solve puzzles. To fight the bosses, the user must choose certain attacks using the space bar.
* Error Handling: Errors I could face during the code could include a breach of data integrity, this could be solved by updating your version of python and fixing your code for bugs and glitches. Menu navigation can also be confusing for new users, this can be solved by reading and understanding the program better.
### Non-Functional Specifications
* Performance: The system must perform simple tasks to the users expectations. If these standards are not met, the maintenance of user engagement drops and the code fails. To ensure that the program is efficient, it is important to make sure that python is updated to the newest version or the version where the code was made.
* Reliability: To make the application more accessible, I could make a very in-depth README file to increase simplicity in my code. To improve the User Interface (UI), I could make it easier to understand and rely on design as well as functionality of the system
* Useability/Accesibility: An issue that I could face in the code is menu navigation doing the wrong thing. This decreases user engagement and can be solved by fixing certain aspects in the code which cause the issue. To prevent complications like data integrity and illogical calculation, user must make sure that their versions of python are fully updated.

## Use Cases

### Actors: Player/User

### Preconditions: The user must have tkinter and the plot file

### Main Flow: First of all, the user runs the code and enters the game, then the user chooses to either leave the game, start the game or get help on what to do.

### Alternative Flows (if needed): The user could leave the game and need help

### Postconditions: The expected outcome is either the user loses and the game displays game over or the user wins and a victory screen is displayed


## Use Case Diagram:
<img src="use_case_diagram.png">

## Storyboard:  
<img src="storyboard.png">

## Level 0 Data Flow Diagram:
<img src="level_0_dfd.png">

## Level 1 Data Flow Diagram:
<img src="level_1_dfd.png">

## Gantt Chart:
<img src="gantt_chart.png">

## UML Class Diagram
<img src="UML_class_diagram.png">

## Structure chart
<img src="structure_chart.png">

## Flowchart 1
<img src="flowchart1.png">

## Flowchart 2
<img src="flowchart2.png">

## Flowchart 3
<img src="flowchart3.png">

## Pseudocode

* Flow chart 1:
    BEGIN start_new_game

        PRINT "Game started"
        PRINT "-------------------------------"
        PRINT game title banner
        
        SET story_progression_index TO 0

        CALL show_next_story_segment

    END start_new_game


* Flow chart 2:

    BEGIN initiate_next_encounter

        IF current_boss_index < number_of_bosses THEN
            SET boss_name TO boss_encounter_order[current_boss_index]

            IF enemy EXISTS for boss_name THEN
                DISPLAY NarrativeScreen with intro_text
                SET next action TO start_battle(enemy)
            ELSE
                DISPLAY VictoryScreen
            ENDIF

        ELSE
            DISPLAY VictoryScreen
        ENDIF

    END initiate_next_encounter


* Flow chart 3

    BEGIN handle_battle_victory

        IF current_battle != 0 THEN

            IF status = "victory" THEN

                SET enemy_name TO current_battle.enemy.name
                PRINT enemy_name + " defeated!"
                
                SET boss_id TO boss_encounter_order[current_boss_index]

                IF boss_id != "Harbinger" THEN
                    ADD boss_id TO defeated_mini_bosses
                    LOG "You obtained a piece of the Crown of Creation!"
                ENDIF

                OUTPUT victory_text
                SET current_battle TO 0

            ENDIF

        ENDIF

    END handle_battle_victory



## End of Sprint 1 Questions (Review): 

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning: My project meets the Functional and Non-Functional requirements well as it does evrything described in them. It runs smoothly and is up to my standards. My project has a successful User Interface, Data Display and Data Retrieval. It is reliable and very useable.

### 2. Analyse the performance of your program against the key use-cases you identified: My project performs well considering the use cases I identified, the preconditions are first met, the main flow works to my expectations and the base alternative flows are succesful. Being in this stage of the code, I have not completely begun adding classes or implementing the UI but considering where I am in the project, the performance of my program is going well.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability: The quality so far is up to strandards as it is simple to understand, the structure is good and it will allow me to further progress my project much easier due to how much I understand what I need to do and what is going on. The code is easy to maintain and I predict that the final result will be very understandable and easy to maintain.

### 4. Explain the improvements that should be made in the next stage of development: In the next stage of development (Sprint 2), I will begin on making the UI which will then shape my understanding of what the result must look like. I will also add the text that will be displayed in my code and introduce the character and possible enemies. While my code now is good for Sprint 1, there is no doubt that it must be improved for further implementation of code.



## End of Sprint 2 Questions (Review): 

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning: For Sprint 2, my project meets the functional and non-functional requirements quite effectively. I have begun implementing the backstory for the game and displaying it in my UI. My functional and non-functional requirements for Sprint 2 have been met as the current performance is acceptable for where I am in my project.

### 2. Analyse the performance of your program against the key use-cases you identified: For where I am in the code, the use-cases have not entirely been met but I am working on succesfully displaying the game. For now, I have started to work on the 'quit' button which will exit the game (Alternative Flow). Although I am working on the Main Flow more in Sprint 3, for now it is successful and easily understandable.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability: My code is currently very understandable for a Sprint 2 standard. The UI is currently unfinished as I still need to add more alternative flows and work on the main flow. The readability however is very successful and simple. The structure of the code is very well prepared for future update, this is good because in Sprint 3 I will start to implement classes.

### 4. Explain the improvements that should be made in the next stage of development: In Sprint 3, I will begin to implement classes which will greatly help me enhance my code. By implementing classes, the code will become much simpler and easier to navigate. Classes will allow me to implement items and battle feature which will make my game much better than it currently is. I can also add a 'help' button to explain to the user what they must do in my game.



## End of Sprint 3 Questions (Review): 

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning: Now that I can start to add classes to my code, the game has become much easier to manoeuvre as it now has defined the main characters class options (Rogue, Pirate, etc). This effectively meets the functional and non-functional requirements as it has improved the UI and made the data easier to display.

### 2. Analyse the performance of your program against the key use-cases you identified: The performance of my program very much reflects my use cases. After the preconditions are met, the code greatly highlights the main flow and post-conditions. I have also implemented a 'quit' button and a 'help' button, these are my alternative flows. after the user either wins or loses, a winning or losing screen is displayed where the user can then choose to either quit the game or restart.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability: My code and UI is very easy to understand as the instructions are very clear and if the user is still confused, they can access a help screen which explains the goal of the game and the combat system. As described, my games structure is quite simple and the maintainability is good considering that the user has tkinter and a working version of python.

### 4. Explain the improvements that should be made in the next stage of development: In the final sprint, I need to add the bosses/fighting system, I also need to improve the UI by changing the fonts, background and overall UI. By doing this, I will have finished my code for the project. Improving the UI will make the project more understandable and simpler.



## End of Sprint 4 Questions (Review): 

### 1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning: My project meets the functional and non-functional requirements well because it does everything shown in them. Some examples of this are: data retrieval, UI, data display, performance, reliability and useablity. My program is very reliable as it currently has no complications, it is also very useable and understandable.

### 2. Analyse the performance of your program against the key use-cases you identified: Considering what is in my use-cases, the games performance is exceptional. All the pre and post conditions have been met and they work very well. The idea for the main flow has been met and the alternative flows have been added.

### 3. Assess the quality of your code in terms of readability, structure, and maintainability: My final project is very readable and understandable. The UI is very simple and easy to understand. For example, when fighting a boss, it clearly shows your remaining health and how much damage you do to the enemy. Also, when choosing a class for your character, a summary of the characters attributes is shown which makes the game very maintainable and readable. I can confidently say that there is no function which the user can't understand if they read the help window.

### 4. Explain the improvements that should be made in the next stage of development: If I were to further improve my game, I would patch vulnerabilities that the user might be exploiting. I would also potentially make the game look better by adding things such as health bars or other nifty things. I would also add a function which would save your progress in the game and load your progress if re-opening the game.


# Design (Sprint 4)
## Identify Potential Enhancements
* To enhance my code, I could add a button that would save and load my game. This would be convenient to users with not much time on their hands. I could also make the UI look better by adding things such as a healthbar, more lore and better abilities. I could also add more bosses and smaller enemies to make the game more interesting and interavtive. Adding puzzles could also be a fun way to make the game more fun and imcrease user interactiveness.

## Explain the Integration Process
* To add these features, I’d start with a save and load system by storing the player’s data (like health and progress) in a file using json. I’d create “Save” and “Load” buttons in the UI to let players continue where they left off. For the UI, I’d add a health bar using tkinter.Canvas that updates during the game. I’d also include some story text and better ability descriptions to make things clearer and more interesting. To add more enemies and bosses, I’d make new enemy types with different stats and abilities. This would make battles feel fresh and more challenging. For puzzles, I’d create separate screens or pop-ups with small challenges—like riddles or pattern games—to give players a break from fighting and make the game more fun. I’d build each part one at a time and test as I go.


## Full Breakdown of Evaluation Requirements:

### Explain how you could improve your system in future updates. Analyse the impact these updates could have on the user experience.
* In future updates of my system, as I previously covered in the last question for the sprint 4 review, I could potentially add more features into my game and remove exploits if there are any. Bug fixes and Python updates would be crucial to maintaining functionality in my project. Changes like this could be detrimental for user enjoyment and overall readability and structure of the project. To engage the user more in my project, I could add a save/load system which would greatly aid the user if they want to log off/on the game. This function would save the players progress, hp, enemy hp, etc. To implement this, I would create a save_game() and load_game() method. The save_game() method would trigger this process, writing the JSON string to a file. The load_game() method would read the JSON file and then reconstruct the games state by re-initialising the player with the saved stats. This would be beneficial to the user as it would allow for more time to enjoy the game, rather than playing it all at once, also if the user has limited time, this could propose a better alternative and allow for better time management. However, a negative of adding this is that it could be confusing and hard to understand for new users and would lead them to stop playing the game. To solve this, the user would simply look at the help window to see how to save and load the game.

### Evaluate the system in terms of how well it meets the requirements and specifications.
* At the end of my code, I believe that I met the requirements and specifications quite well, as I correctly implemented all functions in my user requirements. My code successfully accepts the expected inputs and outputs the necessary information. My final judgement is that I succesfully used Object Oriented Programming to make a functional, immersive and interesting game. I have tested my system numeerous times and I am yet to find any flaws because there aren't any. The UI and Data Retrieval are successful and everyhting that I planned out in my code works.

### Evaluate your processes in terms of project management.
* Time management was my strong suit for most aspects of this project. I managed my time well and managed to complete the code earlier than other students which only left the design and review questions. Although I did some design at the beginning of the task, including my requirements and specifications, most was left until after I finished my code. For some of the tables/charts, this made making them easier while others were more difficult to complete given that I had already completed the data for them a while ago and forgot some things. I definetely had time to add all the necessary features, as shown in my code but I believe that I could've added more features. I am happy with my current code and do not strongly wish to add more features. My GitHub commits greatly display my desired work ethic as I did the code first while other aspects were left until later.

### Peer Feedback:
* Ario (Plus, minus, interests)
+'s Game UI was fun to use, Interacting with it is also easy, The classes were very fun and each one offerd interesting unique mechanics that i had fun using , It replayable and is not just a one time play which makes it a very good game. He also followed his requirements very well and the game was overall amazing
-'s Game was a little spammy and the final boss is pretty much impossible
I's The games story is very cool i wish it was built upon more.

* Rufus (Plus, minus, interests)
+'s: Games UI is simple and yields expected outputs, and each class acts as its own different kind of game / difficulty level. As mentioned in the fuctional requirements, you can enter enemy combat.
-'s: The Game feels a little repetitive and lacks some of the functionality mentioned in the functional requirements (movement and puzzle solving) which is unfortunate.
I's: Trying to beat the game on pirate is very funny because its litterally impossible.

### Justify your use of OOP class features
* The design of the "Crown of Creation" game is fundamentally rooted in Object-Oriented Programming (OOP) principles to ensure modularity, reusability, and maintainability. 

I encapsulated battle logic within the Battle class by managing player, enemy, current_turn, and internal battle_log as instance data, and providing methods like log_message, get_battle_status, and _player_turn_action. This hides complexity from external code and ensures internal state isn’t accidentally manipulated—clearly exhibiting encapsulation. By naming the player action method _player_turn_action with a leading underscore, I signal its intended privacy while maintaining a clean interface. I avoid letting outside modules tamper with battle state directly, which keeps the system robust and easy to maintain. This is classic encapsulation.

My use of instance methods like enemy_turn and get_log avoids any static/class pollution and keeps battle behavior tied to context. This focused responsibility adheres to the Single Responsibility Principle (SRP). I started with a base Character class encapsulating shared data (name, hp, etc.) and behavior (take_damage, deal_damage, heal, is_alive, display_stats). This centralizes shared logic, avoids code duplication, and makes it easy to introduce new character types with minimal changes—an embodiment of inheritance and code reuse.

PlayerCharacter extends Character to add class-specific stats, an inventory system, and a flexible ability mechanism. By mapping ability names to internal methods like _ability_backstab, I employed the Strategy-esque pattern, this is polymorphism via method references. It’s clean, scalable, and removes the need for long if-else chains. Similarly, Enemy subclasses (e.g., Aurelia, Nero) inherit from Character and pass their own stats in the constructor, an example of proper use of inheritance for “is-a” relationships. If I later want to add new enemy behavior, I could override methods like basic_attack, showing extensibility via polymorphism. Furthermore, I chose composition wisely: PlayerCharacter contains an inventory list of Item objects (from items.py), adhering to the principle of composition over deep inheritance hierarchies.

I created a generic Item base class encapsulating shared attributes like name and description, expanding via subclass CrownPiece. This simple inheritance setup allows me to extend item types in the future (e.g., weapons or consumables) without altering existing code, keeping the design open/closed. This abstraction reduces coupling, clients need only know about generic Items.

My Game class aggregates all components: UI, player, battle engine, storyline following composition: Game has a Battle, has a PlayerCharacter, and handles screens from ui.py. Teaming composition with clear instance relationships makes the code modular and maintainable. I also upheld SRP by letting Game manage flow logic (scene transitions, battle setup, victory/defeat handling) while deferring UI behavior to screen classes and combat details to Battle. This separation avoids clutter and makes future extensions (e.g., saving, loading, replay) easier. Turn-tracking and story progression are handled via instance attributes like current_boss_index and story_segments, again safely hidden and managed via class methods, no global state pollution.

I defined BaseScreen as an abstract foundation for all screens, encapsulating shared widget behavior such as show(), hide(), and clear_widgets(). Derived classes (StartScreen, BattleScreen, etc.) inherit this common logic and implement only screen-specific details. This is inheritance in action, keeping code DRY and promoting reuse. Polymorphism makes my Game classes screen-switching easy: calling hide(), destroy(), and show() works uniformly across all screens, even though each screen renders differently. I also structured BattleScreen.update_battle_ui() to invoke callbacks on the Game object dynamically, which retains a decoupled but interactive design.

Encapsulation: Internal state (e.g., HP, turn, logs) is kept private within classes, promoting safety and easier debugging.

Inheritance: Shared behaviors in Character and BaseScreen reduce redundancy and allow additions like new enemies or screens without copy-paste.

Polymorphism: Overridden methods and dynamic dispatch (abilities, enemy attacks, UI updates) give me flexibility to treat diverse objects uniformly.

Abstraction: Clients interact with high-level APIs (use_ability, start_battle, show()) without worrying about underlying details—making the system modular.

Composition over inheritance: I used composition (Game has Battle, inventory has Items) to avoid fragile hierarchies, following modern OOP guidance.

SOLID alignment: Classes are focused (SRP), open for extension but closed to modification (OCP), and replaceable via inheritance/subtyping (LSP), with no fat interfaces and dependency on abstractions (ISP/DIP). In sum, I intentionally distributed responsibilities across well-defined classes, using OOP features to produce code that is modular, extendable, maintainable, and robust. 
