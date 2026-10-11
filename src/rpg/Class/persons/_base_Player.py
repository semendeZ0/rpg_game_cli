from __future__ import annotations
from typing import TYPE_CHECKING
from random import randint, choice
from time import sleep

from ..calcs.Dado import Dado

if TYPE_CHECKING:
    from _base_NPC import NPC

class Player:
    def __init__(self, nome, level=1):
        self.nome = nome
        self.level = level
        self.__dinheiro = 0
        self.inventario = {
            'armas': [],
            'pocoes': []
        }
        self.arma = ''
        self.armadura = ''

        self.dado = Dado()



        # ----STATUS-----
        self.vida = 100 * self.level
        self.defesa = 5 * self.level
        self.forca = 10 * self.level
        self.agilidade = 2 * self.level
        
    
    # só um teste
    def dialogar(self, npc:NPC):
        falas = [
            [f'Como você está, {npc.nome} ?']
        ]

        fala = choice(falas)

        print(f'{self.nome}: ', end="")
        print(*fala)

        sleep(0.5)

        resp = npc.resposta(self, *fala)
        
        print(f'\n{npc.nome}: {resp}')



    def levelUp(self):
        self.level += 1