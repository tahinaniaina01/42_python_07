#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 22:39:06 by trakotos            #+#    #+#            #
#   Updated: 2026/04/10 23:50:06 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import AquaFactory, FlameFactory, CreatureFactory


def test_factory(creature: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base = creature.create_base()
        evolved = creature.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())
        print()
    except Exception as error:
        print(f"Error: {error}")


def test_battle(flame_factory: FlameFactory, aqua_factory: AquaFactory) -> None:
    print("Testing battle")
    creture1 = flame_factory.create_base()
    creture2 = aqua_factory.create_base()
    print(creture1.describe())
    print(" vs.")
    print(creture2.describe())
    print(" fight!")
    print(creture1.attack())
    print(creture2.attack())


if __name__ == "__main__":
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    test_battle(FlameFactory(), AquaFactory())
