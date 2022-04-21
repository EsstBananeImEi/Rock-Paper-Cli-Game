from typing import Optional

from main_components.signs_entity import Entitys

RULES: dict[tuple[Entitys, Entitys], str] = {
    (Entitys.SCHERE, Entitys.PAPIER): "schneidet",
    (Entitys.PAPIER, Entitys.STEIN): "bedeckt",
    (Entitys.STEIN, Entitys.ECHSE): "zerquetscht",
    (Entitys.ECHSE, Entitys.SPOCK): "vergiftet",
    (Entitys.SPOCK, Entitys.SCHERE): "zertrümmert",
    (Entitys.SCHERE, Entitys.ECHSE): "köpft",
    (Entitys.ECHSE, Entitys.PAPIER): "frisst",
    (Entitys.PAPIER, Entitys.SPOCK): "widerlegt",
    (Entitys.SPOCK, Entitys.STEIN): "verdampft",
    (Entitys.STEIN, Entitys.SCHERE): "schleift",
}


def get_winner(
    player_sign: Entitys, npc_sign: Entitys
) -> tuple[Optional[Entitys], str]:
    if player_sign == npc_sign:
        return None, ""

    if (player_sign, npc_sign) in RULES:
        return (
            player_sign,
            f"{player_sign.symbol} {RULES[(player_sign, npc_sign)]} {npc_sign.symbol}",
        )

    return (
        npc_sign,
        f"{npc_sign.symbol} {RULES[(npc_sign, player_sign)]} {player_sign.symbol}",
    )
