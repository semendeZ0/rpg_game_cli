from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _base_Player import Player

class NPC:
    def __init__(self, nome):
        self.nome = nome
        self.afeicao = 0
        
    def resposta(self, player:Player, frase:str) -> str:
        if 'como você está' in frase.lower():
            if self.afeicao == 0:
                return 'Desculpe, eu não te conheço.'
            
            elif self.afeicao >= 5 < 20:
                return f'Ah, olá {player.nome} ! Eu estou bem! :)'
