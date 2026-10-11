from  .._base_Player import Player

class Assassin(Player):
    def __init__(self, nome, level=1):
        super().__init__(nome, level)

        self.vida = 85
        self.forca = 20
