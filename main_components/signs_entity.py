from enum import Enum
from typing import NamedTuple

Entity = NamedTuple("Entity", [("name", str), ("symbol", str)])


class Entitys(Entity, Enum):
    STEIN = Entity(name="Stein", symbol="✊")
    PAPIER = Entity(name="Papier", symbol="✋")
    SCHERE = Entity(name="Schere", symbol="✌")
    ECHSE = Entity(name="Echse", symbol="🦎")
    SPOCK = Entity(name="Spock", symbol="🖖")

    def __str__(self) -> str:
        return self.value
