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
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()
        title_label = ttk.Label(self, text=plot.STORY_WELCOME, font=('Helvetica', 24, 'bold'), background="#2E2E2E",
                                foreground="#E0E0E0")
        title_label.pack(pady=(50, 20))

        start_btn = ttk.Button(self, text="Start New Game", command=self.game_app.start_new_game, style="Large.TButton")
        start_btn.pack(pady = 10)

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
        text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=15, font=('Helvetica', 12), bg="#1C1C1C",
        fg="#D0D0D0", relief=tk.FLAT, padx=10, pady=10)
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
        title_label = ttk.Label(self, text=plot.CLASS_SELECTION_PROMPT, font=('Helvetica', 16, 'bold'), background="#2E2E2E",
        foreground="#E0E0E0")
        title_label.pack(pady=20)

        self.info_label = ttk.Label(self, text="Select a class to see details.", font=('Helvetica', 10), background="#2E2E2E", 
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
        try:
            stats_info = PlayerCharacter.stats[class_type] 
            info = f"Class: {class_type}\nHP: {stats_info['hp']}, Attack: {stats_info['attack']}, Defense: {stats_info['defense']}\nAbilities: {', '
            ''.join(stats_info['abilities'])}" 
            self.info_label.config(text=info) 
        except KeyError:
            self.info_label.config(text="Error displaying class info.")

    def confirm_selection(self): 
        selected = self.selected_class_var.get() 
        if selected: 
            self.game_app.finalize_class_selection(selected) 
        else: 
            self.info_label.config(text="Please select a class.")

