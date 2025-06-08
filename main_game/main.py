import tkinter as tk
from tkinter import ttk 
import plot
from character import PlayerCharacter, Aurelia
from ui import StartScreen, NarrativeScreen, ClassSelectionScreen

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Crown of Creation") 
        self.root.geometry("800x600") 

        self.player = None
        self.current_battle = None
        self.current_screen_widget = None
        self.story_progression_index = 0
        self.defeated_mini_bosses = [] # Stores names of defeated bosses
        self.story_segments = [
            (plot.STORY_START_DESERT, self.show_next_story_segment),
            (plot.STORY_JOURNEY_CONTINUES, self.show_next_story_segment),
            (plot.STORY_GATE_REVELATION, self.show_next_story_segment),
            (plot.STORY_HARBINGER_INTRO, self.show_class_selection)
        ]
        # Boss encounter sequence
        self.boss_encounter_order = ["Aurelia", "Nero", "Decimus", "Harbinger"]
        self.current_boss_index = 0

        self.show_start_screen()

    def _clear_current_screen(self):
        if self.current_screen_widget:
            self.current_screen_widget.hide() # Use hide method from BaseScreen
            self.current_screen_widget.destroy() # Destroy to free memory
            self.current_screen_widget = None

    def show_start_screen(self): 
        self._clear_current_screen()
        self.current_screen_widget = StartScreen(self.root, self)
        self.current_screen_widget.show()
        # Reset game state for a new game if returning to start screen
        self.player = None
        self.current_battle = None
        self.story_progression_index = 0
        self.defeated_mini_bosses = []
        self.current_boss_index = 0


    def start_new_game(self):
        print("Game started") 
        print("----------------------------------------------------------------------------")
        print("""
        ▒█▀▀█ █▀▀█ █▀▀█ █░░░█ █▀▀▄ 　 █▀▀█ █▀▀ 　 ▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀█ █▀▀▄ 
        ▒█░░░ █▄▄▀ █░░█ █▄█▄█ █░░█ 　 █░░█ █▀▀ 　 ▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ ▀█▀ █░░█ █░░█ 
        ▒█▄▄█ ▀░▀▀ ▀▀▀▀ ░▀░▀░ ▀░░▀ 　 ▀▀▀▀ ▀░░ 　 ▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀""")
        print("----------------------------------------------------------------------------")
        
        self.story_progression_index = 0
        self.show_next_story_segment()

    def show_next_story_segment(self):
        if self.story_progression_index < len(self.story_segments):
            narrative_text, next_action_callback = self.story_segments[self.story_progression_index]
            self.story_progression_index += 1
            self._clear_current_screen()
            self.current_screen_widget = NarrativeScreen(self.root, self, narrative_text, next_action_callback)
            self.current_screen_widget.show()
        else:
            print("End of predefined story segments.")
            self.show_class_selection()


    def show_class_selection(self): 
        self._clear_current_screen()
        self.current_screen_widget = ClassSelectionScreen(self.root, self)
        self.current_screen_widget.show()

    def finalize_class_selection(self, class_type):
        player_name = "The Banished" # TODO: consider asking for the name
        self.player = PlayerCharacter(player_name, class_type) 
        print(f"Player created: {self.player.name}, Class: {self.player.class_type}")

        self.current_boss_index = 0 # Start with the first boss
        self.initiate_next_encounter()

    def initiate_next_encounter(self):
        if self.current_boss_index < len(self.boss_encounter_order):
            boss_name = self.boss_encounter_order[self.current_boss_index]
            enemy = None
            intro_text = plot.BOSS_INTROS.get(boss_name, f"You encounter {boss_name}.")

            if boss_name == "Aurelia":
                enemy = Aurelia()
            else:
                # TODO: other bosses
                pass
            
            if enemy:
                # Show narrative intro for the boss first
                self._clear_current_screen()
                # The next action after this narrative is to start the battle
                self.current_screen_widget = NarrativeScreen(self.root, self, intro_text, lambda: self.start_battle(enemy))
                self.current_screen_widget.show()
            else:
                print(f"Error: Boss {boss_name} not defined.")
        else:
            # TODO: All bosses defeated
            pass

    def start_battle(self, enemy):
        # TODO: battle..
        print("Start battle...")
        pass

if __name__ == '__main__':
    root = tk.Tk() 
    app = Game(root)
    root.mainloop()