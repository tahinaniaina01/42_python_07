#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 22:42:39 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 12:49:55 by trakotos           ###   ########.fr      #
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


class Flameling(Creature):
    def __init__(self, name: str = "Flameling", type: str = "Fire") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(
        self, name: str = "Pyrodon", type: str = "Fire/Flying"
    ) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub", type: str = "Water") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon", type: str = "Water") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
