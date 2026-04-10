#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 22:42:39 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 01:13:59 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import abstractmethod


class Creature:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str = "Flameling", type: str = "Unknow") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon", type: str = "Unknow") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub", type: str = "Unknow") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon", type: str = "Unknow") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
