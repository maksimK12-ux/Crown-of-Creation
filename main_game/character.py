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

    def use_ability(self, ability_name, target):
        if ability_name in self.special_abilities:
            print(f"{self.name} used {ability_name} on {target.name}")
            if ability_name == 'Healing Light' and self.class_type == 'Prophet':
                self.heal(20)
            elif ability_name == 'Backstab' and self.class_type == 'Rogue':
                damage = self.attack + 10
                print(f"{self.name}'s Backstab did extra damage!")
                target.take_damage(damage)
            else: 
                target.take_damage(self.attack + 5)
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

# TODO: other bosses