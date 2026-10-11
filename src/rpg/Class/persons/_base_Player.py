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
        self.vida = 100 
        self.defesa = 5
        self.forca = 10
        
    
    def dialogar(self, npc:NPC):
        falas = [
            [f'Como você está, {npc.nome} ?']
        ]

        fala = choice(falas)

        print('Erick: ', end="")
        print(*fala)

        sleep(0.5)

        resp = npc.resposta(self, *fala)
        
        print(f'\n{npc.nome}: {resp}')



