# -*- coding: utf-8 -*-
"""Atividade: implementar um sistema especialista que jogue o Jogo da
Velha. Implemente as regras abaixo para o jogador inteligente. Estas regras
devem ser testadas na ordem apresentada, se uma não levar a uma jogada
passe para a próxima"""
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                
        # R1: finish our own line before blocking the opponent.
        lines = [[(r, c) for c in range(3)] for r in range(3)]
        lines += [[(r, c) for r in range(3)] for c in range(3)]
        lines += [[(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]]
        opponent = Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0
        for mark in (self.tipo, opponent):
            for line in lines:
                values = [self.matriz[r][c] for r, c in line]
                if values.count(mark) == 2 and values.count(Tabuleiro.DESCONHECIDO) == 1:
                    return line[values.index(Tabuleiro.DESCONHECIDO)]
        #R2. Se houver uma jogada que crie duas sequências de duas marcações,use-a.
        for l, c in lista:
            # Simula a jogada
            self.matriz[l][c] = self.tipo
            sequencias = 0
            # Checa linhas
            for i in range(3):
                linha = [self.matriz[i][j] for j in range(3)]
                if linha.count(self.tipo) == 2 and linha.count(Tabuleiro.DESCONHECIDO) == 1:
                    sequencias += 1
            # Checa colunas
            for j in range(3):
                coluna = [self.matriz[i][j] for i in range(3)]
                if coluna.count(self.tipo) == 2 and coluna.count(Tabuleiro.DESCONHECIDO) == 1:
                    sequencias += 1
            # Checa diagonal principal
            diagonal = [self.matriz[i][i] for i in range(3)]
            if diagonal.count(self.tipo) == 2 and diagonal.count(Tabuleiro.DESCONHECIDO) == 1:
                sequencias += 1
            # Checa diagonal secundária
            diagonal = [self.matriz[i][2-i] for i in range(3)]
            if diagonal.count(self.tipo) == 2 and diagonal.count(Tabuleiro.DESCONHECIDO) == 1:
                sequencias += 1
            # Restaura o estado original
            self.matriz[l][c] = Tabuleiro.DESCONHECIDO
            if sequencias >= 2:
                return (l, c)
        # R3. Se o centro estiver livre, jogue nele.
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        #R4. Se seu oponente tiver marcado um dos cantos, marque o canto oposto
        cantos = [(0,0), (0,2), (2,0), (2,2)]
        for (l, c) in cantos:
            if self.matriz[l][c] == opponent:  # adversário
                l_oposto, c_oposto = 2 - l, 2 - c
                if self.matriz[l_oposto][c_oposto] == Tabuleiro.DESCONHECIDO:
                    return (l_oposto, c_oposto)
        # R5. Se um canto estiver livre, jogue nele.
        for (l, c) in cantos:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        