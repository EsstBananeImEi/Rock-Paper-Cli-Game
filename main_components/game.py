from dataclasses import dataclass

import names

from main_components.rules import get_winner
from main_components.scoreboard import Scoreboard
from main_components.ui import UI


@dataclass
class Game:
    scoreboard: Scoreboard
    ui: UI
    player_name: str
    npc_name: str = names.get_first_name()
    rounds_played: int = 0

    def turn(self) -> None:
        player_sign = self.ui.pick_player_sign()
        npc_sign = self.ui.pick_npc_sign()
        self.ui.display_current_round(
            self.player_name, self.npc_name, player_sign, npc_sign
        )

        winner, message = get_winner(player_sign, npc_sign)
        if not winner:
            self.ui.display_draw()
            self.scoreboard.update_score("Unentschieden", 1)
        elif winner == player_sign:
            self.ui.display_round_winner(self.player_name, player_sign, message)
            self.scoreboard.update_score(self.player_name, 1)
        else:
            self.ui.display_round_winner(self.npc_name, npc_sign, message)
            self.scoreboard.update_score(self.npc_name, 1)

    def greet_player(self) -> None:
        self.ui.display_welcome()

    def play(self, rounds: int) -> None:
        self.rounds_played += rounds
        if self.player_name not in self.scoreboard.scores:
            self.scoreboard.register_player(self.player_name)
            self.scoreboard.register_player(self.npc_name)
        for _ in range(rounds):
            self.turn()
            self.scoreboard.display_score(self.ui)
        self.continue_play(rounds)

    def continue_play(self, rounds: int) -> None:
        self.ui.display_continue_play()
        if not self.ui.read_continue_play():
            return
        self.play(rounds)
