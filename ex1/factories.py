#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 23:15:51 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 12:48:42 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .creatures import (
    Creature,
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon,
    HealCapability,
    TransformCapability,
)
from abc import abstractmethod, ABC


class CreatureFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base(self) -> Creature | HealCapability | TransformCapability:
        pass

    @abstractmethod
    def create_evolved(
        self
    ) -> Creature | HealCapability | TransformCapability:
        pass


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
