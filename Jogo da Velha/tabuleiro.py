# -*- coding: utf-8 -*-

from socket import SOMAXCONN


class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        for c in range(0,3):
            somaC = 0
            somaC += (self.matriz[c][0] + self.matriz[c][1] + self.matriz[c][2])
            if somaC == 12:
                return Tabuleiro.JOGADOR_X
            elif somaC == 3:
                return Tabuleiro.JOGADOR_0

        for l in range(0,3):
            somaL = 0
            somaL += (self.matriz[0][l] + self.matriz[1][l] + self.matriz[2][l])
            if somaL == 12:
                return Tabuleiro.JOGADOR_X
            elif somaL == 3:
                return Tabuleiro.JOGADOR_0

        for d1 in range(0,3):
            somaD1 = 0
            somaD1 += (self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2])
            if somaD1 == 12:
                return Tabuleiro.JOGADOR_X
            elif somaD1 == 3:
                return Tabuleiro.JOGADOR_0

        for d2 in range(0,3):
            somaD2 = 0
            somaD2 += (self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0])
            if somaD2 == 12:
                return Tabuleiro.JOGADOR_X
            elif somaD2 == 3:
                return Tabuleiro.JOGADOR_0

        
        