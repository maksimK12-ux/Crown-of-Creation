import tkinter as tk
from tkinter import ttk, scrolledtext
from character import PlayerCharacter
import plot

class BaseScreen(tk.Frame):
    def __init__(self, master, game_app, **kwargs):
        super().__init__(master, **kwargs)
        self.game_app = game_app
        self.configure(bg="#2E2E2E")

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show(self):
        self.pack(fill=tk.BOTH, expand=True)
        self.tkraise()

    def hide(self):
        self.pack_forget()

class StartScreen(BaseScreen):
    def __init__(self, master, game_app):
        super().__init__(master, game_app)
        self.configure(bg="#FFD900")
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()
        title_label = tk.Label(self, text=plot.STORY_WELCOME, font=('Helvetica', 50, 'bold'), background="#FFD900",
                                foreground="#8718B3")
        title_label.pack(pady=(50, 20))

        start_btn = ttk.Button(self, text="Start New Game", command=self.game_app.start_new_game, style="Large.TButton")
        start_btn.pack(pady = 10)

        help_btn = ttk.Button(self, text="Help", command=self.game_app.show_help_dialog, style="Large.TButton")
        help_btn.pack(pady=10)

        quit_btn = ttk.Button(self, text="Quit", command=self.master.quit, style="Large.TButton")
        quit_btn.pack(pady = 10)

class NarrativeScreen(BaseScreen):
    def __init__(self, master, game_app, narrative_text, next_action):
        super().__init__(master, game_app)
        self.narrative_text = narrative_text
        self.next_action = next_action
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()
        text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=15, font=('Courier New', 15, 'bold'), bg="#B0AAAA",
        fg="#760000", relief=tk.FLAT, padx=10, pady=10)
        text_area.insert(tk.INSERT, self.narrative_text)
        text_area.config(state=tk.DISABLED)
        text_area.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        continue_btn = ttk.Button(self, text="Continue...", command=self.next_action, style="Large.TButton")
        continue_btn.pack(pady = 20)

class ClassSelectionScreen(BaseScreen):
    def __init__(self, master, game_app):
        super().__init__(master,game_app)
        self.selected_class_var = tk.StringVar(self)
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()
        title_label = tk.Label(self, text=plot.CLASS_SELECTION_PROMPT, font=('Helvetica', 30, 'bold'), background="#0C9088",
        foreground="#252340")
        title_label.pack(pady=20)

        self.info_label = ttk.Label(self, text="Select a class to see details.", font=('Helvetica', 20), background="#2E2E2E", 
        foreground="#C0C0C0", wraplength=500)
        self.info_label.pack(pady=10)

        classes = ['Rogue', 'Knight', 'Samurai', 'Pirate', 'Prophet', 'KILLER']

        radio_frame = ttk.Frame(self, style="Dark.TFrame")
        radio_frame.pack(pady=10)
        for pc_class in classes:
            rb = ttk.Radiobutton(radio_frame, text=pc_class, variable=self.selected_class_var, value=pc_class,
            command=self.display_class_info, style="Dark.TRadiobutton")
            rb.pack(anchor=tk.W, padx=20, pady=2)

        confirm_btn = ttk.Button(self, text="Confirm Class", command=self.confirm_selection, style="Large.TButton")
        confirm_btn.pack(pady=20)

    def display_class_info(self): 
        class_type = self.selected_class_var.get() 
        try: # Accessing PlayerCharacter stats structure
            stats_info = PlayerCharacter.stats[class_type] 
            info = f"Class: {class_type}\nHP: {stats_info['hp']}, Attack: {stats_info['attack']}, Defense: {stats_info['defense']}\nAbilities: {', '
            ''.join(stats_info['abilities'])}" 
            self.info_label.config(text=info) 
        except KeyError: # Should not happen if classes list matches PlayerCharacter.stats keys 
            self.info_label.config(text="Error displaying class info.")

    def confirm_selection(self): 
        selected = self.selected_class_var.get() 
        if selected: 
            self.game_app.finalize_class_selection(selected) 
        else: 
            self.info_label.config(text="Please select a class.")

