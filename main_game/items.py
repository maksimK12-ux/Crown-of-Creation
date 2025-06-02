class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"
    
class CrownPiece(Item):
    def __init__(self, piece_name, description="A fragment of immense power."):
        super().__init__(piece_name, description)