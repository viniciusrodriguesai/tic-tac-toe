"""AI rule regressions and complete SDL-dummy games with actual click handling."""
import os
import random
import sys
from pathlib import Path
import unittest

os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pygame
from jogo_velha import JogoVelha
from jogador_ia import JogadorIA
from jogador_humano import JogadorHumano
from tabuleiro import Tabuleiro


class FullGameTests(unittest.TestCase):
    def tearDown(self):
        pygame.quit()

    def test_both_marks_win_before_block_and_do_not_mutate_board(self):
        for own, enemy in [(1,4),(4,1)]:
            for cells in [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],
                          [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]:
                b=Tabuleiro()
                for r,c in cells[:2]: b.matriz[r][c]=own
                before=[row[:] for row in b.matriz]
                self.assertEqual(JogadorIA(b,own).getJogada(),cells[2])
                self.assertEqual(b.matriz,before)
            b=Tabuleiro(); b.matriz=[[own,own,0],[enemy,enemy,0],[0,0,0]]
            self.assertEqual(JogadorIA(b,own).getJogada(),(0,2))
            b=Tabuleiro(); b.matriz=[[enemy,enemy,0],[0,own,0],[0,0,0]]
            self.assertEqual(JogadorIA(b,own).getJogada(),(0,2))

    def test_24_complete_games_use_actual_human_event_handler(self):
        for seed in range(24):
            random.seed(seed)
            game=JogoVelha()
            human=game.jogadores[1]
            original=human.getJogada
            def clicked_move():
                empty=[(r,c) for r in range(3) for c in range(3) if game.tabuleiro.matriz[r][c]==0]
                r,c=random.choice(empty)
                button=game.screen.buttons[r][c]
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=button.rect.center))
                return original()
            human.getJogada=clicked_move
            game.start()
            count=sum(v!=0 for row in game.tabuleiro.matriz for v in row)
            self.assertLessEqual(count,9)
            self.assertTrue(game.tabuleiro.tem_campeao()!=0 or count==9)
            self.assertIn(game.screen.resultado_txt,['X vencedor!','0 vencedor!','Deu velha!'])
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            game.wait_quit_event()
            self.assertFalse(pygame.get_init())
