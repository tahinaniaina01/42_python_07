#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 22:42:39 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 12:49:26 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import abstractmethod, ABC


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class HealCapability:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str = "Sproutling", type: str = "Grass") -> None:
        super().__init__(name, type)

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(
        self, name: str = "Bloomelle", type: str = "Grass/Fairy"
    ) -> None:
        super().__init__(name, type)

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str = "Shiftling", type: str = "Normal") -> None:
        super().__init__(name, type)
        self._attack = "attacks normally."

    def attack(self) -> str:
        return f"{self.name} {self._attack}"

    def transform(self) -> str:
        self._attack = "performs a boosted strike!"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._attack = "attacks normally"
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(
        self, name: str = "Morphagon", type: str = "Normal/Drago"
    ) -> None:
        super().__init__(name, type)
        self._attack = "attacks normally."

    def attack(self) -> str:
        return f"{self.name} {self._attack}"

    def transform(self) -> str:
        self._attack = "unleashes a devastating morph strike!"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._attack = "attacks normally"
        return f"{self.name} stabilizes its form"
