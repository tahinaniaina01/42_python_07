#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/11 00:47:47 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 01:10:38 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import TransformCreatureFactory, HealingCreatureFactory


def test_healing_factory(creature_factory: HealingCreatureFactory) -> None:
    base = creature_factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    evolved = creature_factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(creature_factory: TransformCreatureFactory) -> None:
    base = creature_factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    evolved = creature_factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_healing_factory(HealingCreatureFactory())
    print()
    print("Testing Creature with transform capability")
    test_transform_factory(TransformCreatureFactory())
