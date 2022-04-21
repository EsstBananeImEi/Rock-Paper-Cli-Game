from main_components.ui import UI


class Scoreboard:
    def __init__(self) -> None:
        self.scores: dict[str, int] = {"Unentschieden": 0}

    def register_player(self, player: str) -> None:
        self.scores[player] = 0

    def update_score(self, player: str, score: int) -> None:
        self.scores[player] += score

    def display_score(self, ui: UI) -> None:
        ui.display_score(self.scores)
