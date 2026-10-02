import os
from pathlib import Path
import sys
import unittest

os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pygame
from tabuleiro import Tabuleiro
from tabuleiro_screen import TabuleiroScreen
from jogador_humano import JogadorHumano


class InteractionTests(unittest.TestCase):
    def tearDown(self):
        pygame.quit()

    def test_occupied_square_and_right_click_are_ignored(self):
        screen = TabuleiroScreen()
        board = Tabuleiro()
        board.matriz[0][0] = Tabuleiro.JOGADOR_0
        player = JogadorHumano(board, screen.buttons, Tabuleiro.JOGADOR_X)
        pygame.event.clear()
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(150,150)))
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=3, pos=(350,150)))
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(350,150)))
        self.assertEqual(player.getJogada(), (0,1))
        self.assertEqual(board.matriz[0][0], Tabuleiro.JOGADOR_0)

    def test_quit_during_turn_and_after_game(self):
        screen = TabuleiroScreen()
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        with self.assertRaises(SystemExit):
            JogadorHumano(Tabuleiro(),screen.buttons,Tabuleiro.JOGADOR_X).getJogada()
        self.assertFalse(pygame.get_init())
        screen = TabuleiroScreen()
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        screen.wait_quit_event()
        self.assertFalse(pygame.get_init())
