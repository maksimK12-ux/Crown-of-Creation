class Battle:
    def __init__(self, player, enemy, ui_update_callback=None):
        self.player = player
        self.enemy = enemy
        self.current_turn = player
        self.battle_log = []
        self.ui_upate_callback = ui_update_callback
        self.log_message(f"A wild {enemy.name} appears!")
        self.log_message(f"{player.name} is preparing for battle!")

    def log_message(self, message):
        self.battle_log.append(message)

    def _player_turn_action(self, action_type, ability_name=None):
        if not self.player.is_alive() or not self.enemy.is_alive():
            return "Battle is over."
        
        message = ""
        if action_type == "attack":
            damage_dealt = self.player.deal_damage(self.enemy)
            message = f"{self.player.name} attacks {self.enemy.name} for {damage_dealt} damage."
            if not self.enemy.is_alive():
                message += f"\n{self.enemy.name} has been defeated!"
        elif action_type == "ability" and ability_name:
            self.player.use_ability(ability_name, self.enemy)
            message = f"{self.player.name} used {ability_name}."
            if not self.enemy.is_alive():
                message += f"\n{self.enemy.name} has been defeated!"
        else:
            message = "Invalid action."

        self.log_message(message)

        if self.ui_upate_callback:
            self.ui_upate_callback()

        if self.enemy.is_alive():
            self.current_turn = self.enemy
            self.enemy_turn()

        return message
    
    def enemy_turn(self):
        if not self.enemy.is_alive() or not self.player.is_alive():
            return "Battle is over."
        
        damage_dealt = self.enemy.basic_attack(self.player)
        message = f"{self.enemy.name} strikes {self.player.name} for {damage_dealt} damage."
        if not self.player.is_alive():
            message += f"\n{self.player.name} has fallen."

        self.log_message(message)
        self.current_turn = self.player

        if self.ui_upate_callback:
            self.ui_upate_callback()
        return message
    
    def get_battle_status(self):
        if not self.player.is_alive():
            return "defeat"
        if not self.enemy.is_alive():
            return "victory"
        return "ongoing"
    
    def get_log(self):
        return "\n".join(self.battle_log[-5:])