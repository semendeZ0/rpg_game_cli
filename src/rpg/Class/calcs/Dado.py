from __future__ import annotations
from typing import TYPE_CHECKING
from random import randint

if TYPE_CHECKING:
    from .persons._base_NPC import NPC
    from .persons._base_Player import Player


class Dado:
    def __init__(self):
        self.__valor = 0


    def girar(self):
        self.__valor = randint(1, 6)


    @property
    def getValor(self):
        return self.__valor
