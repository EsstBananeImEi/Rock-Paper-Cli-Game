from main_components.cli import CLI
from main_components.game import Game
from main_components.scoreboard import Scoreboard


def main() -> None:
    cli = CLI()
    rounds = cli.read_rounds()
    player_name = cli.read_player_name()
    game = Game(Scoreboard(), cli, player_name)
    game.greet_player()
    game.play(rounds)
    cli.display_statistics(game.scoreboard.scores, game.rounds_played)


if __name__ == "__main__":
    main()
