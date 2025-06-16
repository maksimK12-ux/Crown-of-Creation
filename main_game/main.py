import tkinter as tk
import plot
from character import PlayerCharacter, Aurelia, Nero, Decimus, Harbinger
from battle import Battle
from ui import StartScreen, NarrativeScreen, ClassSelectionScreen, BattleScreen, GameOverScreen, VictoryScreen, HelpDialog

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Crown of Creation") 
        self.root.geometry("1000x600") 

        self.player = None
        self.current_battle = None
        self.current_screen_widget = None
        self.story_progression_index = 0
        self.defeated_mini_bosses = [] # Stores names of defeated bosses
        self.story_segments = [
            (plot.CROWN_CREATION, self.show_next_story_segment),
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
            # This case should ideally not be reached if last segment points to class selection or similar
            print("End of predefined story segments.")
            self.show_class_selection()


    def show_class_selection(self): 
        self._clear_current_screen()
        self.current_screen_widget = ClassSelectionScreen(self.root, self)
        self.current_screen_widget.show()

    def finalize_class_selection(self, class_type):
        player_name = "The Banished"
        self.player = PlayerCharacter(player_name, class_type) 
        print(f"Player created: {self.player.name}, Class: {self.player.class_type}")
        # After class selection, proceed to first encounter or more narrative
        self.current_boss_index = 0 # Start with the first boss
        self.initiate_next_encounter()

    def show_help_dialog(self):
        HelpDialog(self.root)    

    def initiate_next_encounter(self):
        if self.current_boss_index < len(self.boss_encounter_order):
            boss_name = self.boss_encounter_order[self.current_boss_index]
            enemy = None
            intro_text = plot.BOSS_INTROS.get(boss_name, f"You encounter {boss_name}.")

            if boss_name == "Aurelia":
                enemy = Aurelia()
            elif boss_name == "Nero":
                enemy = Nero()
            elif boss_name == "Decimus":
                enemy = Decimus()
            elif boss_name == "Harbinger":
                enemy = Harbinger()
            
            if enemy:
                # Show narrative intro for the boss first
                self._clear_current_screen()
                # The next action after this narrative is to start the battle
                self.current_screen_widget = NarrativeScreen(self.root, self, intro_text, lambda: self.start_battle(enemy))
                self.current_screen_widget.show()
            else:
                print(f"Error: Boss {boss_name} not defined.")
                self.show_victory_screen(plot.VICTORY_TEXT)
        else:
            # All bosses defeated
            self.show_victory_screen(plot.VICTORY_TEXT)


    def start_battle(self, enemy):
        if not self.player:
            print("Player not initialized!")
            self.show_start_screen()
            return

        self.current_battle = Battle(self.player, enemy, self.update_battle_ui)
        self._clear_current_screen()
        self.current_screen_widget = BattleScreen(self.root, self)
        self.current_screen_widget.show()
        self.update_battle_ui() # Initial UI update

    def update_battle_ui(self):
        if isinstance(self.current_screen_widget, BattleScreen):
            self.current_screen_widget.update_battle_ui()
        
        # Check for battle end after UI update
        if self.current_battle:
            status = self.current_battle.get_battle_status()
            if status == "victory":
                self.handle_battle_victory()
            elif status == "defeat":
                self.show_game_over_screen(plot.GAME_OVER_TEXT)


    def player_attack(self):
        if self.current_battle and self.current_battle.current_turn == self.player:
            self.current_battle._player_turn_action("attack") 

    def player_use_ability(self, ability_name):
        if self.current_battle and self.current_battle.current_turn == self.player:
            self.current_battle._player_turn_action("ability", ability_name=ability_name)

    def handle_battle_victory(self):
        if self.current_battle:
            defeated_enemy_name = self.current_battle.enemy.name
            self.current_battle.log_message(f"{defeated_enemy_name} defeated!")
            
            # Specific logic for mini-bosses 
            current_boss_identifier = self.boss_encounter_order[self.current_boss_index]
            if current_boss_identifier != "Harbinger": # Mini-boss
                 if self.player:
                    self.player.add_crown_pieces() 
                    self.defeated_mini_bosses.append(current_boss_identifier) 
                 self.current_battle.log_message(f"You obtained a piece of the Crown of Creation!")


            # Short delay or "Continue" button before next screen
            victory_message = f"You defeated {defeated_enemy_name}!"
            if current_boss_identifier != "Harbinger":
                victory_message += "\nYou feel a surge of power as you claim a piece of the Crown!"
            
            self._clear_current_screen()
            self.current_screen_widget = NarrativeScreen(self.root, self, victory_message, self.proceed_after_victory)
            self.current_screen_widget.show()
            
            self.current_battle = None # Clear current battle

    def proceed_after_victory(self):
        self.current_boss_index += 1
        if self.current_boss_index < len(self.boss_encounter_order):
            self.initiate_next_encounter()
        else: # All bosses defeated, including Harbinger
            self.show_victory_screen(plot.VICTORY_TEXT)


    def show_game_over_screen(self, message): 
        self._clear_current_screen()
        self.current_screen_widget = GameOverScreen(self.root, self, message)
        self.current_screen_widget.show()
        self.current_battle = None

    def show_victory_screen(self, message): 
        self._clear_current_screen()
        self.current_screen_widget = VictoryScreen(self.root, self, message)
        self.current_screen_widget.show()
        self.current_battle = None

    def load_game_placeholder(self):
        print("Load game function not implemented yet.")


if __name__ == '__main__':
    root = tk.Tk() 
    app = Game(root)
    root.mainloop()