class BattleScreen(BaseScreen):
    def __init__(self, master, game_app): 
        super().__init__(master, game_app) 
        self.player_hp_var = tk.StringVar() 
        self.enemy_hp_var = tk.StringVar() 
        self.battle_log_text = None # Will be ScrolledText 
        self.ability_buttons = [] 
        self.create_widgets()

    def create_widgets(self): 
        self.clear_widgets() 
        
        # Main layout frames 
        stats_frame = ttk.Frame(self, style="Dark.TFrame") 
        stats_frame.pack(pady=10, padx=10, fill=tk.X) 

        self.player_stats_label = ttk.Label(stats_frame, text="Player:", font=('Helvetica', 17, 'bold'), style="LightText.TLabel") 
        self.player_stats_label.pack(side=tk.LEFT, padx=10) 
        self.player_hp_label = ttk.Label(stats_frame, textvariable=self.player_hp_var, font=('Helvetica', 15), style="LightText.TLabel") 
        self.player_hp_label.pack(side=tk.LEFT, padx=10) 

        self.enemy_stats_label = ttk.Label(stats_frame, text="Enemy:", font=('Helvetica', 17, 'bold'), style="LightText.TLabel") 
        self.enemy_stats_label.pack(side=tk.RIGHT, padx=10) 
        self.enemy_hp_label = ttk.Label(stats_frame, textvariable=self.enemy_hp_var, font=('Helvetica', 15), style="LightText.TLabel") 
        self.enemy_hp_label.pack(side=tk.RIGHT, padx=10)    

        # Battle Log 
        log_frame = ttk.LabelFrame(self, text="Battle Log", style="Dark.TLabelframe") 
        log_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True) 
        self.battle_log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, width=70, height=10, font=('Courier New', 14), bg="#1C1C1C", 
                                                        fg="#A0A0A0", relief=tk.FLAT) 
        self.battle_log_text.pack(pady=5, padx=5, fill=tk.BOTH, expand=True) 
        self.battle_log_text.config(state=tk.DISABLED) 
        
        # Action buttons 
        action_frame = ttk.Frame(self, style="Dark.TFrame") 
        action_frame.pack(pady=10, padx=10, fill=tk.X) 
        attack_btn = ttk.Button(action_frame, text="Attack", command=self.game_app.player_attack, style="Large.TButton") 
        attack_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X) 
        
        # Placeholder for abilities frame 
        self.abilities_frame = ttk.Frame(action_frame, style="Dark.TFrame") 
        self.abilities_frame.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X) 
        # Ability buttons will be populated by update_battle_ui

    def update_battle_ui(self): 
        player = self.game_app.player 
        enemy = self.game_app.current_battle.enemy if self.game_app.current_battle else None   

        if player: 
            self.player_stats_label.config(text=f"{player.name} ({player.class_type}) Lvl {player.level}") 
            self.player_hp_var.set(f"HP: {player.hp}/{player.max_hp}") 

        if enemy: 
            self.enemy_stats_label.config(text=f"{enemy.name} Lvl {enemy.level}") 
            self.enemy_hp_var.set(f"HP: {enemy.hp}/{enemy.max_hp}")

        if self.game_app.current_battle: 
            log_content = "\n".join(self.game_app.current_battle.battle_log) 
            self.battle_log_text.config(state=tk.NORMAL) 
            self.battle_log_text.delete(1.0, tk.END) 
            self.battle_log_text.insert(tk.END, log_content) 
            self.battle_log_text.see(tk.END) # Scroll to the bottom 
            self.battle_log_text.config(state=tk.DISABLED)

        # Update ability buttons 
        for btn in self.ability_buttons: 
            btn.destroy() 
        self.ability_buttons.clear()

        if player and player.is_alive() and self.game_app.current_battle and self.game_app.current_battle.current_turn == player: 
            for ability_name in player.special_abilities: 
                btn = ttk.Button(self.abilities_frame, text=ability_name, 
                                 command=lambda ab=ability_name: self.game_app.player_use_ability(ab), 
                                 style="Small.TButton") 
                btn.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True) 
                self.ability_buttons.append(btn) 
        else: 
            # Disable buttons if not player's turn or battle over 
            for btn in self.ability_buttons:
                btn.config(state=tk.DISABLED)

