import random

from main_components.signs_entity import Entitys


def _signs_entity_str() -> str:
    return ", ".join(
        f"({index + 1} für {sign.name} {sign.symbol} )"
        for index, sign in enumerate(Entitys)
    )


def _read_player_input() -> str:
    return input().strip()


class CLI:
    def display_welcome(self) -> None:
        print(f"{'=' * 80}")
        print("Willkommen bei Stein Papier Schere Echse Spock")
        print()
        print("Die Regeln in kurzfassung sind:")
        print("✌️➡✋➡✊➡🦎➡🖖➡✌️➡🦎➡✋➡🖖➡✊➡✌️")
        print()
        print("Um ausführliche Regeln zu erhalten, geben Sie Bitte 'rules' ein.")
        print("Drücken Sie Enter um mit dem Spiel zu beginnen")
        print(f"{'=' * 80}")

        player_input = _read_player_input()
        if player_input == "rules":
            self.display_rules()

    def display_rules(self) -> None:
        print(f"{'=' * 80}")

        print("Sie spielen gegen einen Computer")
        print("Die Regeln sind:")
        print("- Schere schneidet Papier")
        print("- Papier bedeckt Stein")
        print("- Stein zerquetscht Echse")
        print("- Echse vergiftet Spock")
        print("- Spock zertrümmert Schere")
        print("- Schere köpft Echse")
        print("- Echse frisst Papier")
        print("- Papier widerlegt Spock")
        print("- Spock verdampft Stein")
        print("- Stein schleift Schere")
        print("Drücken Sie Enter um zum Spiel zu gelangen")
        print(f"{'=' * 80}")

        _ = _read_player_input()

    def display_round_winner(
        self, winner: str, winner_sign: Entitys, message: str
    ) -> None:
        print(f"{winner} gewinnt, denn {message}")

    def display_draw(self) -> None:
        print("Es ist ein Unentschieden")

    def display_score(self, scores: dict[str, int]) -> None:
        print("Scoreboard:")
        print(f"{'=' * 80}")
        for player, score in scores.items():
            print(f"{player}: {score}", end="\t")
        print(f"\n{'=' * 80}")

    def display_current_round(
        self,
        player: str,
        npc: str,
        player_sign: Entitys,
        npc_sign: Entitys,
    ) -> None:
        print(f"{player}'s ({player_sign.symbol}) gegen {npc}'s ({npc_sign.symbol})")
        print("...")

    def pick_player_sign(self) -> Entitys:
        while True:
            try:
                print(f"Wähle {_signs_entity_str()}:", end="\t")
                choice = int(_read_player_input())

                if choice in range(1, len(Entitys) + 1):
                    return list(Entitys)[choice - 1]

                print("Bitte wählen Sie aus den verfügbaren Optionen")
            except ValueError:
                print("Falsche Eingabe")
                continue

    def pick_npc_sign(self) -> Entitys:
        return random.choice(list(Entitys))

    def read_player_name(self) -> str:
        print("Bitte geben Sie Ihren Namen ein:", end="\t")
        return _read_player_input()

    def read_rounds(self) -> int:
        print("Wie viele Runden möchten Sie spielen?", end="\t")
        return int(_read_player_input())

    def display_continue_play(self) -> None:
        print("Möchten Sie noch einmal spielen?")
        print("Drücken Sie Enter für ja oder 'n' für nein")

    def read_continue_play(self) -> bool:
        player_input = _read_player_input()
        if player_input == "n":
            return False
        elif player_input == "":
            return True
        else:
            print("Bitte Drücken Sie Enter für ja oder 'n' für nein")
            return self.read_continue_play()

    def display_statistics(self, scores: dict[str, int], rounds: int) -> None:
        print("Statistik:")
        print(f"{'=' * 80}")
        print(f"{rounds} {'Runden' if 0 < rounds < 1 else 'Runde'} gespielt")
        for player, score in scores.items():
            print(f"{player}: {score}", end="\t")
        print(f"\n{'=' * 80}")
