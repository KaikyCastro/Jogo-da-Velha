# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.oponente = 3 - self.tipo  

    def verificar_sequencia(self, jogador: int) -> (int, int):
        for l in range(3):
            if self.matriz[l].count(jogador) == 2 and self.matriz[l].count(Tabuleiro.DESCONHECIDO) == 1:
                return (l, self.matriz[l].index(Tabuleiro.DESCONHECIDO))

        for c in range(3):
            coluna = [self.matriz[l][c] for l in range(3)]
            if coluna.count(jogador) == 2 and coluna.count(Tabuleiro.DESCONHECIDO) == 1:
                return (coluna.index(Tabuleiro.DESCONHECIDO), c)

        diagonais = [
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for diagonal in diagonais:
            valores = [self.matriz[x][y] for x, y in diagonal]
            if valores.count(jogador) == 2 and valores.count(Tabuleiro.DESCONHECIDO) == 1:
                for x, y in diagonal:
                    if self.matriz[x][y] == Tabuleiro.DESCONHECIDO:
                        return (x, y)

        return None

    def verificar_dupla_ameaca(self) -> (int, int):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo  
                    count = 0

                    if self.verificar_sequencia(self.tipo):
                        count += 1

                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO 

                    if count >= 2:
                        return (l, c)

        return None

    def R3_a_R5(self) -> (int, int):
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for x, y in cantos:
            if self.matriz[x][y] == Tabuleiro.DESCONHECIDO:
                return (x, y)
        return None

    def R6(self) -> (int, int):
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)
        return None

    def getJogada(self) -> (int, int):
        jogada = self.verificar_sequencia(self.tipo)  
        if not jogada:
            jogada = self.verificar_sequencia(self.oponente)  
        if not jogada:
            jogada = self.verificar_dupla_ameaca()  
        if not jogada:
            jogada = self.R3_a_R5() 
        if not jogada:
            jogada = self.R6()  
        return jogada
