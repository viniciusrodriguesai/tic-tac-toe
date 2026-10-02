# Tic-Tac-Toe with a rule-based opponent

A Python/Pygame course project developed for the Data Structures course taught by Professor Gilberto Farias. A human plays X against a computer playing O in a graphical 3×3 board. The computer uses programmed heuristics rather than a trained machine learning model.

## Run locally

Create and activate a Python 3 virtual environment, then run from the repository root:

```bash
python -m pip install -r requirements.txt
python main.py
```

A graphical desktop is required. Click an empty square to play. The computer starts, and the window displays the winner or draw after the game.

## Code organization

- `tabuleiro.py`: board state and winner detection.
- `jogador_ia.py`: computer move rules.
- `jogador_humano.py`: mouse input.
- `tabuleiro_screen.py` and `buttons.py`: Pygame rendering and buttons.
- `jogo_velha.py`: turn sequence; `main.py`: entry point.

## Status

Historical course project. Two automated Pygame interaction tests cover occupied-square rejection, left-click selection and closing the window during a turn or after a game. No unbeatable-opponent claim is made. Board rendering and QUIT handling were verified with Pygame 2.6.1, Python 3.12.14 and SDL dummy drivers. Closing the window now terminates both the human-input loop and the end-of-game wait instead of continuing after pygame.quit(). Full manual gameplay and an unbeatable-opponent claim remain unverified.

## License

[MIT](LICENSE).

## Interaction checks

```bash
python -m unittest discover -s tests -v
```

Tests use SDL dummy video/audio and do not replace full manual gameplay.
