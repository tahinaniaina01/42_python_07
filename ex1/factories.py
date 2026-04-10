#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 23:15:51 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 00:45:33 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .creatures import Creature, Sproutling, Bloomelle, Shiftling, Morphagon
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


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
