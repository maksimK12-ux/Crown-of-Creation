class Character:
    def __init__(self, name, max_hp, attack, defense, level=1):
        pass
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.is_alive_status = True
        
    def take_damage(self, amount):
        damage_taken = max(0, amount - self.defense)
        self.hp -= damage_taken
        if self.hp <= 0:
            self.hp = 0
            self.is_alive_status = False
        return damage_taken
    
    def deal_damage(self, target):
        if self.is_alive():
            damage_dealt = self.attack
            print(f"{self.name} attacks {target.name}.")
            return target.take_damage(damage_dealt)
        return 0
    
    def heal(self, amount):
        if self.is_alive():
            self.hp = min(self.max_hp, self.hp + amount)
            print(f"{self.name} heals for {amount} HP.")

    def is_alive(self):
        return self.hp > 0
    
    def display_stats(self):
        return f"Name: {self.name}\nHP:{self.hp}/{self.max_hp}\nAttack:{self.attack}\nDefense: {self.defense}"
    

class PlayerCharacter(Character):

    stats = {
        'Rogue':{'hp': 80, 'attack': 15, 'defense': 5, 'abilities': ['Backstab', 'Evasion']},
        'Knight': {'hp': 120, 'attack': 10, 'defense': 10, 'abilities': ['Shield Bash', 'Iron Will']}, 
        'Samurai': {'hp': 100, 'attack': 12, 'defense': 7, 'abilities': ['Quick Draw', 'Meditation']}, 
        'Pirate': {'hp': 90, 'attack': 14, 'defense': 6, 'abilities': ['Plunder', 'Booze Strength']}, 
        'Prophet': {'hp': 70, 'attack': 8, 'defense': 4, 'abilities': ['Healing Light', 'Ivy Curse']},
        'KILLER': {'hp': 1000, 'attack': 70, 'defense': 1000, 'abilities': ['Healing Light', 'Ivy Curse']}
    }

    def __init__(self, name, class_type):

        if class_type not in PlayerCharacter.stats:
            raise ValueError(f"Unknown class type: {class_type}")
        
        class_stats = PlayerCharacter.stats[class_type]
        # Fro example:
            # class_type == Samurai
            # class_stats = {'hp': 100, 'attack': 12, 'defense': 7, 'abilities': ['Quick Draw', 'Meditation']}
        super().__init__(name, class_stats['hp'], class_stats['attack'], class_stats['defense'])
        self.class_type = class_type
        self.inventory = []
        self.crown_pieces = 0
        self.special_abilities = class_stats['abilities']
        self.experience_points = 0

    def add_crown_pieces(self):
        self.crown_pieces += 1
        print(f"{self.name} has received a piece of the Crown of Creation! Pieces: {self.crown_pieces}")
        from items import CrownPiece
        self.add_to_inventory(CrownPiece(f"Crown piece number {self.crown_pieces}"))

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory.")

    def _ability_backstab(self, target):
        multiplier = 1.75
        damage = int(self.attack * multiplier)
        damage_done = target.take_damage(damage)
        print(f"{self.name} uses Backstab for a devastating {damage_done} damage!")

    def _ability_evasion(self, target):
        percentage = 0.15
        heal_amount = int(self.max_hp * percentage)
        self.heal(heal_amount)
        print(f"{self.name} uses Evasion to recover {heal_amount} HP.")

    def _ability_shield_bash(self, target):
        multiplier = 2.25
        damage = int(self.attack * multiplier)
        damage_done = target.take_damage(damage)
        print(f"{self.name} performs a Shield Bash, dealing {damage_done} damage.")

    def _ability_iron_will(self, target):
        percentage = 0.30  # Heals for 30%
        heal_amount = int(self.max_hp * percentage)
        self.heal(heal_amount)
        print(f"{self.name}'s Iron Will restores {heal_amount} HP.")

    def _ability_quick_draw(self, target):
        # Overcomes 50% of the enemy's defense
        overcome_percentage = 0.50
        damage = self.attack + int(target.defense * overcome_percentage)
        damage_done = target.take_damage(damage)
        print(f"{self.name}'s Quick Draw strikes true for {damage_done} damage.")

    def _ability_meditation(self, target):
        percentage = 0.5
        heal_amount = int(self.max_hp * percentage)
        self.heal(heal_amount)
        print(f"{self.name} uses Meditation to heal for {heal_amount} HP.")

    def _ability_plunder(self, target):
        # Deals damage and steals 50% of the damage dealt as health
        damage_done = target.take_damage(self.attack)
        life_steal_percentage = 0.50
        life_stolen = int(damage_done * life_steal_percentage)
        self.heal(life_stolen)
        print(f"{self.name}'s Plunder deals {damage_done} damage and recovers {life_stolen} HP.")

    def _ability_booze_strength(self, target):
        percentage = 1.6
        heal_amount = int(self.max_hp * percentage)
        self.heal(heal_amount)
        print(f"{self.name} uses Booze Strength to recover {heal_amount} HP.")

    def _ability_healing_light(self, target):
        percentage = 1.4
        heal_amount = int(self.max_hp * percentage)
        self.heal(heal_amount)
        print(f"{self.name}'s Healing Light restores {heal_amount} HP.")

    def _ability_ivy_curse(self, target):
        damage = self.attack + 10
        print(f"{self.name}'s Ivy Curse did extra damage!")
        damage_done = target.take_damage(damage)
        print (f"{self.name} places an Ivy Curse on {target.name}, dealing {damage_done} damage.")

    def use_ability(self, ability_name, target):
        """
        Uses a dictionary to call the correct ability method.
        """
        ability_map = {
            "Backstab": self._ability_backstab,
            "Evasion": self._ability_evasion,
            "Shield Bash": self._ability_shield_bash,
            "Iron Will": self._ability_iron_will,
            "Quick Draw": self._ability_quick_draw,
            "Meditation": self._ability_meditation,
            "Plunder": self._ability_plunder,
            "Booze Strength": self._ability_booze_strength,
            "Healing Light": self._ability_healing_light,
            "Ivy Curse": self._ability_ivy_curse,
        }

        if ability_name in self.special_abilities:
            ability_method = ability_map.get(ability_name)
            if ability_method:
                print(f"{self.name} used {ability_name} on {target.name}")
                ability_method(target)
            else:
                print(f"{self.name} doesn't know how to use '{ability_name}'.")
        else:
            print(f"{self.name} doesn't know {ability_name}.")    

class Enemy(Character):
    def __init__(self, name, max_hp, attack, defense, enemy_type="Generic Enemy", loot_drops=None):
        super().__init__(name, max_hp, attack, defense)
        self.enemy_type = enemy_type
        self.loot_drops = loot_drops if loot_drops else []

    def basic_attack(self, target):
        print(f"{self.name} does a basic attck on {target.name}.")
        return self.deal_damage(target)
    
class Aurelia(Enemy):
    def __init__(self):
        super().__init__("Aurelia, the Weeping Angel", 150, 18, 8, "MiniBoss_Aurelia")

class Nero(Enemy):
    def __init__(self):
        super().__init__("Nero, The Saint of Death", 200, 21, 5, "MiniBoss_Nero")

class Decimus(Enemy):
    def __init__(self):
        super().__init__("Decimus of Karst", 250, 25, 10, "MiniBoss_Decimus")

class Harbinger(Enemy):
    def __init__(self):
        super().__init__("The Harbinger of Death", 400, 36, 15, "FinalBoss_Harbinger")
