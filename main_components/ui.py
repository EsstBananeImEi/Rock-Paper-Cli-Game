from typing import Protocol

from main_components.signs_entity import Entitys


class UI(Protocol):
    def display_welcome(self) -> None:
        raise NotImplementedError()

    def display_rules(self) -> None:
        raise NotImplementedError()

    def display_round_winner(
        self, winner: str, winner_sign: Entitys, message: str
    ) -> None:
        raise NotImplementedError()

    def display_draw(self) -> None:
        raise NotImplementedError()

    def display_score(self, scores: dict[str, int]) -> None:
        raise NotImplementedError()

    def display_current_round(
        self,
        player: str,
        npc: str,
        player_sign: Entitys,
        npc_sign: Entitys,
    ) -> None:
        raise NotImplementedError()

    def pick_player_sign(self) -> Entitys:
        raise NotImplementedError()

    def pick_npc_sign(self) -> Entitys:
        raise NotImplementedError()

    def read_player_name(self) -> str:
        raise NotImplementedError()

    def display_continue_play(self) -> None:
        raise NotImplementedError()

    def read_continue_play(self) -> bool:
        raise NotImplementedError()

    def display_statistics(self, scores: dict[str, int], rounds: int) -> None:
        raise NotImplementedError()
