from  .._base_Player import Player

class Assassin(Player):
    def __init__(nome, level=1):
        super().__init__(nome, level)

        self.vida = 85
        self.forca = 20
    


teste = Assassin('teste')

teste.levelUp()

print(teste.level)
print(teste.vida)
print(teste.forca)
