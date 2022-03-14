from typing import Type

from apps import tictactoe


class GameFactory:
    def __init__(self) -> None:
        self.games = {
            "tic-tac-toe": tictactoe.TicTacToe
        }

    def get(self, game: str) -> Type:
        if game not in self.games:
            raise KeyError("Game not supported yet")
        return self.games.get(game)()
