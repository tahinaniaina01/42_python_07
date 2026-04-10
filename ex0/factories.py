#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 23:15:51 by trakotos            #+#    #+#            #
#   Updated: 2026/04/10 23:37:07 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from creatures import Aquabub, Flameling, Pyrodon, Torragon, Creature
from abc import abstractmethod


class CreatureFactory:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling(type="Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon(type="Fire/Flying")


class AquaFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub(type="Water")

    def create_evolved(self) -> Creature:
        return Torragon(type="Water")