class GameOverScreen(BaseScreen): 

    def __init__(self, master, game_app, message): 
        super().__init__(master, game_app) 
        self.message = message 
        self.create_widgets() 
    
    def create_widgets(self): 
        self.clear_widgets() 
        label = ttk.Label(self, text=self.message, font=('Times New Roman', 25, 'bold'), background="#2E2E2E", foreground="#FF6B6B", wraplength=550) 
        label.pack(pady=50) 
        menu_btn = ttk.Button(self, text="Return to Main Menu", command=self.game_app.show_start_screen, style="Large.TButton") 
        menu_btn.pack(pady=20) 
        quit_btn = ttk.Button(self, text="Quit", command=self.master.quit, style="Large.TButton") 
        quit_btn.pack(pady=10)


class VictoryScreen(BaseScreen): 

    # Similar to GameOverScreen but for winning 
    def __init__(self, master, game_app, message): 
        super().__init__(master, game_app) 
        self.message = message 
        self.create_widgets()

    def create_widgets(self): 
        self.clear_widgets() 
        label = ttk.Label(self, text=self.message, font=('Times New Roman', 30, 'bold'), background="#2E2E2E", foreground="#76FF03", wraplength=550) 
        label.pack(pady=50) 
        menu_btn = ttk.Button(self, text="Return to Main Menu", command=self.game_app.show_start_screen, style="Large.TButton") 
        menu_btn.pack(pady=20) 
        quit_btn = ttk.Button(self, text="Quit", command=self.master.quit, style="Large.TButton") 
        quit_btn.pack(pady=10)

class HelpDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Crown of Creation -- Help")
        self.geometry("800x650")
        self.configure(bg="#2E2E2E")
        self.transient(master) # Keep dialog on top of the main window
        self.grab_set() # Make the dialog modal

        help_text = """
Welcome to Crown of Creation!

**THE GOAL:**
Your mission is to reclaim your homeland, The Midland of Karst, from the evil Harbinger of Death.
To do this, you must collect the three scattered pieces of the Crown of Creation and use its power to defeat the final boss.

**THE CLASSES:**
At the start of your journey, you will choose a class that defines your abilities and stats:
- Rogue: A master of high-damage attacks.
- Knight: A durable warrior with strong defensive skills.
- Samurai: A disciplined fighter balancing offense and recovery.
- Pirate: A brawler who can weaken enemies and steal life.
- Prophet: A mystic with powerful healing capabilities.
- KILLER: Choose if you want to easily beat the game (test class)

**THE JOURNEY:**
1. You must find and defeat three mini-bosses: Aurelia, Nero, and Decimus of Karst.
2. Each defeated mini-boss will grant you one piece of the Crown of Creation.
3. Once all three pieces are collected, you can face the Harbinger of Death.

**COMBAT:**
Fighting is turn-based. On your turn, you can choose to perform a basic attack or use one of your class's unique special abilities.
Choose wisely to overcome your foes!
        """

        text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, 
                                              font=('Helvetica', 14),
                                              bg="black",
                                              fg="lightgrey",
                                              relief=tk.FLAT, 
                                              padx=15, pady=15)
        text_area.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)
        text_area.insert(tk.INSERT, help_text)
        text_area.config(state=tk.DISABLED)

        # Home button to close the dialog
        home_btn = ttk.Button(self, text="Home", command=self.destroy, style="Large.TButton")
        home_btn.pack(pady=(0, 20))
