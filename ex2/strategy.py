#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategy.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/11 01:48:40 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 08:20:34 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    @abstractmethod
    def acte(self, creature: Any) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Any) -> bool:
        if creature is None:
            return False
        attack_method = getattr(creature, "attack")
        return callable(attack_method)

    def acte(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise Exception(
                f"Invalid Creature '{creature.__class__.__name__}'"
                " for this normal strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Any) -> bool:
        if creature is None:
            return False
        attack_method = getattr(creature, "attack")
        transform_method = getattr(creature, "transform")
        revert_method = getattr(creature, "revert")
        return (
            callable(attack_method)
            and callable(transform_method)
            and callable(revert_method)
        )

    def acte(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.transform())
            print(creature.revert())
        else:
            raise Exception(
                f"Invalid Creature '{creature.__class__.__name__}'"
                " for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, creature: Any) -> bool:
        if creature is None:
            return False
        attack_method = getattr(creature, "attack")
        heal_method = getattr(creature, "heal")
        return callable(attack_method) and callable(heal_method)

    def acte(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(
                f"Invalid Creature '{creature.__class__.__name__}'"
                " for this defensive strategy"
            )
